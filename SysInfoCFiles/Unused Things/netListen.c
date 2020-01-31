/*
	Create a TCP socket
    *********TO COMPILE need to add the -lws2_32 flag set in GCC***********
*/
/*
	Live Server on port 8888
*/
#include<io.h>
#include<stdio.h>
#include<winsock2.h>
char cmd(char * msg, char * statement);
// #pragma comment(lib,"ws2_32.lib") //Winsock Library

int main(void)
{
	WSADATA wsa;
	SOCKET s , new_socket;
	struct sockaddr_in server , client;
	int c;
	char *message;

	printf("\nInitialising Winsock...");
	if (WSAStartup(MAKEWORD(2,2),&wsa) != 0)
	{
		printf("Failed. Error Code : %d",WSAGetLastError());
		return 1;
	}
	
	printf("Initialised.\n");
	
	//Create a socket
	if((s = socket(AF_INET , SOCK_STREAM , 0 )) == INVALID_SOCKET)
	{
		printf("Could not create socket : %d" , WSAGetLastError());
	}

	printf("Socket created.\n");
	
	//Prepare the sockaddr_in structure
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	server.sin_port = htons( 8888 );
	
	//Bind
	if( bind(s ,(struct sockaddr *)&server , sizeof(server)) == SOCKET_ERROR)
	{
		printf("Bind failed with error code : %d" , WSAGetLastError());
		exit(EXIT_FAILURE);
	}
	
	puts("Bind done");

	//Listen to incoming connections
	listen(s , 3);
	
	//Accept and incoming connection
	puts("Waiting for incoming connections...");
	
	c = sizeof(struct sockaddr_in);
	char com[4096] = {0};
	while( (new_socket = accept(s , (struct sockaddr *)&client, &c)) != INVALID_SOCKET )
	{
		puts("Connection accepted");
		
		//Reply to the client
		message = "Hello Client , I have received your connection.\n send 1 for users, 2 for ip info, 3 for system info.\n";
		send(new_socket , message , strlen(message) , 0);
        recv(new_socket, com, 4096, 0);
        printf("\nCom: \n%c", com[0]);
        if (com[0] == '1')
            {
                char message2[4096] = {0};
                cmd(message2, "net user");
                printf("\nMsg: %s\n", message2);
                setsockopt(new_socket, IPPROTO_TCP, TCP_NODELAY, (char *) &server, sizeof(server));
                send(new_socket , message2, sizeof(message2), 0);
            }
        else if (com[0] == '2')
        
            {
                char message2[4096] = {0};
                cmd(message2, "ipconfig /all");
                printf("\nMsg: %s\n", message2);
                setsockopt(new_socket, IPPROTO_TCP, TCP_NODELAY, (char *) &server, sizeof(server));
                send(new_socket , message2, sizeof(message2), 0);
            }
        else if (com[0] == '3')
            {
                char message2[4096] = {0};
                cmd(message2, "systeminfo");
                printf("\nMsg: %s\n", message2);
                setsockopt(new_socket, IPPROTO_TCP, TCP_NODELAY, (char *) &server, sizeof(server));
                send(new_socket , message2, sizeof(message2), 0);
            }
        else if (com[0] == '4')
            {
                char ip[15] = {"10.240.234"};
                char comd[100];
                snprintf(comd, sizeof(comd), "FOR /L %%i IN (1,1,25) DO ping -n 1 %s.%%i", ip);
                char message2[4096] = {0};
                cmd(message2, comd);
                printf("\nMsg: %s\n", message2);
                setsockopt(new_socket, IPPROTO_TCP, TCP_NODELAY, (char *) &server, sizeof(server));
                send(new_socket , message2, sizeof(message2), 0);
            }
        else
            {
                char message2[4096] = {"Dangit Bobby"};
                printf("\nMsg: %s\n", message2);
                setsockopt(new_socket, IPPROTO_TCP, TCP_NODELAY, (char *) &server, sizeof(server));
                send(new_socket , message2, sizeof(message2), 0);
            }
        

	}
	
	if (new_socket == INVALID_SOCKET)
	{
		printf("accept failed with error code : %d" , WSAGetLastError());
		return 1;
	}

	closesocket(s);
	WSACleanup();
	
	return 0;
}

char cmd(char * msg, char * statement) 
{
    char buf[2048] = {0};
    char *str = NULL;
    char *temp = NULL;
    unsigned int size = 1;  // start with size of 1 to make room for null terminator
    unsigned int strlength;
    FILE *comm;
    if (NULL == (comm = popen(statement, "r"))) 
      {
        perror("popen");
        exit(EXIT_FAILURE);
      }
    while (fgets(buf, sizeof(buf), comm) != NULL) 
      {
        strlength = strlen(buf);
        temp = realloc(str, size + strlength);  // allocate room for the buf that gets appended
        if (temp == NULL) 
          {
        // allocation error
          } 
        else 
          {
            str = temp;
          }
        strcpy(str + size - 1, buf);     // append buffer to str
        size += strlength; 
      }
    pclose(comm);
    snprintf(msg, "\n%s\n", str);
    return 0;
}