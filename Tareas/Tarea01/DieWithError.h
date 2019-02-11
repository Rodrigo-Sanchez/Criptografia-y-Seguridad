#include <stdio.h> /* for perror() */
#include <stdlib.h> /* for exit() */

/*DieWithError se usara para terminar la aplicacion. Saldra un mensaje diciendonos cual fue el error (errorMessage) */
void DieWithError(char *errorMessage){
  /* perror() produce un mensaje hacia la stderr
     que es la salida estándar de error */
  perror(errorMessage);
  exit(1);
}
