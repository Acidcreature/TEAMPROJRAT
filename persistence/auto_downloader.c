#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <errno.h>
#include <arpa/inet.h>

int main(void){

    //char domain[] = "www.gnu.org", path[]="/licenses/gpl.txt"; //example 
    char domain[] = "python.org", path[]="/ftp/python/3.7.6/python-3.7.6-amd64.exe"; //example 
        int sock, bytes_received;  
    char send_data[1024],recv_data[9999];
    struct sockaddr_in server_addr;
    struct hostent *he;
    FILE *fp;

    he = gethostbyname(domain);
    if (he == NULL){
       herror("gethostbyname");
       exit(1);
    }

    if ((sock = socket(AF_INET, SOCK_STREAM, 0))== -1){
       perror("Socket");
       exit(1);
    }
    server_addr.sin_family = AF_INET;     
    server_addr.sin_port = htons(80);
    server_addr.sin_addr = *((struct in_addr *)he->h_addr);
    bzero(&(server_addr.sin_zero),8); 

    printf("Connecting ...\n");
    if (connect(sock, (struct sockaddr *)&server_addr,sizeof(struct sockaddr)) == -1){
       perror("Connect");
       exit(1); 
    }

    printf("Sending data ...\n");

    snprintf(send_data, sizeof(send_data), "GET /%s HTTP/1.1\r\nHost: /%s\r\n\r\n", path, domain);

    if(send(sock, send_data, strlen(send_data), 0)==-1){
        perror("send");
        exit(2); 
    }
    printf("Data sent.\n");  

    fp=fopen("received_file","wb");
    printf("Recieving data...\n\n");
    while((bytes_received = recv(sock, recv_data, 9999, 0))>0){
        if(bytes_received==-1){
            perror("recieve");
            exit(3);
        }
        recv_data[bytes_received] = '\0';

        fwrite(recv_data,bytes_received,1,fp);
        printf("%s", recv_data);
    }



    close(sock);
    fclose(fp);
    printf("\n\nDone.\n\n");
    return 0;
}