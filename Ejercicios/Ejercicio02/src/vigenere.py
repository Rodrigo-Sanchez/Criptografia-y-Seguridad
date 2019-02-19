# -*- coding: utf-8 -*-

from collections import Counter, OrderedDict
import sys

# alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Calcula el porcentaje de frecuencias que aparece el caracter especificado.
def frequency(text):
    length = len(text)
    counter = OrderedDict(Counter(list(text)).most_common())
    freqList = []
    for char in counter:
        average = counter[char]/length
        freqList.append(average)
        # Imprimimos el porcentaje que aparece cada letra.
        # Hacemos un cast de average de float a string.
        # print('El porcentaje que aparece la '+char+' es '+repr(average*100)+'%')
    # print(freqList)
    return freqList

# Calcula el decimado de acuerdo al bloque de desplazamiento especificado.
# Al menos debe de valer 1.
def block(t, message):
    if(t <= 0):
        print('Debes introducir un número mayor a 0.');
    else:
        longitud = len(message)
        # print(message[0:longitud:t])
        return message[0:longitud:t]

# Función que calcula la I 
def I(list):
    I = 0
    for i in list:
        I += i**2
    # print(I)
    return I

# Abrimos el archivo especificado en la terminal con permisos de lectura.
with open(sys.argv[1], 'r') as f:
    # Guardamos en una variable su contenido.
    cypher = f.read()
    # Quitamos cualquier otro caracter que no sea alfabético.
    cypherClean = ''.join(filter(str.isalpha, cypher))

# print(cypherClean[:49])

# print(frequency(cypherClean))

# block(0, cypherClean) # Caso de error.
# block(1, cypherClean) # Devuelve la misma entrada.
# frequency(block(2, cypherClean))
# frequency(block(3, cypherClean))
# frequency(block(4, cypherClean))
# frequency(block(5, cypherClean))

for n in range(1, len(cypherClean)):
    print(frequency(block(n, cypherClean)))
    if(I(frequency(block(n, cypherClean))) >= 0.0741):
        q = frequency(block(n, cypherClean))
        print(q)
        break

letterFreq = {'E':13,'A':11.1,'O':9.7,'S':7.98,'R':6.87,'N':6.71,'I':6.25,'D':5.86,'L':4.97,
              'C':4.68,'T':4.63,'U':3.93,'M':3.15,'P':2.51,'B':1.42,'G':1.01,'V':0.9,'Y':0.9,
              'Q':0.88,'H':0.7,'F':0.69,'Z':0.52,'J':0.44,'Ñ':0.31,'X':0.22,'K':0.02,'W':0.01}
p = {0:13,1:11.1,2:9.7,3:8.2,4:8,5:7.7,6:6.9,7:5.3,8:5.2,
     9:4.5,10:3.6,11:3.6,12:3,13:2.9,14:1.4,15:1.3,16:1,17:0.8,
     18:0.7,19:0.6,20:0.6,21:0.3,22:0.3,23:0.2,24:0.1,25:0,26:0}
# letterFrequency = ['E','A','O','S','R','N','I','D','L','C','T','U','M','P','B','G','V','Y','Q','H','F','Z','J','Ñ','X','K','W']

# print(q)

Ik = 0
for k in range(26):
    for i in range(26):
        # print("i:" + repr(i) +" k:" + repr(k))
        # print(q[(i+k)%23])
        Ik += (p[i] * q[(i+k)% 25])
        if(Ik >= 0.0741):
            print('hola: '+repr(Ik))
            Ik =0
            break        

print(Ik)
    # for i in range(1, 28):
    #     Ik = pi * 1
    # if(Ik >= 0.0741):
    #     break
        # print(p[n])
