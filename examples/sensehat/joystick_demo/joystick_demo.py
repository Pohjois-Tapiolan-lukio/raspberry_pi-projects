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
# Use "sudo apt-get install sense-hat" To instal Sense Hat Modeule
# Use CTRL+C To exit the program


from sense_hat import SenseHat 


sense = SenseHat()

def main():
    x = 0
    y = 7

    print("Press CTRL+C To Exit")
    print("----------------------------------------")

    while True:
        event = sense.stick.wait_for_event()
        if event.direction == "right" and event.action != "released":   # Detect that joystick was moved right.
            x, y = go_right(x, y)
            draw_pixel(x, y)
        elif event.direction == "left" and event.action != "released":   # Detect that joystick was moved left.
            x, y = go_left(x, y)
            draw_pixel(x, y)
        elif event.direction == "up" and event.action != "released":   # Detect that joystick was moved up.
            x, y = go_up(x, y)
            draw_pixel(x, y)
        elif event.direction == "down" and event.action != "released":   # Detect that joystick was moved down.
            x, y = go_down(x, y)
            draw_pixel(x, y)


def go_down(x, y):  # Function to move the pixel coordinates down.
    if y < 7 and y >= 0:
        print("Move down at y: {0}".format(y))
        y += 1
    else:
        print("Border at y: {0}".format(y))
    return x, y


def go_up(x, y):  # Function to move the pixel coordinates up.
    if y <= 7 and y > 0:
        print("Move up at y: {0}".format(y))
        y -= 1
    else:
        print("Border at y: {0}".format(y))
    return x, y


def go_right(x, y):  # Function to move the pixel coordinates right.
    if x < 7 and x >= 0:
        print("Move right at x: {0}".format(x))
        x += 1
    else:
        print("Border at x: {0}".format(x))
    return x, y


def go_left(x, y):   # Function to move the pixel coordinates left.
    if x <= 7 and x > 0:
        print("Move left at x: {0}".format(x))
        x -= 1
    else:
        print("Border at x: {0}".format(x))
    return x, y


def draw_pixel(x, y):   # Function to draw the new frame
    sense.clear()
    sense.set_pixel(x, y, 255, 0, 0)

# try/except function to detect keyboard iterrupts so we can shut the code down properly 
try:
    main()
except KeyboardInterrupt:
    print("\n----------------------------------------")
    print("Keyboard Interrupt! Exitting!")
    sense.clear()