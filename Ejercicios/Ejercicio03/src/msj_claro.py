import os
from Crypto.Cipher import AES
k = os.urandom(16)
iv = os.urandom(16)
cifrador = AES.new(k, 2, iv)
mensaje = open('msj_claro.py', 'rb').read()
pad_len = 16 - (len(mensaje) % 16)
padding = bytes([pad_len]) * pad_len
msj_cifrado = cifrador.encrypt(mensaje+padding)
with open('llave', 'wb') as w:
    w.write(k)
with open('msj_cifrado', 'wb') as w:
    w.write(iv + msj_cifrado)

msj_claro.py
Mostrando msj_claro.py.