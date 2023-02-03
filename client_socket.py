import socket
import rsa
import generate_key
def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5004  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input("write your message")# take input
    while message.lower().strip() != 'bye':
        generate_key.generateKeys()
        publicKey, privateKey =generate_key.loadKeys()
    
        ciphertext =generate_key .encrypt(message, publicKey)
        
        
        client_socket.send(ciphertext)  # send message
        publicserverKey, privatservereKey =generate_key.loadserverKeys()
        
        data = client_socket.recv(2048) # receive response
        decryptMessage = generate_key.decrypt(data, privatservereKey)

        print('Received from server: ' + decryptMessage)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()