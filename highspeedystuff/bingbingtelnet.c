#include <stdio.h> // include the things

int main() // instantiate main
{
    FILE *p; // for unix and windows set file to p
    FILE * res = fopen("results_tel.txt", "w");  // opens a file to write the output of the program to

    char ch; // char variable of ch

    char ip[15] = {"127.0.0.1"};


    char cmd[100];
    printf("Enter IP: "); //user input to get an ip
    fgets(ip, 15, stdin); //stores the user inputed ip to the 'ip' variable
    snprintf(cmd, sizeof(cmd), "telnet %s", ip); //runs telnet command with user inputed ip

    printf("\n %s \n", cmd);

    

    p = popen(cmd, "r");   // command for windows get system info ***COMMENT OUT FOR USE ON UNIX***

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

