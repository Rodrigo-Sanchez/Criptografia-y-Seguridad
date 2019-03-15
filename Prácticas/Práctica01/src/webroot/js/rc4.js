/*
 * Función que implementa el cifrado RC4.
 * @param string key llave para encriptar/descencriptar.
 * @param string string cadena a encriptar/descencriptar.
 * @return string res el resultado de aplicar el método.
 */
function RC4(key, str) {
    let s = [], j = 0, x, res = '';
    for (let i = 0; i < 256; i++) {
        s[i] = i;
    }
    for (i = 0; i < 256; i++) {
        j = (j + s[i] + key.charCodeAt(i % key.length)) % 256;
        x = s[i];
        s[i] = s[j];
        s[j] = x;
    }
    i = 0;
    j = 0;
    for (let y = 0; y < str.length; y++) {
        i = (i + 1) % 256;
        j = (j + s[i]) % 256;
        x = s[i];
        s[i] = s[j];
        s[j] = x;
        res += String.fromCharCode(str.charCodeAt(y) ^ s[(s[i] + s[j]) % 256]);
    }
    return res;
}

console.log(RC4("hola", "AAAAAAAAAAAA"))

/**
 * Función que obtiene un número criptográficamente seguro en el rango [0,1).
 * @returns number 0 o 1 dependiendo si el resultado es mayor/menor que 0.5
 */
function cryptoRandom() {
    return (window.crypto.getRandomValues(new Uint32Array(1))[0] / 0x100000000) > 0.5 ? 1 : 0;
}

// Vector de Inicialización de 5 bytes para cada mensaje cifrado.
let IV = Array.from(Array(5), () => cryptoRandom());