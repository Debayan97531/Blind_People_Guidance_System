import socket
import pickle

# create socket and listen for incoming connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 1234))  # listen on all available interfaces
s.listen()

# accept incoming connection and receive dictionary
conn, addr = s.accept()
data_bytes = b''
while True:
    # receive data in chunks
    chunk = conn.recv(4096)
    if not chunk:
        break
    data_bytes += chunk

# deserialize dictionary using pickle
data = pickle.loads(data_bytes)

# print received data
print(data)

# close connection and socket
conn.close()
s.close()
