import socket
import time

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 16111
BUFFER_SIZE = 4096
SENDING_COOLDOWN = 0.3

def send_message(sock, message):
    sock.sendall(bytes(message + "\n", encoding='utf-8'))
    time.sleep(SENDING_COOLDOWN)

def receive_message(sock):
    data = sock.recv(BUFFER_SIZE)
    return data.decode('utf-8').strip()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((SERVER_ADDRESS, SERVER_PORT))
        
        while True:
            flag = False # Used in the edge case with "POST" function
            command = input("client: ").strip().upper() #getting the command
            send_message(client_sock, command)
            
            if command == 'POST':
                while True:
                    line = input("client: ")
                    send_message(client_sock, line)
                    if line.strip() == "#": #end of the message
                        flag = True #edge case
                        break
                response = receive_message(client_sock)
                print("server:", response)
            
            elif command == 'GET':
                while True:
                    response = receive_message(client_sock)
                    if response == '#':
                        break
                    elif response == "":
                        break
                    print("server:", response)
                print("server: #")


            
            elif command == 'DELETE':
                while True:
                    message_id = input("client: ")
                    send_message(client_sock, message_id)
                    if message_id.strip() == "#":
                        break
                response = receive_message(client_sock)
                print("server:", response)
            
            elif command == 'QUIT':
                response = receive_message(client_sock)
                print("server:", response)
                break

            elif not flag: #ensures that it is not end of the 'POST' function
                print("server: ERROR - Command not understood")

if __name__ == '__main__':
    main()