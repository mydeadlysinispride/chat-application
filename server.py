def broadcast_message(message):
    pass

def recieve_message(client_socket):
    pass   

def connect_client():
      '''Connect an incoming client to the server'''
    while True:
        #Accept any incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}...")

        #Send a NAME flag to prompt the client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        #Add new client socket and client name to appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        #Update the server, individual client, and ALL clients
        print(f"Name of new client is {client_name}\n") #server
        client_socket.send(f"{client_name}, you have connected to the server!".encode(ENCODER)) #Individual client
        broadcast_message(f"{client_name} has joined the chat!".encode(ENCODER))

        #Now that a new client has connected, start a thread
        recieve_thread = threading.Thread(target=recieve_message, args=(client_socket,))
        recieve_thread.start()

        
#Start the server
print("Server is listening for incoming connections...\n")
connect_client()
