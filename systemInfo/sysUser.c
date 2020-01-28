#include <stdio.h> // include the things

int main() // instantiate main
{
    FILE *p; // for unix and windows set file to p
    char ch; // char variable of ch
    p = popen("net user","r");   // command for windows get system info ***COMMENT OUT FOR USE ON UNIX****
    if( p == NULL) // if p = null
    {
        puts("Unable to open process"); // tell the user
        return(1);
    }
    while( (ch=fgetc(p)) != EOF) // while ch is not the end of the file then print c and close the file
        putchar(ch);
    pclose(p);
    return(0);
}