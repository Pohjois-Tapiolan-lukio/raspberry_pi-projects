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
#
#
# Version 0.1
#
# Use "sudo apt-get install sense-hat" To instal Sense Hat Module
# Use CTRL+C To exit the program

from sense_hat import SenseHat 

sense = SenseHat()

# Main loop to do the job!
def main():
    print("Press CTRL+C To Exit")
    while True:  
        temp = sense.get_humidity()
        msg = "{0:.1f}%".format(temp)
        print("Relative humidity: {0}".format(msg))
        sense.show_message(msg, scroll_speed=.1, text_colour=[255, 0, 0]) # Message to display, Text speed (Bigger number is slower), Text Color (RGB)

# try/except function to detect keyboard iterrupts so we can shut the code down properly 
try:
    main()
except KeyboardInterrupt:
    print("\n----------------------------------------")
    print("Keyboard Interrupt! Exitting!")
    sense.clear()
