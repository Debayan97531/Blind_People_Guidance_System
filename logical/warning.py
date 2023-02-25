import cv2
import numpy as np

def collision_warning(coords_in_roi,distance_in_roi, frame_3_roi):
    for i in range(len(coords_in_roi)):
        if (distance_in_roi[i] < 3):
            # x1 = coords_in_roi[0]
            # y1 = coords_in_roi[1]
            RED = (0,0,255)
            cv2.putText(frame_3_roi, str(np.round(distance_in_roi[i],2)), (coords_in_roi[i][0] , coords_in_roi[i][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, RED, 4)
            cv2.putText(frame_3_roi, "COLLISION DETECTION", (80, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.9, RED, 4)
            cv2.rectangle(frame_3_roi, (coords_in_roi[i][0] , coords_in_roi[i][1]), (coords_in_roi[i][2], coords_in_roi[i][3]), RED, 3)

            print("##########################################")
            print("#          !! ... WARNING ... !!         #")
            print("##########################################")