#include <stdio.h> // include the things

int main() // instantiate main
{
    FILE *p; // for unix and windows set file to p
    // FILE *p2; // for unix for extra info have a second file of p2
    char ch; // char variable of ch

    p = popen("systeminfo","r");   // command for windows get system info ***COMMENT OUT FOR USE ON UNIX***
//  p = popen("uname -a","r"); command for unix get OS info*** COMMENT OUT FOR USE ON WINDOWS*** 
//  p2 = popen("lshw","r"); command for unix system info *** COMMENT OUT FOR USE ON WINDOWS***
    if( p == NULL) // if p = null
    {
        puts("Unable to open process"); // tell the user
        return(1);
    }
    while( (ch=fgetc(p)) != EOF) // while ch is not the end of the file then print c and close the file
        putchar(ch);
    pclose(p);
    /*
    if( p2 == NULL) // if p = null
    {
        puts("Unable to open process"); // tell the user
        return(1);
    }
    while( (ch=fgetc(p2)) != EOF) // while ch is not the end of the file then print c and close the file
        putchar(ch);
    pclose(p2);
    */

    return(0);
}