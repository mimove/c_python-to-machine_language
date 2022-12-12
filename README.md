# NOTAS SOBRE LENGUAJE ALTO NIVEL Y LENGUAJE MÁQUINA

En este directorio, tenemos un programa escrito en C que calcula los numeros de la serie de Fibonacci, y un conversor del binario que escribe el compilador gcc a código máquina. Para entender las diferentes instrucción del código máquina se puede consultar el siguiente [enlace](<https://www.geeksforgeeks.org/machine-instructions/>). Para entender más en profundidad estos conceptos, se puede utilizar este [pdf](./x64_cheatsheet.pdf).

La forma de utilizar el código de este repositorio es:

1. Compilar el programa en C usando:

```sh
make
```

2. Una vez compilados todos los ejecutables con diferentes niveles de optimización, se ejecuta el script ```c2machine.sh``` que crea los archivos .txt con el código en ensamblador utilizando la herramienta ```otool```.

