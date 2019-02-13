# -*- coding: utf-8 -*-

from collections import Counter

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Calcula el porcentaje de frecuencias que aparece el caracter especificado.
def frecuencias(text):
    length = len(text)
    counter = Counter(list(text))
    for char in counter:
        average = (counter[char] / length) * 100
        print('El porcentaje que aparece la '+char+' es '+repr(average)+'%')

# Calcula el decimado de acuerdo al bloque de desplazamiento especificado.
# Al menos debe de valer 1.
def bloque(t, mensaje):
    if(t <= 0):
        print('Debes introducir un número mayor a 0.');
    else:
        longitud = len(mensaje)
        print(mensaje[0:longitud:t])

frecuencias(alphabet)

bloque(0, alphabet)
bloque(1, alphabet)
bloque(2, alphabet)
bloque(3, alphabet)
bloque(4, alphabet)
bloque(5, alphabet)
