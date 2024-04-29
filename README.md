**ARQUITECTURA MIPS por Conejos MIPS**

Este proyecto se centra principalmente en la construcción de un procesador iniciando en la
construcción del “Single Datapath” quien será el encargado de que pueda
implementar/decodificar instrucciones básicas tipo R a traves de una interfaz gráfica
que convierte las instrucciones tipo R de lenguaje ensamblador a código binario.


**Cómo pueden comenzar los usuarios con el proyecto.**
* Se recomienda tener al menos un archivo con extensión ".asm" ya generado y ubicado para poder
  utilizarlo (puede estar vacío).
* El archivo ASM deberá estar guardado en la carpeta de proyecto de Verilog con la
  finalidad de que el archivo se encuentre en una ubicación apropiada para el momento de la
  simulación.
* Se debe tener instalado Python para poder ejecutar la interfaz.

- 1.- Abrir y compilar el código en Python
- 2.- Dar click en el botón de "Cargar Archivo ASM"
- 3.- Escribir las instrucciones en ensamblador
  La sintaxis es:
  instrucción $rd $rs $rt

| Instrucción    | Description                |
| :------------- | :------------------------- |
| `add` | Las primeras letras señalan la instrucción y deben estár escritas en minusculas, sin acentos ni caracteres especiales |
| `$1 $2 $3` | Los registros de operandos y destinos deben estar escritos con un número en decimal seguido se un signo de pesos "$"  y separados por un solo espacio entre si |



**Conejos-Mips**
CPU arquitectura MIPS
Equipo 1
Equipo Conejos Mips
Integrantes:
Arturo Daniel Agredano Gutiérrez,
Carlos Eduardo Román Bravo,
Márquez Canizales Cristian,
Alexia Gómez Rubio
