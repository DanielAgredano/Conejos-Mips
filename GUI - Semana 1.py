import tkinter as tk
from tkinter import filedialog
import os

filepath = ""

instructions ={ #Instrucciones codificadas {<instrucción> : [<tipo>,<func>]}
    "add"   : ["R","100000"],
    "sub"   : ["R","100010"],
    "and"   : ["R","100100"],
    "or"    : ["R","100101"],
    "nor"   : ["R","100111"],
    "slt"   : ["R","101010"]
}

def filepath_data(path):
    global filepath # Modifica la variable global
    filepath = path.removesuffix("asm") #Le quita la extensión
    return filepath #Retorna el nuevo valor por si lo necesita otra función

def cargar_archivo_asm():
    filepath = filedialog.askopenfilename(filetypes=[("Archivos ASM", "*.asm")]) #Solicita un archivo al usuario
    if filepath: #Verifica si el usuario dió un archivo
        filepath = filepath_data(filepath) #Guarda la dirección sinextensión
        with open(filepath+"asm", "r") as file: #Abre el archivo de ensamblador
            contenido_text.delete("1.0", tk.END) # Limpia contenido anterior
            contenido_text.insert(tk.END, file.read()) # Muestra contenido en el Text
        if(os.path.exists(filepath+"txt")): #Verifica que el txt exista
            with open(filepath+"txt", "r") as file: #Abre el txt
                bin_text.delete("1.0", tk.END)  # Limpia contenido anterior
                bin_text.insert(tk.END, file.read()) # Muestra contenido en el Text

def guardar_cambios():
    with open(filepath+"asm", "w") as asm_file: #Abre el archivo de ensamblador
        asm_file.write(contenido_text.get("1.0", tk.END).removesuffix("\n")) #Sobreescribe el archivo

def IntStr_Bin(cadena, ancho):
    return (format(int(cadena),'b')).zfill(ancho) #Convierte un enteo dado como cadena a un binario de longitud especificada

def instruccion_R(line): #Arma el formato de la instrucción
    ins = ""
    ins += "000000" #Op code
    ins += IntStr_Bin(line[2],5) #rs
    ins += IntStr_Bin(line[3],5) #rt
    ins += IntStr_Bin(line[1],5) #rd
    ins += "00000" #Shamt
    ins += instructions[line[0]][1] #Funct
    ins += "\n"
    return ins

def convertir_archivo():
    text = contenido_text.get("1.0", tk.END) #Lee el contenido del cuadro de texto
    text = text.replace("$","") #Quita los '$'
    words = [line.split(" ") for line in text.splitlines()] #Separa el texto en lineas y palabras (arreglo bidimensional)

    binary = ""

    for line in words: #Revisa cada línea
        if line[0] in instructions: #Si la primera palabra corresponde a una instrucción válida
            if instructions[line[0]][0]=="R": #Checa si es de tipo R (en el diccionario biene especificado)
                binary += instruccion_R(line) #Arma la línea y la agrega al texto resultado

    binary = binary.removesuffix("\n") #Quita el último salto de línea
    with open(filepath+"txt", "w") as txt_file: #Abre/crea el archivo txt
        txt_file.write(binary) #Escribe el texto resultado
        bin_text.delete("1.0", tk.END) # Limpia contenido anterior
        bin_text.insert(tk.END, binary) # Muestra contenido en el Text


root = tk.Tk() #Inicializa la ventana
root.title("Editor y Convertidor de Archivos ASM") #Le da un título a la ventana
#Etiqueta
label1 = tk.Label(root, text="ASM")
label1.pack()
#Cuadro de texto (ASM)
contenido_text = tk.Text(root, wrap=tk.WORD, height=15, width=80)
contenido_text.pack(padx=10, pady=5)

#Etiqueta
label2 = tk.Label(root, text="TXT")
label2.pack(padx=1, pady=1)
#Cuadro de texto (TXT)
bin_text = tk.Text(root, wrap=tk.WORD, height=15, width=80)
bin_text.pack()

#Botón para abrir archivo asm
cargar_asm_button = tk.Button(root, text="Cargar Archivo ASM", command=cargar_archivo_asm)
cargar_asm_button.pack(pady=5)

#Botón para guardar cambios en el archivo asm
modificar_button = tk.Button(root, text="Guardar Cambios", command=guardar_cambios)
modificar_button.pack(pady=5)

#Botón para convertir el asm a binario, guardar el archivo y mostrarlo en la ventana
guardar_button = tk.Button(root, text="Convertir Archivo", command=convertir_archivo)
guardar_button.pack(pady=5)

root.mainloop()
