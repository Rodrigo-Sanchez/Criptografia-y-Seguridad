#include <stdio.h>
#include <stdlib.h>
#include "DieWithError.h"

int main()
{

    // void decript(int a, int b);   //Write the correct image on file
    // int modInverse(int a, int c); //Calculate the modular inverse

    // int imageSize, a, b;
    // unsigned char *image;
    // unsigned char b1, b2, decriptB1, decriptB2;

    FILE *picture;
    // El nombre del archivo que vamos a abrir.
    char ch, *file = "c1";

    // Get Picture Size
    picture = fopen(file, "r");
    if (picture == NULL)
    {
        perror("Ocurrió un error mientras se abría el archivo");
        exit(EXIT_FAILURE);
    }

    // printf("El contenido del archivo %s es:\n", picture);
    while((ch = fgetc(picture)) != EOF)
        printf("%c", ch);

    fclose(picture);
    // fseek(picture, 0, SEEK_END);
    // imageSize = ftell(picture);
    // fseek(picture, 0, SEEK_SET);


    // //Store Picture as Byte Array
    // image = (unsigned char *)malloc(imageSize);
    // if (!image)
    // {
    //     DieWithError("malloc() failed");
    // }
    // fread(image, imageSize, sizeof(unsigned char), picture);

    // //Get the first 2 bytes of file
    // b1 = *image;
    // b2 = *(image + 1);
    // // printf("D1: %d, D2: %d\n", b1, b2);

    // //Now find the two keys a and b, also write the correct image
    // for (int i = 0; i < 256; i++)
    // {
    //     int mi;
    //     mi = modInverse(i, 256);
    //     if (mi == 0)
    //         continue;
    //     for (int j = 0; j < 256; j++)
    //     {
    //         decriptB1 = (mi * (b1 - j)) % 256;
    //         decriptB2 = (mi * (b2 - j)) % 256;

    //         if (decriptB1 == 255 && decriptB2 == 216)
    //         {
    //             printf("The keys are a = %d and b = %d\n", i, j);
    //             decript(i, j);
    //         }
    //     }
    // }

    return 0;
}

/* Given the pair (a,b), the key, decript the file and write
   another one which is the correct image */
void decript(int a, int b)
{
    int imageSize;
    unsigned char *image;
    unsigned char c;
    FILE *picture, *decriptPic;
    char *file = "c1";
    int modInverse(int a, int c);
    //Get Picture Size
    if ((picture = fopen(file, "r")) == 0)
        DieWithError("fopen() failed");
    fseek(picture, 0, SEEK_END);
    imageSize = ftell(picture);
    fseek(picture, 0, SEEK_SET);

    //Store Picture as Byte Array
    image = (unsigned char *)malloc(imageSize);
    if (!image)
    {
        DieWithError("malloc() failed");
    }
    fread(image, imageSize, sizeof(unsigned char), picture);

    FILE *f = fopen("cancion_1.mp3", "w");
    if (f == NULL)
        DieWithError("Error opening file!");

    int i = 0;
    int mi = modInverse(a, 256);
    while (i < imageSize)
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
