import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

instructions ={ #Instrucciones codificadas {<instrucción> : [<tipo>,<func>]}
    #Instrucciones R
    "add"   : ["R","100000"],
    "sub"   : ["R","100010"],
    "and"   : ["R","100100"],
    "or"    : ["R","100101"],
    "nor"   : ["R","100111"],
    "slt"   : ["R","101010"],
    "nop"   : ["R","000000"],
    #Instrucciones I
    #Aritméticas
    "addi"  : ["I","001000"],
    "subi"  : ["I","000000"],#No encontrado
    "andi"  : ["I","001100"],
    "ori"   : ["I","001101"],
    "nori"  : ["I","000000"],#No encontrado
    "slti"  : ["I","001010"],
    #Memoria
    "lw"    : ["I","100011"],
    "sw"    : ["I","101011"],
    #Ramificación
    "beq"   : ["I","000100"],
    "bne"   : ["I","000101"],
    "bgtz"  : ["I","000111"],
    #Instrucciones J
    "j"     : ["J","000010"]
}

class MainWindow:
    def __init__(self):
        self.path = ""
        self.estatus = True
        self.error = ""

        self.root = tk.Tk() #Inicializa la ventana
        self.root.title("Editor y Convertidor de Archivos ASM") #Le da un título a la ventana

        #Divisiones
        self.fTexts = ttk.Frame(self.root, width=80)
        self.fASM = ttk.Frame(self.fTexts)
        self.fBIN = ttk.Frame(self.fTexts)
        self.fLog = ttk.Frame(self.root)
        self.fButtons = ttk.Frame(self.root)
        #Elementos
        self.label_path = tk.Label(self.root, text="Carpeta:")
        self.label_log = tk.Label(self.fLog, text="Estado:")
        self.label_mensajes = tk.Label(self.fLog, text="Bienvenido", borderwidth=1, relief="solid")
        self.label1 = tk.Label(self.fASM, text="ASM")
        self.asm_text = tk.Text(self.fASM, wrap=tk.WORD, width=30)
        self.label2 = tk.Label(self.fBIN, text="TXT")
        self.bin_text = tk.Text(self.fBIN, wrap=tk.WORD, width=30)
        self.cargar_asm_button = tk.Button(self.fButtons, text="Seleccionar carpeta", command=self.cargar_archivo_asm)
        self.modificar_button = tk.Button(self.fButtons, text="Guardar Cambios", command=self.guardar_cambios)
        self.guardar_button = tk.Button(self.fButtons, text="Convertir Archivo", command=self.convertir_archivo)
        self.memoria_button = tk.Button(self.fButtons, text="Precargar memorias", command=self.crear_ventana)
        #Acomodo
        self.label_path.pack(fill="x")
        self.fTexts.pack(fill="y")
        self.fASM.pack(side=tk.LEFT)
        self.fBIN.pack(side=tk.LEFT)
        self.fLog.pack(fill="x")
        self.fButtons.pack(fill="x")

        self.label1.pack(padx=1, pady=1)
        self.asm_text.pack(padx=2, pady=5, expand=True)
        self.label2.pack(padx=2, pady=1)
        self.bin_text.pack(padx=1, pady=5, expand=True)
        self.label_log.pack(padx=5, pady=5, side=tk.LEFT)
        self.label_mensajes.pack(padx=5, pady=5, side=tk.LEFT, expand=True, fill='x')
        self.cargar_asm_button.pack(padx=5, pady=5, side=tk.LEFT, expand=True)
        self.modificar_button.pack(padx=5, pady=5, side=tk.LEFT, expand=True)
        self.guardar_button.pack(padx=5, pady=5, side=tk.LEFT, expand=True)
        self.memoria_button.pack(padx=5, pady=5, side=tk.LEFT, expand=True)

        self.root.mainloop()

    def cargar_archivo_asm(self):
        path = filedialog.askdirectory() #Solicita una carpeta al usuario
        if path: #Verifica si el usuario dió una carpeta
            message="Carpeta seleccionada" #Mensaje que se mostrará
            self.path = path #Actualiza la carpeta actual

            self.label_path.configure(text="Carpeta:  "+self.path) #Muestra el directorio
            self.bin_text.delete("1.0", tk.END) #Limpia contenido anterior
            self.asm_text.delete("1.0", tk.END) #Limpia contenido anterior

            if(os.path.exists(path+"/INS1.asm")): #Verifica que el ASM exista
                with open(path+"/INS1.asm", "r") as file: #Abre el archivo de ensamblador
                    message += ", ASM cargado" #Agrega al mensaje que el ASM se cargó
                    self.asm_text.insert(tk.END, file.read()) #Muestra contenido en el Text

            if(os.path.exists(path+"/INS1.txt")): #Verifica que el TXT exista
                with open(path+"/INS1.txt", "r") as file: #Abre el TXT
                    message += ", TXT cargado" #Agrega al mensaje que el TXT se cargó
                    self.bin_text.insert(tk.END, file.read()) #Muestra contenido en el Text

            self.label_mensajes.config(text=message) #Muestra el mensaje

    def guardar_cambios(self):
        self.label_mensajes.config(text="Cambios guardados") #Muestra el mensaje
        with open(self.path+"/INS1.asm", "w") as asm_file: #Abre el archivo de ensamblador
            asm_file.write(self.asm_text.get("1.0", tk.END).removesuffix("\n")) #Sobreescribe el archivo

    def crear_ventana(self):
        self.label_mensajes.config(text="Abriendo memorias") #Muestra el mensaje
        MemWindow(self.path) #Crea una nueva ventana para editar las memorias

    def IntStr_Bin(self, cadena, ancho):
        cadena = cadena.replace("$","") #Quita los '$'
        num = int(cadena) #Convierte a entero
        fill = '1' if num<0 else '0' #selecciona el caracter con el que se rellebará la cadena (0 positivo/1 negativo)
        num = (pow(2,ancho)+num) if num<0 else num #Le hace complemento A2 al número
        return (format(num,'b')).rjust(ancho,fill) #Convierte un entero dado como cadena a un binario de longitud especificada

    def splitLines(self, string, n):
        return '\n'.join([(string[i:i+n]) for i in range(0, len(string), n)]) #Pone saltos de línea cada 8 caracteres

    def instruccion_R(self, line): #Arma el formato R
        ins = ""
        ins += "000000" #Op code
        ins += self.IntStr_Bin(line[2],5) #rs
        ins += self.IntStr_Bin(line[3],5) #rt
        ins += self.IntStr_Bin(line[1],5) #rd
        ins += "00000" #Shamt
        ins += instructions[line[0]][1] #Funct
        return self.splitLines(ins,8) #Secciona la instrucción en 4 partes

    def instruccion_I(self, line): #Arma el formato I
        ins = ""
        ins += instructions[line[0]][1] #Opcode
        ins += self.IntStr_Bin(line[2],5) #rs
        ins += self.IntStr_Bin(line[1],5) #rt
        ins += self.IntStr_Bin(line[3],16) #Inmediato
        return self.splitLines(ins,8) #Secciona la instrucción en 4 partes

    def instruccion_J(self, line): #Arma el formato J
        ins = ""
        ins += instructions[line[0]][1] #Opcode
        ins += self.IntStr_Bin(line[1],26) #Dirección
        return self.splitLines(ins,8) #Secciona la instrucción en 4 partes
    
    def linea_valida(self, linea):
        tipo = instructions[linea[0]][0] #Guarda el tipo de instrucción para evaluarla
        if tipo == "R": #Si es de tipo R
            if len(linea)<4: #Verifica que la cantidad de operandos sea correcta
                self.error = "Faltan operandos"
                return False
            for i in range(1,4): #Para cada operando
                if linea[i][0] != '$': #Verifica si tiene el '$'
                    self.error = "Se esperaba una direccion"
                    return False
        if tipo == "I": #Si es de tipo I
            if len(linea)<4: #Verifica que la cantidad de operandos sea correcta
                self.error = "Faltan operandos"
                return False
            for i in range(1,3): #Para los primeros 2 operandos
                if linea[i][0] != '$': #Verifica si tiene el '$'
                    self.error = "Se esperaba una direccion"
                    return False
            if linea[3][0] == '$': #Para el último operando verifica que no tenga '$'
                self.error = "Se esperaba un valor inmediato"
                return False
        if tipo == "J": #Si es de tipo J
            if len(linea)<2: #Verifica que la cantidad de operandos sea correcta
                self.error = "Faltan operandos"
                return False
            if linea[1][0] == '$': #Para el único operando verifica que no tenga '$'
                self.error = "Se esperaba un valor inmediato"
                return False
        return True

    def procesar_instrucciones(self, words):
        binary = []

        for n,line in enumerate(words): #Revisa cada línea y le asigna un número
            if line[0] in instructions: #Si la primera palabra corresponde a una instrucción válida
                if(not self.linea_valida(line)): #Si se encontró un error se cancela el proceso
                    return "Error en linea "+str(n)+": "+self.error
                if instructions[line[0]][0]=="R": #Checa si es de tipo R (en el diccionario biene especificado)
                    binary.append(self.instruccion_R(line)) #Arma la línea y la agrega al texto resultado
                if instructions[line[0]][0]=="I": #Checa si es de tipo I (en el diccionario biene especificado)
                    binary.append(self.instruccion_I(line)) #Arma la línea y la agrega al texto resultado
                if instructions[line[0]][0]=="J": #Checa si es de tipo J (en el diccionario biene especificado)
                    binary.append(self.instruccion_J(line)) #Arma la línea y la agrega al texto resultado
            else: #Si es una insrucción inválida
                return "Error en linea "+str(n)+": Instruccion no valida"

        return binary

    def convertir_archivo(self):
        text = self.asm_text.get("1.0", tk.END) #Lee el contenido del cuadro de texto
        words = [line.split(" ") for line in text.splitlines()] #Separa el texto en lineas y palabras (arreglo bidimensional)

        binary = self.procesar_instrucciones(words) #Procesa las instrucciones

        if(type(binary)==str): #Si llegó un error en lugar de la conversión
            self.label_mensajes.config(text=binary) #Se muestra el error
            return
        self.label_mensajes.config(text="Convertido sin errores") #Se muestra un mensaje de completado

        binary = '\n'.join(binary) #Recibe las instrucciones procesadas y las une con saltos de linea

        with open(self.path+"/INS1.txt", "w") as txt_file: #Abre/crea el archivo txt
            txt_file.write(binary) #Escribe el texto resultado
            self.bin_text.delete("1.0", tk.END) #Limpia contenido anterior
            self.bin_text.insert(tk.END, binary) #Muestra contenido en el Text


