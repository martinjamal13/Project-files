import os
import paramiko
import socket
import sys
import threading

CWD = os.path.dirname(os.path.realpath(__file__))
HOSTKEY = paramiko.RSAKey(filename = os.path.join(CWD, 'RSA key file'))

class Server( paramiko.ServerInterface): #class used to initalize ssh
    def _init_(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMIN_PROHIBITED
    def check_auth_password(self, username: str, password: str):
        if username == 'tim' and password == 'secret': #never hard code user and pwd in this manner. always envrypt
            return paramiko.AUTH_SUCCESSFUL
        
if __name__ == '__main__':
    server =  "172.16.197.129" #enter your IP 
    ssh_port = 2222
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port)) #binds socket to server and ssh port
        sock.listen(100)
        # start socket as listen
        print("Listen for connection....")
        client, addr = sock.accept()
    except Exception as e:
        print("Listen failed: " + str(e))
        sys.exit(1)
    else:
        print("Got a connection!", client, addr)

    bhSession = paramiko.Transport(client) #configure authenication methods
    bhSession.add.server_key(HOSTKEY)
    server = Server() #server class initialized
    bhSession.start_server(server = server)

    chan = bhSession.accept(20)
    if chan is None:
        print('*** No channel. ')
        sys.exit(1)
    print("Authenicated ")
    print(chan.recv(1024))
    chan.send('Welcome to bh_ssh')
    try:
        while True:
            command = input("Enter command: ")
            if command != 'exit':
                chan.send(command)
                r = chan.recv(8192)
                print(r.decode())
            else:
                chan.send('exit')
                print('exiting')
                bhSession.close()
                break
    except KeyboardInterrupt:
        bhSession.close()

