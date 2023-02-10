import time
import serial
import win32api, win32con

arduino = serial.Serial('COM3', 9600, timeout=2)
input("Press Enter to start")
input_full = 1
input_full_diff = 1
def interpret():
        global index_knuckles_proximal
        global index_proximal_middle
        index_knuckles_proximal = 0
        index_proximal_middle = 0
        data = arduino.readline()
        string = data.decode()
        string_stripped = string.strip()
        num = int(string_stripped)
        list_of_digits = [int(i) for i in str(num)]
        index_knuckles_proximal = int(list_of_digits[0])
        index_proximal_middle = int(list_of_digits[1])
        return index_knuckles_proximal
        return index_proximal_middle
def click():
        interpret()
        global input_full
        global input_full_diff
        if(index_proximal_middle != input_full):
                input_full = index_proximal_middle
                if index_proximal_middle == 2:
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        else:
                print("not working 1")
        if(index_knuckles_proximal != input_full_diff):
                input_full_diff = index_knuckles_proximal
                if index_knuckles_proximal == 2:
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        else:
                print("not working 2")
while True:
        click()