class MemWindow:
    def __init__(self, path):
        self.path = path #Recibe el directorio seleccionado

        self.memories = tk.Toplevel() #Inicializa la ventana
        self.memories.title("Editor de memorias") #Le da un título a la ventana
        #Divisiones
        self.fTexts = ttk.Frame(self.memories, width=80)
        self.fASM = ttk.Frame(self.fTexts)
        self.fBIN = ttk.Frame(self.fTexts)
        self.fButtons = ttk.Frame(self.memories)
        #Elementos
        self.label3 = tk.Label(self.fASM, text="Banco de memoria")
        self.bm_text = tk.Text(self.fASM, wrap=tk.WORD, width=32, height=32)
        self.label4 = tk.Label(self.fBIN, text="Memoria")
        self.m_text = tk.Text(self.fBIN, wrap=tk.WORD, width=32, height=32)
        self.cargar_bm_button = tk.Button(self.fButtons, text="Abrir banco", command=lambda: self.cargar_memoria("BR1.txt",self.bm_text))
        self.guardar_bm_button = tk.Button(self.fButtons, text="Cargar banco", command=lambda: self.escribir_memoria("BR1.txt",self.bm_text))
        self.cargar_m_button = tk.Button(self.fButtons, text="Abrir memoria", command=lambda: self.cargar_memoria("MEM1.txt",self.m_text))
        self.guardar_m_button = tk.Button(self.fButtons, text="Cargar memoria", command=lambda: self.escribir_memoria("MEM1.txt",self.m_text))
        #Acomodo
        self.fTexts.pack(fill="y")
        self.fASM.pack(side=tk.LEFT)
        self.fBIN.pack(side=tk.LEFT)
        self.fButtons.pack(fill="x")
        self.label3.pack(padx=1, pady=1)
        self.bm_text.pack(padx=2, pady=5, expand=True)
        self.label4.pack(padx=2, pady=1)
        self.m_text.pack(padx=1, pady=5, expand=True)
        self.cargar_bm_button.pack(padx=5, pady=5, side=tk.LEFT, expand=True)
        self.guardar_bm_button.pack(padx=5, pady=5, side=tk.LEFT, expand=True)
        self.cargar_m_button.pack(padx=5, pady=5, side=tk.LEFT, expand=True)
        self.guardar_m_button.pack(padx=5, pady=5, side=tk.LEFT, expand=True)

        self.cargar_memoria("BR1.txt",self.bm_text) #Muestra el banco de registros
        self.cargar_memoria("MEM1.txt",self.m_text) #Muestra la memoria

    def cargar_memoria(self, archivo, texto):
        texto.delete("1.0", tk.END) #Limpia contenido anterior
        if(os.path.exists(self.path+"/"+archivo)): #Verifica que el archivo exista
            with open(self.path+"/"+archivo, "r") as file: #Abre el archivo
                texto.insert(tk.END, file.read()) # Muestra contenido en el Text

    def escribir_memoria(self, archivo, texto):
        with open(self.path+"/"+archivo, "w") as asm_file: #Abre/crea el archivo
            asm_file.write(texto.get("1.0", tk.END).removesuffix("\n")) #Sobreescribe el archivo

MainWindow()