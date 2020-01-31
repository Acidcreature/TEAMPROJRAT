#include <stdio.h> // include the things

int main() // instantiate main
{
    FILE *p; // for unix and windows set file to p
    FILE * res = fopen("results.txt", "w");
    char ch; // char variable of ch
    char arr[2048] = {0};
    p = popen("systeminfo","r");   // command for windows get system info ***COMMENT OUT FOR USE ON UNIX***
    if( p == NULL) // if p = null
    {
        puts("Unable to open process"); // tell the user
        return(1);
    }
    while( (ch=fgetc(p)) != EOF) // while ch is not the end of the file then print c and close the file
        {
        putchar(ch);
        fputc(ch, res);
        }
    pclose(p);
    fclose(res);
    return(0);
}