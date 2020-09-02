# Manual de usuario SimpleQL

SimpleQL es un lenguaje de consultas con funcionalidad en consola, con este podremos cargar archivos .json y poder desde realizar consultas hasta generar reportes.

Al ingresar al programa le pedira ingresar un comando, estos se enlistan a continuacion.
Los comandos se escriben uno por uno y se pulsa enter para que se ejecuten.


## Comandos

A continuación se explicara el uso de los comandos permitios, estos pueden ir en mayúsculas o minúsculas.
Por Ejemplo: **Seleccionar**  =  **SELECCIONAR** = **seleccionar**

### Cargar

Con este podremos cargar cualquier cantidad de  archivos a memoria escribiendo el nombre del archivo separado por comas.
```
Cargar Prueba1.json, Prueba2.json
```
 

### Seleccionar

Con este podremos imprimir los datos que coincidan con algún parámetro que le especifiquemos. 
Por Ejemplo:
```
Seleccionar nombre, edad Donde nombre = "registro 3"
Seleccionar activo, promedio Donde edad = 55 
SELECCIONAR nombre, promedio DONDE activo = True
SELECCIONAR * DONDE promedio = 56.456
seleccionar edad
seleccionar *
```
**Con el \* seleccionamos todos los atributos.**

### Máximo y mínimo
Estos comandos tienen nos permiten encontrar el valor máximo y mínimo de los atributos edad y promedio de todos los registros en memoria.
Por Ejemplo:
```
MINIMO edad
MAXIMO promedio
```

### Suma

Al igual que los anteriores con este sumamos todos los atributos ya sea de edad o del promedio.
```
SUMA edad
SUMA promedio
```
### Cuenta

Este únicamente cuenta el total de registros en memoria.
```
Cuenta
```
### Reportar N
Este nos genera un reporte en formato HTML que se abrirá en el navegador por defecto. Tendremos que ingresar el numero de registros que queramos.
```
- Reportar 3
```
Por Ejemplo:

![Reporte](https://lh3.googleusercontent.com/3RM0lmGkfLfcHbNPh-73wlZ9qFZA7BVmDmsrgVIq5gBDa6ls1gXaS1Jy-nIJhjbw1KLeo17lo7vkvg1tvt9c6nQrmhhiaJqIifDyiTiHw8pbut0EKRTTDIjW1WWKCcQqZmMA6okb=w2400)

![Reporte](https://lh3.googleusercontent.com/6863CwswCuRtWgnOhtpRiDSHvb-UjkUowx2XuKDf67IHmMp8ECGthpe145aOOJgt0iX-tfkGOT89Z9ToTeH4gikP9Z7pIJYUGg5_L613pkSXor7cxhBIwlQL9iVeYP0Vd7Z6PpsR=w2400)
