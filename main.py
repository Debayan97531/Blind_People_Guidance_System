import cv2
import numpy as np
from time import time
import pyttsx3
import zmq

from util.obj_detection import objectDetection
from util.vis import visualize_frame
from util.distance_est  import *
from util.create_bounding_box import ego_roi
from logical.warning import collision_warning

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://192.168.137.213:5555')
socket.setsockopt_string(zmq.SUBSCRIBE, '')


context_1 = zmq.Context()
socket_1 = context_1.socket(zmq.PUB)
socket_1.bind('tcp://192.168.70.221:5555')


detect = objectDetection()

video_path = "D:/TIVRA AI\DATASET\VID_20210624_162710_Trim.mp4" # front camera
cap = cv2.VideoCapture(video_path)

count = 0
center_points_prev_frame = []
tracking_objects = {}
track_id = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def run_voiceAssist(text):
    engine.say(text)
    engine.runAndWait()

while True:

    message = socket.recv_pyobj()
    frame = cv2.imdecode(message['shreasi'], cv2.IMREAD_COLOR)

    start_time = time()
    name, box_coord, obj_detected_frame = detect.detect_objects(frame) # getting the bounding box
    DIST_H_per_FRAME, DIST_2_per_FRAME, frame_2, box_coord_2  = calculate_distance(box_coord, obj_detected_frame, name) # calculating the distance
    frame_3_roi, coords_in_roi, distance_in_roi = ego_roi(frame_2, name, box_coord_2, DIST_H_per_FRAME) # creating the bounding box
    # for i in range(len(name)):
    #     text = str(name[i]) + "is at a distance" + str(np.round(DIST_H_per_FRAME[i])) + "meter"
    #     run_voiceAssist(text)
    # text = name[0] 
    # print(DIST_2_per_FRAME[0])
    collision_warning(coords_in_roi,distance_in_roi,frame_3_roi)



    # print(DIST_H_per_FRAME)
    # r,en_image = cv2.imencode(".jpg",obj_detected_frame, encode_param )
    # send_to_client = {"server":en_image}
    # socket_1.send_pyobj(send_to_client)
    # print("sending ...")
    

    end_time = time()
    visualize_frame(obj_detected_frame, start_time, end_time)
