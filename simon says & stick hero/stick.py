from ppadb.client import Client
import numpy
import time
from mss import mss
import math
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]


sct = mss()
def auto():

    start_x, start_y = 1360, 920
    screen_x = { 'left': start_x, 'top': start_y, 'width': 500, 'height': 1 }
    screen_pixel = numpy.array(sct.grab(screen_x))
    cur_pix = 1360
    first = True
    initial_x, next_x = 0,2
    for pixels in screen_pixel:
        for pixel in pixels:
            if pixel[1]<=10 and first:
                first = False
                initial_x = cur_pix + 30
            if pixel[1]<=10 and not(first) and cur_pix>initial_x+20:
                next_x = cur_pix
                break
            cur_pix += 1


    screen_y = { 'left': next_x, 'top': 450, 'width': 1, 'height': 400 }
    screen_pixel = numpy.array(sct.grab(screen_y))

    next_y = 450
    for pixels in screen_pixel:
        for pixel in pixels:
            if pixel[1]<15:
                break
            next_y += 1
    #print('next', next_x, next_y)

    screen_y = { 'left': initial_x-24, 'top': 450, 'width': 1, 'height': 400 }
    screen_pixel = numpy.array(sct.grab(screen_y))
    initial_y = 450
    for pixels in screen_pixel:
        for pixel in pixels:
            if pixel[1]<20:
                break
            initial_y += 1
    print('ini',initial_x, initial_y)

    def cor_dis(x1,y1,x2,y2):
        xs = (x1-x2)**2
        ys = (y1-y2)**2
        return int(math.sqrt(xs+ys))

    radius = cor_dis(initial_x, initial_y, next_x, next_y)
    if initial_y>next_y:
        radius = next_x-initial_x
        #print("taking x dis")
    print('rad', radius)
    touch_x, touch_y = initial_x+5, initial_y-radius+30
    return (touch_x, touch_y)

while True:
    time.sleep(.1)
    cor = auto()
    final_cor = { 'left': cor[0], 'top': cor[1], 'width': 1, 'height': 1 }
    final_pixel = numpy.array(sct.grab(final_cor))
    cor_chek = { 'left': cor[0], 'top': cor[1]-20, 'width': 1, 'height': 1 }
    chek_pixel = numpy.array(sct.grab(cor_chek))
    if final_pixel[0][0][1]<12 and chek_pixel[0][0][1]:
        print('hit')
        click(1400, 300)
        print('done')
        time.sleep(2)






