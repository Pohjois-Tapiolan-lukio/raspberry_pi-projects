# Copyright 2017 Jussi Roos
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR 
# PERFORMANCE OF THIS SOFTWARE.

'''
Module is supposed to be used with Rasperry Pi Sense HAT module and Sens HAT python module.  
Converts intiger to pixel array.
'''


def intToPixels(num, fg_color, bg_color):
    '''
    num = your number (int)  
    fg_color = foreground color [R, G, B]
    bg_color = background color [R, G, B]
    '''
    pixels_empty = [
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_00 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_01 = [
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_02 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_03 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_04 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_05 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_06 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_07 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_08 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_09 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]

    # 10+
    pixels_10 = [
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_11 = [
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_12 = [
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_13 = [
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_14 = [
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_15 = [
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_16 = [
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_17 = [
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_18 = [
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_19 = [
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]

    # 20+
    pixels_20 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_21 = [
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_22 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_23 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_24 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_25 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_26 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_27 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_28 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_29 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]

    # 30+
    pixels_30 = [
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_31 = [
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_32 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_33 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_34 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_35 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_36 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_37 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_38 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_39 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]

    # 40+
    pixels_40 = [
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_41 = [
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_42 = [
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_43 = [
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_44 = [
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_45 = [
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_46 = [
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_47 = [
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_48 = [
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_49 = [
    fg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]

    # 50+
    pixels_50 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_51 = [
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]

    pixels_52 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_53 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_54 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_55 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_56 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_57 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_58 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_59 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]

    # 60+
    pixels_60 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_61 = [
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_62 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_63 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_64 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_65 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_66 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_67 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_68 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_69 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, bg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]

    # 70+
    pixels_70 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_71 = [
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_72 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_73 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_74 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_75 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_76 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_77 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_78 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_79 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]

    # 80+
    pixels_80 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_81 = [
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_82 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_83 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_84 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_85 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_86 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_87 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_88 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_89 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]

    # 90+
    pixels_90 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_91 = [
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_92 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_93 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_94 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_95 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_96 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, bg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_97 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_98 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]
    pixels_99 = [
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    fg_color, bg_color, fg_color, bg_color, fg_color, bg_color, fg_color, bg_color,
    fg_color, fg_color, fg_color, bg_color, fg_color, fg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, fg_color, bg_color, bg_color, bg_color, fg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color,
    bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color, bg_color
    ]

    # If statements 
    if num == 0:
        return pixels_00
    elif num == 1:
        return pixels_01
    elif num == 2:
        return pixels_02
    elif num == 3:
        return pixels_03
    elif num == 4:
        return pixels_04
    elif num == 5:
        return pixels_05
    elif num == 6:
        return pixels_06
    elif num == 7:
        return pixels_07
    elif num == 8:
        return pixels_08
    elif num == 9:
        return pixels_09
    elif num == 10:
        return pixels_10
    elif num == 11:
        return pixels_11
    elif num == 12:
        return pixels_12
    elif num == 13:
        return pixels_13
    elif num == 14:
        return pixels_14
    elif num == 15:
        return pixels_15
    elif num == 16:
        return pixels_16
    elif num == 17:
        return pixels_17
    elif num == 18:
        return pixels_18
    elif num == 19:
        return pixels_19
    elif num == 20:
        return pixels_20
    elif num == 21:
        return pixels_21
    elif num == 22:
        return pixels_22
    elif num == 23:
        return pixels_23
    elif num == 24:
        return pixels_24
    elif num == 25:
        return pixels_25
    elif num == 26:
        return pixels_26
    elif num == 27:
        return pixels_27
    elif num == 28:
        return pixels_28
    elif num == 29:
        return pixels_29
    elif num == 30:
        return pixels_30
    elif num == 31:
        return pixels_31
    elif num == 32:
        return pixels_32
    elif num == 33:
        return pixels_33
    elif num == 34:
        return pixels_34
    elif num == 35:
        return pixels_35
    elif num == 36:
        return pixels_36
    elif num == 37:
        return pixels_37
    elif num == 38:
        return pixels_38
    elif num == 39:
        return pixels_39
    elif num == 40:
        return pixels_40
    elif num == 41:
        return pixels_41
    elif num == 42:
        return pixels_42
    elif num == 43:
        return pixels_43
    elif num == 44:
        return pixels_44
    elif num == 45:
        return pixels_45
    elif num == 46:
        return pixels_46
    elif num == 47:
        return pixels_47
    elif num == 48:
        return pixels_48
    elif num == 49:
        return pixels_49
    elif num == 50:
        return pixels_50
    elif num == 51:
        return pixels_51
    elif num == 52:
        return pixels_52
    elif num == 53:
        return pixels_53
    elif num == 54:
        return pixels_54
    elif num == 55:
        return pixels_55
    elif num == 56:
        return pixels_56
    elif num == 57:
        return pixels_57
    elif num == 58:
        return pixels_58
    elif num == 59:
        return pixels_59
    elif num == 60:
        return pixels_60
    elif num == 61:
        return pixels_61
    elif num == 62:
        return pixels_62
    elif num == 63:
        return pixels_63
    elif num == 64:
        return pixels_64
    elif num == 65:
        return pixels_65
    elif num == 66:
        return pixels_66
    elif num == 67:
        return pixels_67
    elif num == 68:
        return pixels_68
    elif num == 69:
        return pixels_69
    elif num == 70:
        return pixels_70
    elif num == 71:
        return pixels_71
    elif num == 72:
        return pixels_72
    elif num == 73:
        return pixels_73
    elif num == 74:
        return pixels_74
    elif num == 75:
        return pixels_75
    elif num == 76:
        return pixels_76
    elif num == 77:
        return pixels_77
    elif num == 78:
        return pixels_78
    elif num == 79:
        return pixels_79
    elif num == 80:
        return pixels_80
    elif num == 81:
        return pixels_81
    elif num == 82:
        return pixels_82
    elif num == 83:
        return pixels_83
    elif num == 84:
        return pixels_84
    elif num == 85:
        return pixels_85
    elif num == 86:
        return pixels_86
    elif num == 87:
        return pixels_87
    elif num == 88:
        return pixels_88
    elif num == 89:
        return pixels_89
    elif num == 90:
        return pixels_90
    elif num == 91:
        return pixels_91
    elif num == 92:
        return pixels_92
    elif num == 93:
        return pixels_93
    elif num == 94:
        return pixels_94
    elif num == 95:
        return pixels_95
    elif num == 96:
        return pixels_96
    elif num == 97:
        return pixels_97
    elif num == 98:
        return pixels_98
    elif num == 99:
        return pixels_99
    else:
        return pixels_empty
