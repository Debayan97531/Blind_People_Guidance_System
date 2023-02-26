import zmq
import cv2
import pickle

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://192.168.137.213:5555')
socket.setsockopt_string(zmq.SUBSCRIBE, '')


context_1 = zmq.Context()
socket_1 = context_1.socket(zmq.PUB)
socket_1.bind('tcp://192.168.0.104:5555')

listner = 0

while(True):
    message = socket.recv_pyobj()
    # data = pickle.loads(message)
    data = cv2.imdecode(message['shreasi'], cv2.IMREAD_COLOR)
    cv2.imshow("frame", data)
    cv2.waitKey(1)


