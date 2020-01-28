#include <stdio.h> // include the things

int main() // instantiate main
{
    FILE *p; // for unix and windows set file to p
    // FILE *p2; // for unix for extra info have a second file of p2
    char ch; // char variable of ch

    p = popen("ipconfig /all","r");   // command for windows ***COMMENT OUT FOR USE ON UNIX***
//  p = popen("ip -a -h address","r"); command for unix *** COMMENT OUT FOR USE ON WINDOWS*** 
//  p2 = popen("ip -a -h routes","r"); command for unix *** COMMENT OUT FOR USE ON WINDOWS***
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