#include <stdio.h>
#include <stdlib.h>
#include "DieWithError.h"

int main()
{

    // void decript(int a, int b);   //Write the correct image on file
    // int modInverse(int a, int c); //Calculate the modular inverse

    // int size, a, b;
    // unsigned char *image;
    // unsigned char b1, b2, decriptB1, decriptB2;

    FILE *fp;
    // El nombre del archivo que vamos a abrir.
    char ch, *file = "c1";
    int size;
    unsigned char *image;
    unsigned char b1, b2;

    // Abrimos el archivo fp.
    fp = fopen(file, "r");

    if (fp == NULL)
    {
        perror("Ocurrió un error mientras se abría el archivo");
        exit(EXIT_FAILURE);
    }

    // Busca el inicio del archivo.
    fseek(fp, 0, SEEK_END);

    // Obtenemos el tamaño de memoria del archivo.
    size = ftell(fp);

    fseek(fp, 0, SEEK_SET);

    // Guardamos la imagen como un arreglo de bytes.
    image = (unsigned char *)malloc(size);

    if (!image)
    {
        perror("Ocurrió un error mientras se abría el archivo");
        exit(EXIT_FAILURE);
    }

    printf("El tamaño total del archivo %s es %d bytes\n", file, size);

    fread(image, size, sizeof(unsigned char), fp);

    b1 = *image;
    b2 = *(image + 1);

    // Cerramos el archivo fp.
    fclose(fp);

    return 0;
}

/* Given the pair (a,b), the key, decript the file and write
   another one which is the correct image */
void decript(int a, int b)
{
    int size;
    unsigned char *image;
    unsigned char c;
    FILE *fp, *decriptPic;
    char *file = "c1";
    int modInverse(int a, int c);
    //Get fp Size
    if ((fp = fopen(file, "r")) == 0)
        DieWithError("fopen() failed");
    fseek(fp, 0, SEEK_END);
    size = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    //Store fp as Byte Array
    image = (unsigned char *)malloc(size);
    if (!image)
    {
        DieWithError("malloc() failed");
    }
    fread(image, size, sizeof(unsigned char), fp);

    FILE *f = fopen("cancion_1.mp3", "w");
    if (f == NULL)
        DieWithError("Error opening file!");

    int i = 0;
    int mi = modInverse(a, 256);
    while (i < size)
    {
        c = *(image + i);
        c = (mi * (c - b)) % 256;
        *(image + i) = c;
        fputc(*(image + i), f);
        i++;
    }
}

/* Calculate the modular inverse of a and c,
   returns 0 if not exists, that is, a and c are not coprimes */
int modInverse(int a, int c)
{
    for (int b = 0; b < c; b++)
    {
        if ((a * b) % c == 1)
            return b;
    }
    return 0;
}
