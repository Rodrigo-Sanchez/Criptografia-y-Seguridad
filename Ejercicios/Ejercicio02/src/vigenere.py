# -*- coding: utf-8 -*-

from collections import Counter
import sys

# alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Calcula el porcentaje de frecuencias que aparece el caracter especificado.
def frequency(text):
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
    return freqList

# Calcula el decimado de acuerdo al bloque de desplazamiento especificado.
# Al menos debe de valer 1.
def block(t, message):
    if(t <= 0):
        print('Debes introducir un número mayor a 0.');
    else:
        longitud = len(message)
        print(message[0:longitud:t])
        return message[0:longitud:t]

# Función que calcula la I 
def I(list):
    I = 0
    for i in list.keys():
        I += list[i] ** 2
        # print("Got key", i, "which maps to value", freqList[i])
    # print(I)
    return I

# Abrimos el archivo especificado en la terminal con permisos de lectura.
with open(sys.argv[1], 'r') as f:
    # Guardamos en una variable su contenido.
    cypher = f.read()
    # Quitamos cualquier otro caracter que no sea alfabético.
    cypherClean = ''.join(filter(str.isalpha, cypher))

# print(cypherClean[:49])

print(frequency(cypherClean))

# block(0, cypherClean) # Caso de error.
# block(1, cypherClean) # Devuelve la misma entrada.
# frequency(block(2, cypherClean))
# frequency(block(3, cypherClean))
# frequency(block(4, cypherClean))
# frequency(block(5, cypherClean))

for n in range(1, len(cypherClean)):
    if(I(frequency(block(n, cypherClean))) >= 0.0741):
        break

letterFreq = {'E':13.68,'A':12.53,'O':8.68,'S':7.98,'R':6.87,'N':6.71,'I':6.25,'D':5.86,'L':4.97,
              'C':4.68,'T':4.63,'U':3.93,'M':3.15,'P':2.51,'B':1.42,'G':1.01,'V':0.9,'Y':0.9,
              'Q':0.88,'H':0.7,'F':0.69,'Z':0.52,'J':0.44,'Ñ':0.31,'X':0.22,'K':0.02,'W':0.01}
letterFreq2 = {0:13.68,1:12.53,2:8.68,3:7.98,4:6.87,5:6.71,6:6.25,7:5.86,8:4.97,
              9:4.68,10:4.63,11:3.93,12:3.15,13:2.51,14:1.42,15:1.01,16:0.9,17:0.9,
              18:0.88,19:0.7,20:0.69,21:0.52,22:0.44,23:0.31,24:0.22,25:0.02,26:0.01}
# letterFrequency = ['E','A','O','S','R','N','I','D','L','C','T','U','M','P','B','G','V','Y','Q','H','F','Z','J','Ñ','X','K','W']

# qi = 

Ik = 0
pi = 0
for k in range(27):
    for i in range(1, 27):
        pi = letterFreq2[i]
    for i in range(1, 28):
        Ik = pi * 1
    if(Ik >= 0.0741):
        break
        # print(letterFreq2[n])