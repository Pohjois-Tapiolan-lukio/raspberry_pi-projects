# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Python wrapper around the VisionBonnet Spicomm device node."""

import array
import fcntl
import struct
import sys

SPICOMM_DEV = '/dev/vision_spicomm'

SPICOMM_IOCTL_BASE = 0x8900
# TODO: 0xc0100000 should be calculated properly base on structure size.
SPICOMM_IOCTL_TRANSACT = 0xc0100000 + SPICOMM_IOCTL_BASE + 3

HEADER_SIZE = 16
DEFAULT_PAYLOAD_SIZE = 12 * 1024 * 1024  # 12 M

FLAG_ERROR = 1 << 0
FLAG_TIMEOUT = 1 << 1
FLAG_OVERFLOW = 1 << 2


class SpicommError(IOError):
    """Base class for Spicomm errors."""
    pass


class SpicommDevNotFoundError(SpicommError):
    """A usable Spicomm device node not found."""
    pass


class SpicommOverflowError(SpicommError):
    """Transaction buffer too small for response.

    Attributes:
      size: Number of bytes needed for the response.
    """

    def __init__(self, size):
        self.size = size
        super(SpicommOverflowError, self).__init__()


class SpicommTimeoutError(SpicommError):
    """Transaction timed out."""
    pass


class SpicommInternalError(SpicommError):
    """Internal unexpected error."""
    pass


def _fill_buffer(buf, timeout_s, data):
    buf[0:4] = struct.pack('I', 0)  # flags, not currently used.
    buf[4:8] = struct.pack('I', int(timeout_s * 1000))  # timeout, ms.
    buf[8:12] = struct.pack('I', len(buf))  # total buffer size.
    buf[12:16] = struct.pack('I', len(data))  # filled range of buffer.
    buf[16:16 + len(data)] = data


def _get_timeout(payload_len):
    """Conservatively assume min 5 seconds or 3 seconds per 1MB."""
    return max(3 * payload_len / 1024 / 1024, 5)


class Spicomm(object):
    """VisionBonnet Spicomm wrapper.

    Provides the ability to send and receive data as a transaction.
    This means that every call to transact consists of a combined
    send and receive step that's atomic from the calling application's
    point of view. Multiple threads and processes can access the device
    node concurrently using one Spicomm instance per thread.
    Transactions are serialized in the underlying kernel driver.
    """

    def __init__(self):
        try:
            self._dev = open(SPICOMM_DEV, 'r+b', 0)
        except (IOError, OSError):
            raise SpicommDevNotFoundError
        self._tbuf = bytearray(HEADER_SIZE + DEFAULT_PAYLOAD_SIZE)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def close(self):
        if self._dev:
            self._dev.close()

    def transact(self, request, timeout=None):
        """Execute a Spicomm transaction.

        The bytes in request are sent, a response is waited for and returned.
        If the request or response is too large SpicommOverflowError is raised.

        Args:
          request: Request bytes to send.
          timeout: How long a response will be waited for, in seconds.

        Returns:
          Bytes-like object with response data.

        Raises:
          SpicommOverflowError: Transaction buffer was too small for response.
                                The 'size' attribute contains the required size.
          SpicommTimeoutError : Transaction timed out.
          SpicommInternalError: Unexpected error interacting with kernel driver.
        """
        payload_len = len(request)
        if payload_len > DEFAULT_PAYLOAD_SIZE:
            buf = bytearray(HEADER_SIZE + payload_len)
        else:
            buf = self._tbuf

        timeout_s = timeout if timeout else _get_timeout(payload_len)

        _fill_buffer(buf, timeout_s, request)

        try:
            # Send transaction to kernel driver.
            fcntl.ioctl(self._dev, SPICOMM_IOCTL_TRANSACT, buf)

            # No exception means errno 0 and buf is now mutated.
            _, _, _, payload_len = struct.unpack('IIII', buf[0:16])
            return buf[16:16 + payload_len]
        except (IOError, OSError):
            # FLAG_ERROR is set if we actually talked to the kernel.
            flags, _, _, payload_len = struct.unpack('IIII', buf[0:16])
            if flags & FLAG_ERROR:
                if flags & FLAG_TIMEOUT:
                    raise SpicommTimeoutError
                elif flags & FLAG_OVERFLOW:
                    raise SpicommOverflowError(payload_len)

            # This is unexpected.
            raise SpicommInternalError
