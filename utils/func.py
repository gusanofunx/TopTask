
from tkinter import messagebox
import pyautogui # type: ignore

def show_msg():
   messagebox.showinfo('Alert' , ' estees un mensaje d e alert')

def show_desktop():
   pyautogui.hotkey('win', 'd')