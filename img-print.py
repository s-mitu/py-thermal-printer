#!/usr/local/bin/python2
# coding:utf-8

import printer
from PIL import Image
import sys
port = "/dev/cuaU0"
#brate = 115200
brate = 38400
#brate = 19200

if len(sys.argv) > 1:
    imagefile = sys.argv[1]
    if len(sys.argv) > 2:
        port = sys.argv[2]
    if len(sys.argv) > 3:
        brate = int(sys.argv[3])
else:
    print("File name ")
    exit(1)

p = printer.ThermalPrinter(serialport=port, baudrate=brate)
i = Image.open(imagefile)
data = list(i.getdata())
w, h = i.size
p.print_bitmap(data, w, h)

p.linefeed(3)
