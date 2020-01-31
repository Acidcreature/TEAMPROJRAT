/*
	Create a TCP socket
    *********TO COMPILE need to add the -lws2_32 flag set in GCC***********
*/

#include<stdio.h>
#include<winsock2.h>
#include<windows.h>
#include<ws2tcpip.h>
#include<stdlib.h>

#pragma comment(lib,"ws2_32.lib") //Winsock Library

int main(void)
{
	WSADATA wsa;
	SOCKET s;
    struct sockaddr_in server;
	printf("\nInitialising Winsock...");
    char *message[2048] = {0};
	if (WSAStartup(MAKEWORD(2,2),&wsa) != 0)
	{
		printf("Failed. Error Code : %d",WSAGetLastError());
		return 1;
	}
	
	printf("Initialised.\n");
	
	
	if((s = socket(AF_INET , SOCK_STREAM , 0 )) == INVALID_SOCKET)
	{
		printf("Could not create socket : %d" , WSAGetLastError());
	}

	printf("Socket created.\n");

    server.sin_addr.s_addr = inet_addr("127.0.0.1");
    server.sin_family = AF_INET;
    server.sin_port = htons(8888);
    char com[2048] = {"4"};
    if (connect(s, (struct sockaddr *)&server, sizeof(server)) < 0)
    {
        puts("Connect error");
        return 1;
    }
    puts("connected");
    recv(s, message, 2048, 0);
    send(s, com, sizeof(com), 0);
    printf("\nmsg: %s\n", message);
    recv(s, message, 4096, 0);
    printf("\nmsg: %s\n", message);
	return 0;
}