#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

    // Archivos.
    FILE *fp, *fc, *fn, * fx;
    char ch, *result;
    // El nombre del archivo que vamos a abrir.
    char *file = "cancion_2.mp3", *file2 = "cosa_rara", *file3 = "cosa2", *file4 = "cosa2XOR";
    int size1, size2;
    unsigned char *cancion_2, *cosa_rara;
    unsigned char hex1, hex2;

    // Abrimos el archivo fp, fc, fn y fx.
    fp = fopen(file, "r");
    fc = fopen(file2, "r");
    fn = fopen(file3, "w");
    fx = fopen(file4, "w");

    if (fp == NULL || fc == NULL)
    {
        perror("Ocurrió un error mientras se abrían los archivos");
        exit(EXIT_FAILURE);
    }

    // Busca el inicio de los archivos.
    fseek(fp, 0, SEEK_END);
    fseek(fc, 0, SEEK_END);

    // Obtenemos el tamaño de memoria del archivo.
    size1 = ftell(fp);
    size2 = ftell(fc);

    fseek(fp, 0, SEEK_SET);
    fseek(fc, 0, SEEK_SET);

    // Guardamos la cancion_2 como un arreglo de bytes.
    cancion_2 = (unsigned char *)malloc(size1);

    // Guardamos cosa_rara como un arreglo de bytes.
    cosa_rara = (unsigned char *)malloc(size2);

    if (!cancion_2 || !cosa_rara)
    {
        perror("Ocurrió un error mientras se abrían los archivos");
        exit(EXIT_FAILURE);
    }

    printf("El tamaño total del archivo %s es %d bytes\n", file, size1);
    printf("El tamaño total del archivo %s es %d bytes\n", file2, size2);

    // Lee la información de cada archivo.
    fread(cancion_2, size1, 1, fp);
    fread(cosa_rara, size2, 1, fc);

    hex1 = *cancion_2;
    hex2 = *cosa_rara;

    for (int i = 0; i < size1; i++)
    {
        hex1 = *(cancion_2 + i);
        hex2 = *(cosa_rara + i);

        // Escribimos en el nuevo archivo el XOR de los dos números.
        fputc((hex1 ^ hex2), fn);

        // Escribimos en el nuevo archivo el XOR con la clave holahola...
        if (i % 4 == 1) {
            fputc((hex1 ^ (int)'h'), fx); // h case.
        } else if (i % 4 == 2) {
            fputc((hex1 ^ (int)'o'), fx); // o case.
        } else if (i % 4 == 3) {
            fputc((hex1 ^ (int)'l'), fx); // l case.
        } else if (i % 4 == 0) {
            fputc((hex1 ^ (int)'a'), fx); // a case.
        } 

        // printf ("El hex1 %d XOR hex2 %d es igual a %d.\n", hex1, hex2, hex1^hex2);
    }

    // Cerramos el archivo fp.
    fclose(fp);
    // Cerramos el archivo fc.
    fclose(fc);
    // Cerramos el archivo fn.
    fclose(fn);

    // Terminamos el programa.
    return 0;
}