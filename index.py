import tkinter as tk
from tkinter import messagebox
# import    pygetwindow as gw
import pygetwindow as gw  # type: ignore
import pyautogui  # type: ignore
from utils.func import get_window_icon, show_desktop, show_msg  # type: ignore
import win32gui
import win32con
import win32process
import psutil
from PIL import Image, ImageTk

from utils.topTaskBehavior import slide_down, slide_up  # type: ignore

root = tk.Tk()
screen_width = root.winfo_screenwidth()
final_screen = int(screen_width * 0.4)
# root.geometry(f'{final_screen+50}x50+0+0')  # Tamaño para simular una barra de tareas
# Calcular la posición x y y para centrar la ventana
position_x = (screen_width - final_screen) // 2
# position_y = (screen_height - window_height) // 2
# Función para aumentar la altura al hacer hover


def activate_window(hwnd):
    try:
        #   win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Si está minimizada, restaurarla
        # Restaurar la ventana si está minimizada
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)  # Maximizar la ventana
    except Exception as e:
        print(f"Error al activar la ventana: {e}")
# Función para listar las ventanas activas


def listar_aplicaciones_abiertas():
    def enum_windows_callback(hwnd, windows):
        # Solo ventanas visibles con título
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            if psutil.pid_exists(pid):  # Verificar que el proceso exista
                windows.append((hwnd, win32gui.GetWindowText(hwnd)))
        return True

    open_windows = []
    win32gui.EnumWindows(enum_windows_callback, open_windows)

    # Limpiar el contenido del taskbar antes de actualizar
    for widget in taskbar_frame.winfo_children():
        widget.destroy()

    # Mostrar cada ventana abierta en el taskbar
    for hwnd, title in open_windows:
        icon_img = get_window_icon(hwnd)

        if icon_img:
            icon_img = icon_img.resize((40, 40))  # Redimensionar el ícono
            icon_tk = ImageTk.PhotoImage(icon_img)
            app_icon = tk.Label(taskbar_frame, image=icon_tk, bg='lightblue')
            app_icon.image = icon_tk  # Guardar la referencia para evitar que el ícono se destruya
            app_icon.pack(side='right', padx=5)
            app_icon.bind("<Button-1>", lambda event,
                          hwnd=hwnd: activate_window(hwnd))

  

    root.after(2000, listar_aplicaciones_abiertas)


root.geometry(f'{final_screen}x5+{position_x}+{0}')
root.overrideredirect(True)  # Elimina la barra de título
root.configure(bg='#000000')
root.attributes('-alpha', 0.8)
root.attributes('-topmost', True)


def on_taskbar_click(event):
    root.quit()
    # show_desktop()


def show_desktop(event):
    pyautogui.hotkey('win', 'd')


cont_app = tk.Frame(root, bg='#c221eb', width=final_screen)
cont_app.pack(fill='both',)
cont_app.bind("<Button-1>", show_desktop)
button = tk.Button(cont_app, text='Close',
                   background='#fff', command=root.quit)
button.pack(side='left',)


taskbar_frame = tk.Frame(cont_app, bg='#ff47e3', width=final_screen)
taskbar_frame.pack(fill='none',)
taskbar_frame.bind("<Button-1>", on_taskbar_click)

# Crear otro frame que englobe tanto el taskbar como los íconos
taskbar_wrapper = tk.Frame(taskbar_frame, bg='#1c91ff')
taskbar_wrapper.pack(fill='both', expand=True)

# Asociar los eventos de hover a todo el área del taskbar y los íconos
# Cuando el ratón entra en el área visible
taskbar_wrapper.bind('<Enter>', lambda event:  slide_down(
    root, final_screen, position_x))
cont_app.bind('<Leave>', lambda event: slide_up(
    root, final_screen, position_x))
taskbar_frame.bind('<Enter>', lambda event:  slide_down(
    root, final_screen, position_x))
# Crea botones o íconos para simular la barra de tareas


# Crear un botón que lleva al escritorio (minimiza todas las ventanas)
desktop_button = tk.Button(taskbar_frame, text="Desktop", command=show_desktop,
                           background='#ec0d0d', relief='flat', height=50)
desktop_button.pack(side='right', fill='y')
listar_aplicaciones_abiertas()
root.mainloop()

#  pyinstaller --onefile --noconsole index.py
