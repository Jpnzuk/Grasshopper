import time
import serial
import win32api
import win32con
from pynput.keyboard import Key, Controller
from scan import PressKey, ReleaseKey, W, A, S, D

arduino = serial.Serial('COM3', 9600, timeout=2)
input("Press Enter to start")
last_value = 1
last_value2 = 1
last_value3 = 1
last_value4 = 1
last_value5 = 1


def interpret():
    global index_knuckles_proximal
    global index_proximal_middle
    global touch_index
    global touch_middle
    global touch_ring
    index_knuckles_proximal = 0
    index_proximal_middle = 0
    touch_index = 0
    touch_middle = 0
    touch_ring = 0
    data = arduino.readline()
    string = data.decode()
    string_stripped = string.strip()
    num = int(string_stripped)
    list_of_digits = [int(i) for i in str(num)]
    index_knuckles_proximal = int(list_of_digits[0])
    index_proximal_middle = int(list_of_digits[1])
    touch_index = int(list_of_digits[2])
    touch_middle = int(list_of_digits[3])
    touch_ring = int(list_of_digits[4])
    return index_knuckles_proximal
    return index_proximal_middle
    return touch_index
    return touch_middle
    return touch_ring


def auto():
    global last_value
    global last_value2
    global last_value3
    global last_value4
    global last_value5
    global keyboard
    interpret()
    if (index_proximal_middle == 2):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        last_value = index_proximal_middle
    if last_value != index_proximal_middle:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        last_value = index_proximal_middle

    if (index_knuckles_proximal == 2):
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        last_value2 = index_knuckles_proximal
    if last_value2 != index_knuckles_proximal:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        last_value2 = index_knuckles_proximal

    if (touch_index == 2):
        PressKey(D)
        last_value3 = touch_index
    if last_value3 != touch_index:
        last_value3 = touch_index
        ReleaseKey(D)

    if (touch_middle == 2):
        PressKey(W)
        last_value4 = touch_middle
    if last_value4 != touch_middle:
        last_value4 = touch_middle
        ReleaseKey(W)

    if (touch_ring == 2):
        PressKey(A)
        last_value5 = touch_ring
    if last_value5 != touch_ring:
        last_value5 = touch_ring
        ReleaseKey(A)


while True:
    auto()
