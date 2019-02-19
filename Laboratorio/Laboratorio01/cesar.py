# -*- coding: utf-8 -*-

# Programa que genera un desplazamiento para
# cifrar o descifrar como en el Cifrado de Cesar.

# El alfabeto de entrada con el que vamos a estar trabajando.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ., "
# La cadena que vamos a encriptar.
clearString = str(raw_input("Cadena a encriptar: ")).upper()
# La llave que vamos a utilizar.
key = int(raw_input("Digita la llave: "))

# Funcion que cifra.
def enc(key, clearString):

	# La cadena que vamos a regresar con el texto encriptado.
	encriptedString = ""

	# Iteramos cada char de la cadena en claro.
	for char in clearString:
		# Movemos la posicion del char con respecto a la llave.
		op = alphabet.find(char)+key
		# Sacamos el modulo para los casos que se salen del indice.
		mod = int(op)%29
		# Vamos concatenando el nuevo char al resultado.
		encriptedString = encriptedString+str(alphabet[mod])

	# Regresamos la cadena encriptada.	
	return encriptedString

# Funcion que descifra.
def dec(key, encriptedString):

	# La cadena que vamos a regresar con el texto encriptado.
	clearString = ""

	# Iteramos cada char de la cadena en claro.
	for char in encriptedString:
		# Movemos la posicion del char con respecto a la llave.
		op = alphabet.find(char)-key
		# Sacamos el modulo para los casos que se salen del indice.
		mod = int(op)%29
		# Vamos concatenando el nuevo char al resultado.
		clearString = clearString+str(alphabet[mod])

	# Regresamos la cadena descencriptada.
 	return clearString

# Imprimimos el resultado de la funcion enc.
print enc(key, clearString)
# Imprimimos el resultado de la funcion dec.
print dec(key, enc(key, clearString))

# Codigo para leer los bytes de un archivo.
with open("calamardo_pastel.jpg", "rb") as f:
	bytes_archivo = f.read()
	# Lista donde vamos a guardar el archivo en hexadecimal.
	numbers = []
	for b in bytes_archivo:
		# La funcion ord transforma del 0 al 255.
		# La funcion chr nos da la representación en hexadecimal.
		numbers.append(chr(ord(b)))

# print numbers
