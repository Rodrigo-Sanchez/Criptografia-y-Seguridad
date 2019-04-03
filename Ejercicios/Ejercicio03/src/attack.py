


# Función que implementa el oráculo de padding.
# Usa AES en modo CBC con la llave global k para descifrar el criptotexto.
# :param str criptotext: El criptotexto de entrada.
# :return: Booleano si el mensaje descifrado tiene un relleno válido.
def padding_correcto(criptotext):



# Función que recupera el padding.
# :param str bloque: Bloque de cadena de 16(n + 1) bytes, es decir, un bloque IV y n bloques de datos.
# :return: La longitud del padding.
def recupera_padding(block):
    # Usar padding_correcto.



# Función que implementa el oráculo de padding.
# Usa AES en modo CBC con la llave global k para descifrar el criptotexto.
# :return: Recupera el mensaje claro que corresponde al mensaje cifrado C.
def recupera_mensaje_original():
    # Usar recupera_padding.

