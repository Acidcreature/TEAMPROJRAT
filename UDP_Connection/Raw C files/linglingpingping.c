

#include <stdio.h> // include the things

int main() // instantiate main
{
    FILE *p; // for unix and windows set file to p
    FILE * res = fopen("results.txt", "w"); // opens a file that the program writes the data to

    char ch; // char variable of ch

    char ip[15] = {"127.0.0.1"}; //place holder for ip variable

    char cid[] = {"24"}; //place holder for cider variable

    char cmd[100]; //place holder for command 'cmd' variable
    printf("Enter IP: "); //print statement to collect 'ip' variable
    fgets(ip, 15, stdin); //stores user inputed variable
    printf("\nEnter cider: "); //print statements to collect 'cider' variable
    fgets(cid, 2, stdin); //stores user inputed variable
    snprintf(cmd, sizeof(cmd), "ping -c 1 %s/%s", ip, cid); //runs ping command with user inputed variables

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

