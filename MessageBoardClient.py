import socket
import time

#SERVER_ADDRESS = '127.0.0.1'
#SERVER_PORT = 16111
BUFFER_SIZE = 4096
SENDING_COOLDOWN = 0.3

def send_message(sock, message):
    time.sleep(SENDING_COOLDOWN)
    sock.sendall(bytes(message , encoding='utf-8'))

def receive_message(sock):
    data = sock.recv(BUFFER_SIZE)
    return str(data, encoding='utf-8')

def deletefunc(sock):
    while True:
        message_id = input("client: ")
        send_message(sock, message_id)
        if message_id.strip() == "#":
            break
    response = receive_message(sock)
    print("server:", response)

def getfunc(sock):
    while True:
        response = receive_message(sock)
        if response == '#':
            break
        elif response == "":
            break
        print("server:", response)
    print("server:", response)

def quitfunc(sock):
    response = receive_message(sock)
    print("server:", response)

def postfunc(sock):
    while True:
        line = input("client: ")
        send_message(sock, line)
        if line.strip() == "#": #end of the message
            break
    response = receive_message(sock)
    print("server:", response)

def diffcommand(sock):
    response = receive_message(sock)
    print("server:", response)

def main():
    SERVER_ADDRESS = input() #get the server IP
    SERVER_PORT = int(input()) #get the port number
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        sock.connect((SERVER_ADDRESS, SERVER_PORT))
        while True:
            command = input("client: ").strip().upper() #getting the command
            send_message(sock, command)
            
            if command == 'POST':
                postfunc(sock)
            elif command == 'GET':
                getfunc(sock)
            elif command == 'DELETE':
                deletefunc(sock)
            elif command == 'QUIT':
                quitfunc(sock)
                break
            else:
                diffcommand(sock)

if __name__ == '__main__':
    main()