import socket
import rsa
import generate_key
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5004  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(2048)
        print(data)
        publicKey, privateKey =generate_key.loadKeys()
        
        #decryptMessage = rsa.decrypt(data, privateKey).decode()
        decryptMessage = generate_key.decrypt(data, privateKey)
        
        if not decryptMessage:
            # if data is not received break
            break
        print("from connected user: " + str(decryptMessage))
        data = input(' -> ')
        publicserverKey, privatservereKey =generate_key.loadserverKeys()
        ciphertext =generate_key .encrypt(data, publicserverKey)
        
        
        conn.send(ciphertext)  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
