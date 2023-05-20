import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from threading import Thread
from tkinter import *
import os
import shutil
from PIL import Image, ImageTk
#import fnmatch




## FUNCIONES
def readme():
    os.system('start readme.txt')

def salirAplicacion(root):
    valor = messagebox.askquestion("Exit", "¿Deseas salir de la aplicacion?")
    if valor == "yes": root.destroy()



# Archivo de configuración
CONFIG_FILE = 'config.txt'




# Función para guardar la configuración en el archivo de configuración
def save_config():
    global input_dir, output_dir, supply_path, new_name
    with open(CONFIG_FILE, 'w') as f:
        f.write(input_dir + '\n')
        f.write(output_dir + '\n')
        f.write(supply_path + '\n')
        f.write(new_name + '\n')


# Función para cargar la configuración desde el archivo de configuración
def load_config():
    global input_dir, output_dir, supply_path, new_name
    try:
        with open(CONFIG_FILE, 'r') as f:
            input_dir = f.readline().strip()
            output_dir = f.readline().strip()
            supply_path = f.readline().strip()
            new_name = f.readline().strip()
    except:
        pass

# Cambio de nombre de archivo
def switch_name(input_dir, new_name):
    for file_name in os.listdir(input_dir):
        if '_' in file_name:
            halfs = file_name.split('_')
            # Unir la primera parte del nombre con el nuevo nombre y la extensión del archivo
            new_file_name = halfs[0] + '_' + new_name + os.path.splitext(file_name)[1]
            # Renombrar el archivo
            os.rename(os.path.join(input_dir, file_name), 
                      os.path.join(input_dir, new_file_name)) 
            
    messagebox.showinfo("Info", "Cambio de extensión realizado con éxito ")

# Convertir cups de 22 a 20
def quitar_sufijo(input_dir):

    for file_name in os.listdir(input_dir):
        halfs = file_name.split('_')
        if len(halfs) >= 2 and len(halfs[0]) == 22:
            cups = halfs[0]
            new_cups = cups[:-2]
            # Unir la nueva sección del nombre del archivo con el resto del nombre y la extensión del archivo
            new_file_name = new_cups + '_' + '_'.join(halfs[1:])
            # Renombrar el archivo
            os.rename(os.path.join(input_dir, file_name), 
                      os.path.join(input_dir, new_file_name))
    messagebox.showinfo("Info", "Sufijos retirados con éxito ")

# Convertir cups de 20 a 22           
def add_sufijo(input_dir):

    for file_name in os.listdir(input_dir):
        halfs = file_name.split('_')
        if len(halfs[0]) == 20:
            cups = halfs[0]
            gas_cups = ['ES0238', 'ES0210', 'ES0221', 'ES0217', 'ES0229', 'ES0219', 'ES0222', 'ES0234', 'ES0220', 'ES0218', 'ES0236', 'ES0227', 'ES0209', 'ES0224', 'ES0225', 'ES0208', 'ES0201', 'ES0212', 'ES0230', 'ES0205', 'ES0226', 'ES0203', 'ES0215', 'ES0206', 'ES0237', 'ES0204', 'ES0207', 'ES0223', 'ES0242', 'ES0211', 'ES0213', 'ES0202', 'ES0216', 'ES0214']

            if cups[0:6] == 'ES0021':
                new_cups = cups + '1F'
            elif cups[0:6] == 'ES0022':
                new_cups = cups + '1P'
            elif cups[0:5] == 'ES039':
                new_cups = cups + '1P'
            elif cups[0:6] in gas_cups:
                new_cups = cups
            else:
                new_cups = cups + '0F'

            # Unir la nueva sección del nombre del archivo con el resto del nombre y la extensión del archivo
            new_file_name = new_cups + '_' + '_'.join(halfs[1:])
            # Renombrar el archivo
            os.rename(os.path.join(input_dir, file_name), 
                      os.path.join(input_dir, new_file_name))
    messagebox.showinfo("Info", "Sufijos añadidos con éxito ")


