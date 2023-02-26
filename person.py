import cv2
import numpy as np
import zmq
import pickle


from util.vis import visualize_frame
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://192.168.137.213:5555')



# context_1 = zmq.Context()
# socket_1 = context_1.socket(zmq.SUB)
# socket_1.connect('tcp://192.168.70.221:5555')
# socket_1.setsockopt_string(zmq.SUBSCRIBE,'')

url = "http://192.168.137.118:8080/video"
cap = cv2.VideoCapture(url)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]
while (True):
    camera, frame = cap.read()
    # print(frame.shape)
    frame = cv2.resize(frame, (500, 500),
               interpolation=cv2.INTER_LINEAR)
    r, en_img = cv2.imencode(".jpg", frame, encode_param)
    message = {'shreasi': en_img}
    # data = pickle.dumps(message)
    socket.send_pyobj(message)
    print("sending ...")
    
    # from_server = socket_1.recv_pyobj()
    # pro_frame = cv2.imdecode(from_server['server'], cv2.IMREAD_COLOR)
    
    # if pro_frame is not None:
    #     cv2.imshow("Frame", pro_frame)
    # q = cv2.waitKey(1)
    # if q == ord("q"):
    #     break
cv2.destroyAllWindows()
