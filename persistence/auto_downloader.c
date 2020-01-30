#include <stdio.h> 
#include <windows.h> 
#include <wininet.h>

#pragma comment (lib, "wininet.lib") 
 
int main() 
{ 

    FILE *fp; // Added 
    HINTERNET hOpen, hURL; 

    hOpen = InternetOpen("WebReader", INTERNET_OPEN_TYPE_PRECONFIG, NULL, NULL, 0 ); 
    hURL = InternetOpenUrl( hOpen, "https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe", 
                            NULL, 0, 0, 0 ); 
    const int numRead = 99; 
    char file[numRead]; 
    unsigned long read; 
    fp = fopen("%homepath%\\python.exe", "wb"); // Added 
    do 
    { 
        InternetReadFile(hURL, file, numRead - 1, &read); 
        fwrite(file, sizeof(char), read, fp);
        file[read] = '\0'; 
        printf("%s", file);
    } while (read == numRead - 1);
    fclose(fp);  // Added 
    printf ("\n"); 
    InternetCloseHandle(hOpen);
    InternetCloseHandle(hURL);

    return 0; 
}
