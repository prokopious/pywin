import time
import win32gui
import uiautomation as auto

_active_window_name = None

while True:
    time.sleep(4)
    window = win32gui.GetForegroundWindow()
    chromeControl = auto.ControlFromHandle(window)
    edit = chromeControl.EditControl()

    #print(dir(chromeControl.EditControl()))
    print(edit.GetValuePattern().Value)

    time.sleep(5)

