import tkinter as tk
from tkinter import messagebox
# import    pygetwindow as gw
import pygetwindow as gw  # type: ignore
import pyautogui # type: ignore
from utils.func import show_desktop, show_msg # type: ignore

root = tk.Tk()
screen_width = root.winfo_screenwidth()
final_screen = int(screen_width * 0.3)
# root.geometry(f'{final_screen+50}x50+0+0')  # Tamaño para simular una barra de tareas
# Calcular la posición x y y para centrar la ventana
position_x = (screen_width - final_screen) // 2
# position_y = (screen_height - window_height) // 2

# Función para aumentar la altura al hacer hover
def slide_down(event):
    root.geometry(f'{final_screen}x50+{position_x}+0')  # Cambia la altura a 50

# Función para reducir la altura cuando se quite el hover
def slide_up(event):
    root.geometry(f'{final_screen}x50+{position_x}+{-45}')  # Cambia la altura a 5


root.geometry(f'{final_screen}x5+{position_x}+0')

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
 background='#ec0d0d' , relief='flat' ,)
desktop_button.pack(side='right')
# desktop_button.place(x=screen_width-50 ,y=0)
 # Minimizar cada ventana

# Crear un Frame inferior que actúa como el "padding bottom"
padding_frame = tk.Frame(root, height=10, width=2, bg='gray')
padding_frame.pack(  side='bottom')
# Asociar los eventos de hover
root.bind('<Enter>', slide_down)  # Cuando el ratón entra en la ventana
root.bind('<Leave>',slide_up) 

root.mainloop()