# Copia de archivos que aparecen en el documetos de condiciones
def execute_process():
    # Lee la lista de suministros del archivo txt

    if not check_paths():
        return
     
    with open(supply_path) as supply_file: 
        supply = supply_file.read().splitlines() 

    contador = 0
    
    distintos_sup = ""
    
    for file in os.listdir(input_dir):
        if any(sup in file for sup in supply):
            sup = [sup for sup in supply if sup in file][0]  # Obtenemos el sup correspondiente al archivo
            if sup not in distintos_sup:  # Verificamos si el sup ya está en la lista
                distintos_sup += sup + '\n'  # Agregamos el sup a la lista
                           
            contador += 1
            shutil.move(os.path.join(input_dir, file), output_dir)


    if contador == 1:
        messagebox.showinfo("Proceso realizado con éxito ", "Se ha copiado " + str(contador) + " archivo exitosamente, correspodiente al siguiente punto de suministro:\n\n" + str(distintos_sup))
    else:
        messagebox.showinfo("Proceso realizado con éxito ", "Se han copiado " + str(contador) + " archivos exitosamente, correspodientes a los siguientes puntos de suministro:\n\n" + str(distintos_sup))
       


# INTERFAZ


class Inicio(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Inicio")
        self.master.geometry("300x320")
        self.master.configure(bg="#F5F5F5")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', background='#E0E0E0', font=('Arial', 12), foreground='#333333', relief='raised')
        self.style.map('TButton', background=[('active', '#ff6200')])
        self.create_widgets()

    def create_widgets(self):
        header_frame = tk.Frame(self.master, bg="#00404d")
        header_frame.pack(side='top', fill='x', pady=10)
        header_label = tk.Label(header_frame, text="INICIO", font=('Arial', 16, "bold"), bg="#00404d", fg="#FFFFFF")
        header_label.pack()

        button_frame = tk.Frame(self.master, bg="#F5F5F5")
        button_frame.pack(expand=True, pady=20)
            
        # Alinear los botones verticalmenteyoitu
        button_principal = ttk.Button(button_frame, text="Búsqueda de ficheros", command=self.buscar_ficheros, style="Custom.TButton")
        button_principal.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.X)
        button_secundaria = ttk.Button(button_frame, text="Modificación de nombres", command=self.modificar_nombres, style="Custom.TButton")
        button_secundaria.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.X)
        button_otro = ttk.Button(button_frame, text="Ajuste nº caracteres CUPS", command=self.ajuste_CUPS, style="Custom.TButton")
        button_otro.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.X)


        footer_frame = tk.Frame(self.master, bg="#E0E0E0")
        footer_frame.pack(side='bottom', fill='x')
        status_label = tk.Label(footer_frame, text="Consulte la opción 'Ayuda' en el menú para más información.", font=('Arial', 7), bg="#E0E0E0", fg="#333333")
        status_label.pack(fill='x', padx=10, pady=5)
        
        
    def buscar_ficheros(self):
        self.master.destroy() # Cerrar la ventana actual
        GUI_ficheros() # Abrir la interfaz principal
    
    def modificar_nombres(self):
        self.master.destroy() # Cerrar la ventana actual
        GUI_nombres() # Abrir la interfaz de cambio de nombres
        
    
    def ajuste_CUPS(self):
        self.master.destroy() # Cerrar la ventana actual
        GUI_cups() # Abrir la interfaz principal
        pass
        

