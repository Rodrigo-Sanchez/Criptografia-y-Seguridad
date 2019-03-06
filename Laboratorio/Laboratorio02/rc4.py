# -*- coding: utf-8 -*-

# Programa que genera un cifrado de RC4.

class RC4:
    def __init__(self, key):
        self.key = key
    
    def get_byte(self):
        S = list()
        for i in range(256):
            S.append(i)
        print(S)

        j = 0
        for i in range(256):
            j = (j + S[i] + ord(self.key[i % len(self.key)])) % 256
            S[i], S[j] = S[j], S[i]
        print(S)

llave = list('mi llave')
generador = RC4(llave)
nuevo_byte = generador.get_byte()

# print(llave)
# print(generador)
# print(nuevo_byte)