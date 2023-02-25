import socket
import pickle

# define dictionary to send
data = {"name": "Alice", "age": 25, "city": "New York"}

# create socket and connect to receiver
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.33.34', 1234))  # replace with actual receiver IP address

# serialize dictionary using pickle and send it over socket
data_bytes = pickle.dumps(data)
s.sendall(data_bytes)

# close socket
s.close()
