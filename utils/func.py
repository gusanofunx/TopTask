
from tkinter import messagebox
import pyautogui  # type: ignore
#
import win32gui
import win32con
import win32process
import psutil
from PIL import Image, ImageTk  # type: ignore
import win32ui

def show_msg():
    messagebox.showinfo('Alert', ' estees un mensaje d e alert')

def show_desktop():
    pyautogui.hotkey('win', 'd')

def get_window_icon(hwnd):
    # Obtener el ícono del window handle (hwnd)
    icon_handle = win32gui.SendMessage(
        hwnd, win32con.WM_GETICON, win32con.ICON_SMALL, 0)
    if icon_handle == 0:
        icon_handle = win32gui.SendMessage(
            hwnd, win32con.WM_GETICON, win32con.ICON_BIG, 0)
    if icon_handle == 0:
        icon_handle = win32gui.GetClassLong(hwnd, win32con.GCL_HICON)

    if icon_handle != 0:
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, 32, 32)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)

        win32gui.DrawIconEx(hdc.GetHandleOutput(), 0, 0,
                            icon_handle, 32, 32, 0, None, win32con.DI_NORMAL)
        bmpinfo = hbmp.GetInfo()
        bmpstr = hbmp.GetBitmapBits(True)
        img = Image.frombuffer(
            'RGBA', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRA', 0, 1)
        return img
    return None
