#include <stdio.h>
#include <stdlib.h>

int main()
{

    FILE *fp, *fc;
    // El nombre del archivo que vamos a abrir.
    char ch, *file = "cancion_2.mp3", *file2 = "cosa_rara";
    int size, size2;
    unsigned char *cancion_2, *cosa_rara;
    unsigned char b1, b2;

    // Abrimos el archivo fp y fc.
    fp = fopen(file, "r");
    fc = fopen(file2, "r");

    if (fp == NULL || fc == NULL)
    {
        perror("Ocurrió un error mientras se abrían los archivos");
        exit(EXIT_FAILURE);
    }

    // Busca el inicio de los archivos.
    fseek(fp, 0, SEEK_END);
    fseek(fc, 0, SEEK_END);

    // Obtenemos el tamaño de memoria del archivo.
    size = ftell(fp);
    size2 = ftell(fc);

    fseek(fp, 0, SEEK_SET);
    fseek(fc, 0, SEEK_SET);

    // Guardamos la cancion_2 como un arreglo de bytes.
    cancion_2 = (unsigned char *)malloc(size);

    // Guardamos cosa_rara como un arreglo de bytes.
    cosa_rara = (unsigned char *)malloc(size2);

    if (!cancion_2 && !cosa_rara)
    {
        perror("Ocurrió un error mientras se abrían los archivos");
        exit(EXIT_FAILURE);
    }

    printf("El tamaño total del archivo %s es %d bytes\n", file, size);
    printf("El tamaño total del archivo %s es %d bytes\n", file2, size2);

    // Lee y muestra la información.
    fread(cancion_2, size, sizeof(unsigned char), fp);
    fread(cosa_rara, size2, sizeof(unsigned char), fc);

    b1 = *cancion_2;
    b2 = *cosa_rara;

    for(int i = 0; i < size; i++) {
        b1 = *(cancion_2+i); 
        printf ("%d ", b1);
    }

    for(int i = 0; i < size2; i++) {
        b2 = *(cosa_rara+i); 
        printf ("%d ", b2);
    }

    // Cerramos el archivo fp.
    fclose(fp);

    // Cerramos el archivo fc.
    fclose(fc);

    // Terminamos el programa.
    return 0;
}
