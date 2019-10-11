import socket 
import threading

bind_ip = "127.0.0.1" # change as you like
bind_port = 1234 #change as you like

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET=ipv4 

server.bind((bind_ip,bind_port)) #binding

server.listen(5) #start listing with max 5 connections

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

#this is our client-handling thread

def handle_client(client_socket):
    # print out what the client sends
    request = client_socket.recv(1024)

    print "[*] Received: %s" % request

    # send back a packet

    client_socket.send("ACK!")
    
    client_socket.close()

while True:
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
