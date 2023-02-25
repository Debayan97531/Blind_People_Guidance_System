import cv2
import numpy as np

def visualize_frame(obj_detected_frame, start_time, end_time):
    '''  This function is just to visualize the output as an image frame
         ARGS        :    obje_detected_frame     ->    image frame as the output from object detection code
                     :    start_time              ->    Starting time for fps calculation
                     :    end_time                ->    Ending time for fps calcualtion

         RETURNS     :    NONE

         PARAMETERS  :    fps                     ->    processing frames per second
    '''
    fps  =  1/np.round(end_time - start_time,2)
#     print(f"FPS : {fps}")

    cv2.putText(obj_detected_frame, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5 , (255,0,0), 3)
    cv2.imshow('Object Detection', obj_detected_frame)

    cv2.waitKey(1)