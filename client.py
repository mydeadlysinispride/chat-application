def send_message():
    '''Send a message to the server to be broadcast'''
    while True:
        message = input("")
        client_socket.send(message.encode(ENCODER))

def recieve_message():
    '''Recieve an incoming message from the server'''
    while True:
        try:
            #Recieve an incoming message from the server.
            message = client_socket.recv(BYTESIZE).decode(ENCODER)

            #Check for the name flag, else show the message
            if message == "NAME":
                name = input("What is your name: ")
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            #An error occured, close the connection
            print("An error occured...")
            client_socket.close()
            break
