import cv2
import numpy as np
from time import time
import pyttsx3

from util.obj_detection import objectDetection
from util.vis import visualize_frame
from util.distance_est  import *
from util.create_bounding_box import ego_roi
from logical.warning import collision_warning


detect = objectDetection()

video_path = "D:/TIVRA AI\DATASET\VID_20210624_162710_Trim.mp4" # front camera
cap = cv2.VideoCapture(video_path)

count = 0
center_points_prev_frame = []
tracking_objects = {}
track_id = 0

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def run_voiceAssist(text):
    engine.say(text)
    engine.runAndWait()

while True:
    ret,frame = cap.read()
    count+=1
    if not ret:
        break

    start_time = time()
    name, box_coord, obj_detected_frame = detect.detect_objects(frame) # getting the bounding box
    DIST_H_per_FRAME, DIST_2_per_FRAME, frame_2, box_coord_2  = calculate_distance(box_coord, obj_detected_frame, name) # calculating the distance
    frame_3_roi, coords_in_roi, distance_in_roi = ego_roi(frame_2, name, box_coord_2, DIST_H_per_FRAME) # creating the bounding box
    for i in range(len(name)):
        text = str(name[i]) + "is at a distance" + str(np.round(DIST_H_per_FRAME[i])) + "meter"
        run_voiceAssist(text)
    # text = name[0] 
    # print(DIST_2_per_FRAME[0])
    collision_warning(coords_in_roi,distance_in_roi,frame_3_roi)



    print(DIST_H_per_FRAME)
    

    end_time = time()
    visualize_frame(obj_detected_frame, start_time, end_time)
