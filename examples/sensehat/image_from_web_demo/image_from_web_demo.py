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
# Requires sense_hat, PIL and urllib.request modeules to work
# 
# Use "sudo apt-get install sense-hat" To instal Sense Hat Module

from sense_hat import SenseHat 
from PIL import Image
import urllib.request


sense = SenseHat()


def main():
    continueRunnig = True

    newIMG()

    while continueRunnig:
        toDo = input('''Type "n" for new picture or type "c" to clear screen and exit or type "e" to exit \n''')
        if toDo == "n":
            newIMG()
        elif toDo == "c":
            exitClear()
            continueRunnig = False
        elif toDo == "e":
            continueRunnig = False


def newIMG():
    url = input("URL adress to image (.jpg or .png)?\n")
    img = getImage(url)
    img = processImage(img, url)
    displayImage(img)

def detectType(url):
    splitUrl = url.split(".")
    last = len(splitUrl)
    print(splitUrl[last-1])
    return splitUrl[last-1]
    
    

def getImage(url):
    imgL = urllib.request.urlopen(url)
    return imgL

def processImage(imgLoaded, typeUrl):
    img = Image.open(imgLoaded) 
    new_width  = 8
    new_height = 8
    img = img.resize((new_width, new_height))
    l = []

    imgType = detectType(typeUrl) 

    if imgType == "jpg":
        for y in range(0, 8):
            for x in range(0, 8):
                r, g, b = img.getpixel((x,y))
                l.append([r, g, b])
    elif imgType == "jpeg":
        for y in range(0, 8):
            for x in range(0, 8):
                r, g, b = img.getpixel((x,y))
                l.append([r, g, b])
    elif imgType == "png":
        for y in range(0, 8):
            for x in range(0, 8):
                r, g, b, a = img.getpixel((x,y))
                l.append([r, g, b])

    return l

def displayImage(imgList):
    sense.set_pixels(imgList)


def exitClear():
    sense.clear()

main()
