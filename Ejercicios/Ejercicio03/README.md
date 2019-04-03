Para ejecutar el programa es necesario abrir una terminal en el directorio `~/Ejercicio03/src/` donde se debe escribir el siguiente comando

```bash
$ python attack.py archivo llave msj_cifrado
```

Donde el archivo _llave_ es un archivo que contiene exactamente los 16 bytes de la llave k, y _msj_cifrado_ contiene un mensaje cifrado cuyos primeros 16 bytes son el valor IV con el que fue cifrado.