import socket 

target_host = "127.0.0.1" #change as you like 
target_port = 9999 #change as you like

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is ipv4 and SOCK_STREAM is TCP client

client.connect((target_host, target_port))

client.send("some message here") 

response = client.recv(4096) #receiving 4096 bits you can change as you like	

print response
