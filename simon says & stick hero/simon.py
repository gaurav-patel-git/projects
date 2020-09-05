from ppadb.client import Client
import numpy
import time
from mss import mss

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

device.shell('input tap 400 650')

time.sleep(.5)

g = { 'left': 1510, 'top': 301, 'width': 1, 'height': 1 }
y = { 'left': 1510, 'top': 730, 'width': 1, 'height': 1 }
r = { 'left': 1790, 'top': 311, 'width': 1, 'height': 1 }
b = { 'left': 1790, 'top': 811, 'width': 1, 'height': 1 }

sct = mss()

def detect_next():
    detecting = False

    while True:
        green_pixel = numpy.array(sct.grab(g))
        yellow_pixel = numpy.array(sct.grab(y))
        red_pixel = numpy.array(sct.grab(r))
        blue_pixel = numpy.array(sct.grab(b))
        ri,gi,bi = 2,1,0
        green_b = green_pixel[0][0][bi]
        yellow_b = yellow_pixel[0][0][bi]
        red_g = red_pixel[0][0][gi]
        blue_r = blue_pixel[0][0][ri]
        if not detecting and \
            green_b < 10 and \
            yellow_b < 100 and \
            red_g < 70 and \
            blue_r < 50:
            detecting = True

        if not detecting:
            continue

        if 10 <= green_b:
            return 'g'
        if 100 <= yellow_b:
            return 'y'
        if 70 <= red_g:
            return 'r'
        if 50 <= blue_r:
            return 'b'

moves = 1
colors = []

while True:
    for i in range(moves):
        color = detect_next()
        print(f'detected {color}')

        colors.append(color)

    print(colors)

    time.sleep(1)

    for color in colors:
        if color == 'g':
            device.shell('input tap 150 300')
        if color == 'y':
            device.shell('input tap 150 800')
        if color == 'r':
            device.shell('input tap 600 300')
        if color == 'b':
            device.shell('input tap 600 800')

    moves += 1
    colors = []
