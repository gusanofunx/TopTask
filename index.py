import tkinter as tk
from tkinter import messagebox
# import    pygetwindow as gw
import pygetwindow as gw  # type: ignore
import pyautogui # type: ignore
from utils.func import show_msg # type: ignore

def show_desktop():
   pyautogui.hotkey('win', 'd')


root = tk.Tk()
screen_width = root.winfo_screenwidth()
root.geometry(f'{screen_width+50}x50+0+0')  # Tamaño para simular una barra de tareas
root.overrideredirect(True)  # Elimina la barra de título
root.configure(bg='#000000')
root.attributes('-alpha', 0.8)
root.attributes('-topmost', True)
# Crea botones o íconos para simular la barra de tareas
button = tk.Button(root, text='Inicio', command=root.quit)
button.pack(side='left',  )
button = tk.Button(root, text='holi', command=show_msg)
button.pack(side='left',  )
# Crear un botón que lleva al escritorio (minimiza todas las ventanas)

desktop_button = tk.Button(root, text="Desktop", command=show_desktop ,
 background='#ec0d0d' , relief='flat' , width=130 ,height=50)
desktop_button.place(x=screen_width-50 ,y=0)
 # Minimizar cada ventana

root.mainloop()