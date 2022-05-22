from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController
import serial
keyboard = Controller()
mouse = MouseController()
ser = serial.Serial('/dev/ttyACM0', 9600)
mouseMode = False
while True:
    try:
        data = ser.readline().decode('utf-8')
    except UnicodeDecodeError:
        continue
    if not mouseMode:
        if "S" in data:
            if data[1:][:-2] == "0":
                keyboard.press(Key.space)
            else:
                keyboard.release(Key.space)
        if "X" in data:
            x = int(data[1:][:-2])
            if x > 1000:
                keyboard.press(Key.up)
            else:
                keyboard.release(Key.up)
            if x < 23:
                keyboard.press(Key.down)
            else:
                keyboard.release(Key.down)
        if "Y" in data:
            y = int(data[1:][:-2])
            if y > 1000:
                keyboard.press(Key.right)
            else:
                keyboard.release(Key.right)
            if y < 23:
                keyboard.press(Key.left)
            else:
                keyboard.release(Key.left)
    if mouseMode:
        if "X" in data:
            x = int(data[1:][:-2])
            if x > 1000:
                mouse.move(0, -1)
            else:
                mouse.move(0, 1)
            if x < 23:
                mouse.move(0, 1)
            else:
                mouse.move(0, -1)
        if "Y" in data:
            y = int(data[1:][:-2])
            if y > 1000:
                mouse.move(1, 0)
            else:
                mouse.move(-1, 0)
            if y < 23:
                mouse.move(-1, 0)
            else:
                mouse.move(1, 0)
        if "S" in data:
            if data[1:][:-2] == "0":
                mouse.press(Button.left)
            else:
                mouse.release(Button.left)
    if "K" in data:
        if data[1:][:-2] == "0":
            mouseMode = False
    if "M" in data:
        if data[1:][:-2] == "0":
            mouseMode = True
    if "E" in data:
        if data[1:][:-2] == "0":
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
