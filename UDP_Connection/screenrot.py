# import the relevant things
import win32api as win32
import win32con
import time
import os
# define the function to get the screens
def printAllScreen():
    # set i
    i = 0
    # While loop to do the things
    while True:
        # Try except to handle errors
        try:
            # Set the device to be the thing
            device = win32.EnumDisplayDevices(None,i)
            # print the thing
            print("[%d] %s (%s)"%(i,device.DeviceString,device.DeviceName))
            # add to i to iterate
            i = i+1
        # if not then it won't work
        except:
            break
    # return i
    return i
# define the function to rotate the screens
def rotateScreens(x):
    # set the device to be the screen number indicated
    device = win32.EnumDisplayDevices(None, x)
    # prompt that rotating is occuring
    print("Rotate device %s (%s)"%(device.DeviceString,device.DeviceName))
    # set dm to be the current display setting for that screen
    dm = win32.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
    # set the display orientation to be 180 degrees
    dm.DisplayOrientation = win32con.DMDO_180
    # swap the pixels
    dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
    # no clue what this is doing but doing something new based off the display orientation
    dm.Fields = dm.Fields & win32con.DM_DISPLAYORIENTATION
    # does the rotate
    win32.ChangeDisplaySettingsEx(device.DeviceName,dm)
    # sleep a bit 
    time.sleep(2)
    # set the display orientation to be the default setting
    dm.DisplayOrientation = win32con.DMDO_DEFAULT
    # swap the pixels
    dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
    # no clue what this is doing but doing something new based off the display orientation
    dm.Fields = dm.Fields & win32con.DM_DISPLAYORIENTATION
    # does the rotate
    win32.ChangeDisplaySettingsEx(device.DeviceName,dm)
# define the function to rotate each connected screen
def makeItRotate():
    instWin32 = "pip install pypiwin32"
    os.system(instWin32)
    # get the number of screens
    screen_count=printAllScreen()
    # iterate through the screens
    for i in range(0, int(screen_count)):
        # try to rotate
        try:
            rotateScreens(i)
        # if not then pass
        except:
            pass
# call make it rotate
makeItRotate()