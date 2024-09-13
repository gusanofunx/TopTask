import tkinter as tk
# import    pygetwindow as gw
import pygetwindow as gw  # type: ignore
import pyautogui

def show_desktop():
   pyautogui.hotkey('win', 'd')

root = tk.Tk()
root.geometry('1920x40+0+0')  # Tamaño para simular una barra de tareas
root.overrideredirect(True)  # Elimina la barra de título
root.configure(bg='#000000')
root.attributes('-alpha', 0.8)
root.attributes('-topmost', True)
# Crea botones o íconos para simular la barra de tareas
button = tk.Button(root, text='Inicio', command=root.quit)
button.pack(side='left',  )
# Crear un botón que lleva al escritorio (minimiza todas las ventanas)

desktop_button = tk.Button(root, text="Desktop", command=show_desktop)
desktop_button.pack(side='left' )
 # Minimizar cada ventana

root.mainloop()