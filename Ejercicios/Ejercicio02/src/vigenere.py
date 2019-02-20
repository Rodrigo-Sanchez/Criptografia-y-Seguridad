# -*- coding: utf-8 -*-

from collections import Counter, OrderedDict
import sys

alpha = Counter({'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'Ñ':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26})

# Calcula el porcentaje de frecuencias que aparece el caracter especificado.
def frequency(text):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    length = len(text)
    lettersList = list(text)
    sortedList = sorted(lettersList)
    counter = Counter(sortedList)
    freqList = []

    for char in counter:
        average = counter[char]/length
        freqList.append(average)

        alphabet = "".join([x for x in alphabet if x is not char])
        # Imprimimos el porcentaje que aparece cada letra.
        # Hacemos un cast de average de float a string.
        print('El porcentaje que aparece la '+char+' es '+repr(average*100)+'%')
    
    # Convertimos la cadena a una lista.
    missingLettersList = list(alphabet)

    # Agregamos al resultado las letras faltantes.x
    for char in missingLettersList:
        freqList.insert(alpha[char], 0)

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
    for i in list:
        I += i**2
    # print("El valor de I es: "+repr(I))
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
    if(I(frequency(block(n, cypherClean))) >= 0.0741):
        # Obtiene las frecuenciasde  las letras en el texto.
        bloc = block(n, cypherClean)
        q = frequency(bloc)
        # print("Las frecuencias qi en el texto B son: " + repr(q))
        break

p = {0:0.1253,1:0.0142,2:0.0468,3:0.0586,4:0.1386,5:0.0069,6:0.0101,7:0.007,8:0.0625,9:0.0044,10:0.0002,11:0.0497,12:0.0315,13:0.0671,14:0.0031,15:0.0868,16:0.0251,17:0.0088,18:0.0687,19:0.0798,20:0.0463,21:0.0393,22:0.009,23:0.0001,24:0.0022,25:0.009,26:0.0052}

# p = {0:13,1:11.1,2:9.7,3:8.2,4:8,5:7.7,6:6.9,7:5.3,8:5.2,
#     9:4.5,10:3.6,11:3.6,12:3,13:2.9,14:1.4,15:1.3,16:1,17:0.8,
#     18:0.7,19:0.6,20:0.6,21:0.3,22:0.3,23:0.2,24:0.1,25:0,26:0}

for k in range(27):
    Ik = 0
    for i in range(27):
        # print("p " + repr(i) + " " + repr(p[i]))
        # print("q " + repr(i+k) + " " + repr(q[(i+k)%27]))
        # print("p*q " +repr(p[i] * q[(i+k)%27]))
        Ik += (p[i] * q[(i+k)%27])
    # Ik = Ik%27
    print("Ik: " + repr(Ik))
    if(Ik >= 0.0741):
        shift = k
        print('Mayor a 0.0741: '+repr(Ik))
        break

print("El valor del desplazamiento k es: " + repr(shift))

alph = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Funcion que descifra.
def dec(key, encriptedString):

	# La cadena que vamos a regresar con el texto encriptado.
	clearString = ""

	# Iteramos cada char de la cadena en claro.
	for char in encriptedString:
		# Movemos la posicion del char con respecto a la llave.
		op = alph.find(char)-key
		# Sacamos el modulo para los casos que se salen del indice.
		mod = int(op)%27
		# Vamos concatenando el nuevo char al resultado.
		clearString = clearString+str(alph[mod])

	# Regresamos la cadena descencriptada.
	return clearString

# print(shift)
# print(bloc)
# print("--------------")
print(dec(shift, bloc))
# print(dec(shift, cypherClean))
# print(dec(shift, cypher))