class GUI_cups(tk.Frame):

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ajuste CUPS")

        # Cargar la configuración
        load_config()
        
        
        # Configuración de la ventana principal
        self.root.geometry("690x480")
        self.root.resizable(False, False)
        self.root.config(bg="#F5F5F5")
        
        # Imágenes
        
        img_folder = Image.open('logo.jpg')
        img_folder = img_folder.resize((22, 22), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.img_folder = ImageTk.PhotoImage(img_folder)

        # Icono

        icon = Image.open("repsol.jpg")
        icon = icon.resize((118, 86), Image.ANTIALIAS) # Redimensiona el icono a 15x15 píxeles
        self.icon = ImageTk.PhotoImage(icon)
        icon_label = tk.Label(self.root, image=self.icon, bg="#F5F5F5")
        icon_label.grid(column=0, row=11, padx=20, pady=10, sticky="sw")

        back_icon = Image.open("back.png")
        back_icon = back_icon.resize((92, 51), Image.ANTIALIAS) 
        self.back_icon = ImageTk.PhotoImage(back_icon)

        
        # Título principal
        title_label = tk.Label(self.root, text="Ajuste de CUPS", font=("Arial", 16, "bold"), bg="#F5F5F5")
        title_label.grid(column=0, row=0, columnspan=2, padx=20, pady=20)
        
        # Labels y botones para directorios y archivo condicional
        input_label = tk.Label(self.root, text="Directorio de entrada:", font=("Arial", 12), bg="#F5F5F5")
        input_label.grid(column=0, row=1, padx=20, pady=10, sticky="w")
        
        self.text_box_input = tk.Entry(self.root, width=85, font=("Arial", 10))
        self.text_box_input.grid(column=0, row=2, padx=20, sticky="w")
        self.text_box_input.insert(0, input_dir)
        
        input_button = tk.Button(self.root, command=self.select_input_dir, image=self.img_folder, bg="#FFFFFF")
        input_button.grid(column=1, row=2, padx=0, sticky="w")

        # Botón para ejecutar proceso
        execute_button1 = tk.Button(self.root, text="Quitar sufijos", font=("Arial", 12, "bold"), bg="#4CAF50", fg="#FFFFFF", command=lambda: quitar_sufijo(input_dir), width=25, pady=10)
        execute_button1.grid(column=0, row=5, columnspan=2, padx=20, pady=20)

        execute_button2 = tk.Button(self.root, text="Añadir sufijos", font=("Arial", 12, "bold"), bg="#4CAF50", fg="#FFFFFF", command=lambda: add_sufijo(input_dir), width=25, pady=10)
        execute_button2.grid(column=0, row=8, columnspan=2, padx=20, pady=20)

        # Botón para ir a Inicio
        back_button = tk.Button(self.root, image=self.back_icon, bg="#F5F5F5", command=self.ir_a_inicio, width=30, height=30)
        back_button.grid(column=0, row=0, padx=20, pady=20, sticky="nw")

    def ir_a_inicio(self):
        self.root.destroy()  # Cerrar la ventana actual
        #Inicio(tk.Tk())
        main() # Abrir la ventana de Inicio
        


    def select_input_dir(self):
        global input_dir
        input_dir = filedialog.askdirectory()
        
        self.text_box_input.delete(0, tk.END)
        self.text_box_input.insert(0, input_dir)
        save_config()

    

class GUI_nombres(tk.Frame):

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cambio de nombres")

        # Cargar la configuración
        load_config()
        #new_name = 'SOLICITUD'
        
        # Configuración de la ventana principal
        self.root.geometry("690x480")
        self.root.resizable(False, False)
        self.root.config(bg="#F5F5F5")
        
        # Imágenes
        
        img_folder = Image.open('logo.jpg')
        img_folder = img_folder.resize((22, 22), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.img_folder = ImageTk.PhotoImage(img_folder)
        
        img_file = Image.open('save2.jpg')
        img_file = img_file.resize((22, 22), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.img_file = ImageTk.PhotoImage(img_file)

        # Icono

        icon = Image.open("repsol.jpg")
        icon = icon.resize((118, 86), Image.ANTIALIAS) 
        self.icon = ImageTk.PhotoImage(icon)
        icon_label = tk.Label(self.root, image=self.icon, bg="#F5F5F5")
        icon_label.grid(column=0, row=11, padx=20, pady=10, sticky="sw")

        back_icon = Image.open("back.png")
        back_icon = back_icon.resize((92, 51), Image.ANTIALIAS) 
        self.back_icon = ImageTk.PhotoImage(back_icon)
        #back_icon_label = tk.Label(self.root, image=self.back_icon, bg="#F5F5F5")
        #back_icon_label.grid(column=0, row=11, padx=20, pady=10, sticky="sw")
        
        
        # Título principal
        title_label = tk.Label(self.root, text="Cambio de extensión", font=("Arial", 16, "bold"), bg="#F5F5F5")
        title_label.grid(column=0, row=0, columnspan=2, padx=20, pady=20)
        
        # Labels y botones para directorios y archivo condicional
        input_label = tk.Label(self.root, text="Directorio de entrada:", font=("Arial", 12), bg="#F5F5F5")
        input_label.grid(column=0, row=1, padx=20, pady=10, sticky="w")
        
        self.text_box_input = tk.Entry(self.root, width=85, font=("Arial", 10))
        self.text_box_input.grid(column=0, row=2, padx=20, sticky="w")
        self.text_box_input.insert(0, input_dir)
        
        input_button = tk.Button(self.root, command=self.select_input_dir, image=self.img_folder, bg="#FFFFFF")
        input_button.grid(column=1, row=2, padx=0, sticky="w")
        
        name_label = tk.Label(self.root, text="Extensión nueva:", font=("Arial", 12), bg="#F5F5F5")
        name_label.grid(column=0, row=5, padx=20, pady=10, sticky="w")
        
        self.text_box_name = tk.Entry(self.root, width=85, font=("Arial", 10))
        self.text_box_name.grid(column=0, row=6, padx=20, sticky="w")
        self.text_box_name.insert(0, new_name)
        
        name_button = tk.Button(self.root, command=self.select_new_name, image=self.img_file, bg="#FFFFFF")
        name_button.grid(column=1, row=6, padx=0, sticky="w")

        # Botón para ejecutar proceso
        execute_button1 = tk.Button(self.root, text="Ejecutar", font=("Arial", 12, "bold"), bg="#4CAF50", fg="#FFFFFF", command=lambda: switch_name(input_dir, new_name), width=25, pady=10)
        execute_button1.grid(column=0, row=7, columnspan=2, padx=20, pady=20)

        # Botón para ir a Inicio
        back_button = tk.Button(self.root, image=self.back_icon, bg="#F5F5F5", command=self.ir_a_inicio, width=30, height=30)
        back_button.grid(column=0, row=0, padx=20, pady=20, sticky="nw")


    def ir_a_inicio(self):
        self.root.destroy()  # Cerrar la ventana actual
        main()  # Abrir la ventana de Inicio
        

    def select_input_dir(self):
        global input_dir
        input_dir = filedialog.askdirectory()
        
        self.text_box_input.delete(0, tk.END)
        self.text_box_input.insert(0, input_dir)
        save_config()

    def select_new_name(self):
        global new_name
        new_name = self.text_box_name.get()
        
        self.text_box_name.delete(0, tk.END)
        self.text_box_name.insert(0, new_name)
        save_config()
        



class GUI_ficheros(tk.Frame):
        
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Demo solución")

        # Cargar la configuración
        load_config()
        
        # Configuración de la ventana principal
        self.root.geometry("690x480")
        self.root.resizable(False, False)
        self.root.config(bg="#F5F5F5")
        
        # Imágenes
        
        img_folder = Image.open('logo.jpg')
        img_folder = img_folder.resize((22, 22), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.img_folder = ImageTk.PhotoImage(img_folder)
        
        img_file = Image.open('txt.jpg')
        img_file = img_file.resize((22, 22), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.img_file = ImageTk.PhotoImage(img_file)

        # Icono

        icon = Image.open("repsol.jpg")
        icon = icon.resize((118, 86), Image.ANTIALIAS) # Redimensiona el icono a 15x15 píxeles
        self.icon = ImageTk.PhotoImage(icon)
        icon_label = tk.Label(self.root, image=self.icon, bg="#F5F5F5")
        icon_label.grid(column=0, row=11, padx=20, pady=10, sticky="sw")

        back_icon = Image.open("back.png")
        back_icon = back_icon.resize((92, 51), Image.ANTIALIAS) 
        self.back_icon = ImageTk.PhotoImage(back_icon)
        
        # Título principal
        title_label = tk.Label(self.root, text="Búsqueda de ficheros", font=("Arial", 16, "bold"), bg="#F5F5F5")
        title_label.grid(column=0, row=0, columnspan=2, padx=20, pady=20)
        
        # Labels y botones para directorios y archivo condicional
        input_label = tk.Label(self.root, text="Directorio de entrada:", font=("Arial", 12), bg="#F5F5F5")
        input_label.grid(column=0, row=1, padx=20, pady=10, sticky="w")
        
        self.text_box_input = tk.Entry(self.root, width=85, font=("Arial", 10))
        self.text_box_input.grid(column=0, row=2, padx=20, sticky="w")
        self.text_box_input.insert(0, input_dir)
        
        input_button = tk.Button(self.root, command=self.select_input_dir, image=self.img_folder, bg="#FFFFFF")
        input_button.grid(column=1, row=2, padx=0, sticky="w")
        
        output_label = tk.Label(self.root, text="Directorio de salida:", font=("Arial", 12), bg="#F5F5F5")
        output_label.grid(column=0, row=3, padx=20, pady=10, sticky="w")
        
        self.text_box_output = tk.Entry(self.root, width=85, font=("Arial", 10))
        self.text_box_output.grid(column=0, row=4, padx=20, sticky="w")
        self.text_box_output.insert(0, output_dir)
        
        output_button = tk.Button(self.root, command=self.select_output_dir, image=self.img_folder, bg="#FFFFFF")
        output_button.grid(column=1, row=4, padx=0, sticky="w")
        
        supply_label = tk.Label(self.root, text="Puntos de suministro:", font=("Arial", 12), bg="#F5F5F5")
        supply_label.grid(column=0, row=5, padx=20, pady=10, sticky="w")
        
        self.text_box_supply = tk.Entry(self.root, width=85, font=("Arial", 10))
        self.text_box_supply.grid(column=0, row=6, padx=20, sticky="w")
        self.text_box_supply.insert(0, supply_path)
        
        supply_button = tk.Button(self.root, command=self.select_supply_path, image=self.img_file, bg="#FFFFFF")
        supply_button.grid(column=1, row=6, padx=0, sticky="w")
        
        # Botón para ejecutar proceso
        execute_button = tk.Button(self.root, text="Ejecutar", font=("Arial", 12, "bold"), bg="#4CAF50", fg="#FFFFFF", command=execute_process, width=25, pady=10)
        execute_button.grid(column=0, row=7, columnspan=2, padx=20, pady=20)

        # Botón para ir a Inicio
        back_button = tk.Button(self.root, image=self.back_icon, bg="#F5F5F5", command=self.ir_a_inicio, width=30, height=30)
        back_button.grid(column=0, row=0, padx=20, pady=20, sticky="nw")

    def ir_a_inicio(self):
        self.root.destroy()  # Cerrar la ventana actual
        main()  # Abrir la ventana de Inicio
        


    # Funciones para seleccionar los directorios y archivo de suministros
            
    def select_input_dir(self):
        global input_dir
        input_dir = filedialog.askdirectory()
        
        self.text_box_input.delete(0, tk.END)
        self.text_box_input.insert(0, input_dir)
        save_config()
    
    
    def select_output_dir(self):
        global output_dir
        output_dir = filedialog.askdirectory()
        
        self.text_box_output.delete(0, tk.END)
        self.text_box_output.insert(0, output_dir)
        save_config()
        
        
    def select_supply_path(self):
        global supply_path
        supply_path = filedialog.askopenfilename(title = "Selecciona el archivo de suministros", filetypes = [("Archivos de texto", "*.txt")])

        self.text_box_supply.delete(0, tk.END)
        self.text_box_supply.insert(0, supply_path)
        save_config()
        
    

def check_paths():
        if input_dir == output_dir:
            messagebox.showerror("Error", "La ruta de entrada y salida no puede ser la misma")
            return False
        return True   



def main():

    config_file = 'config.txt'

    input_dir = ''
    output_dir = ''
    supply_path = ''
    

    if os.path.isfile(config_file):
        with open(config_file, 'r') as f:
            lines = f.readlines()
            if len(lines) >= 1:
                input_dir = lines[0].strip()
            if len(lines) >= 2:
                output_dir = lines[1].strip()
            if len(lines) >= 3:
                supply_path = lines[2].strip()

    root = Tk()
    app = Inicio(root)
    root.resizable(0, 0)
    #root.configure(bg='#4B4B4B') PERMITE PONER EL COLOR DE FONDO DE LA VENTANA

    # Guardar rutas seleccionadas en el archivo de configuración después de seleccionarlas
    #def save_config():
        #with open(config_file, 'w') as f:
            #f.write(f"{app.input_dir}\n")
            #f.write(f"{app.output_dir}\n")
            #f.write(f"{app.supply_path}\n")
    #app.input_dir_button.config(command=lambda: app.do_run_select_input_dir(save_config))
    #app.output_dir_button.config(command=lambda: app.do_run_select_output_dir(save_config))
    #app.supply_path_button.config(command=lambda: app.do_run_select_supply_path(save_config))
    
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Ayuda", command=readme)
    filemenu.add_command(label="Salir", command=lambda: salirAplicacion(root))
    menubar.add_cascade(label="Menu", menu=filemenu)
    root.config(menu=menubar)

    root.mainloop()
        

    root.mainloop()
    
if __name__ == '__main__':
    main()
