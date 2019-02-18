# -*- coding: utf-8 -*-

from collections import Counter
import sys

# alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Calcula el porcentaje de frecuencias que aparece el caracter especificado.
def frecuencias(text):
    length = len(text)
    counter = Counter(list(text))
    freqList = {}
    for char in counter:
        average = counter[char]/length
        freqList[char] = average
        # Imprimimos el porcentaje que aparece cada letra.
        # Hacemos un cast de average de float a string.
        print('El porcentaje que aparece la '+char+' es '+repr(average*100)+'%')
    # print(freqList)
    I = 0
    for i in freqList.keys():
        I += freqList[i] ** 2
        # print("Got key", i, "which maps to value", freqList[i])
    print(I)
    return I


# Calcula el decimado de acuerdo al bloque de desplazamiento especificado.
# Al menos debe de valer 1.
def bloque(t, message):
    if(t <= 0):
        print('Debes introducir un número mayor a 0.');
    else:
        longitud = len(message)
        print(message[0:longitud:t])
        return message[0:longitud:t]

# def I():

# Abrimos el archivo especificado en la terminal con permisos de lectura.
with open(sys.argv[1], 'r') as f:
    # Guardamos en una variable su contenido.
    cypher = f.read()
    # Quitamos cualquier otro caracter que no sea alfabético.
    cypherClean = ''.join(filter(str.isalpha, cypher))

# print(cypherClean[:49])

frecuencias(cypherClean)

# bloque(0, cypherClean) # Caso de error.
# bloque(1, cypherClean) # Devuelve la misma entrada.
# frecuencias(bloque(2, cypherClean))
# frecuencias(bloque(3, cypherClean))
# frecuencias(bloque(4, cypherClean))
# frecuencias(bloque(5, cypherClean))

for n in range(1,len(cypherClean)):
    if(frecuencias(bloque(n, cypherClean)) >= 0.0741):
        break