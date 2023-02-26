from turtle import distance
import cv2

def ego_roi(frame_2, name, box_coord, DIST_H_per_FRAME):
    
    x_rec_mid = int(frame_2.shape[1]/2)
    y_rec_mid = int(frame_2.shape[0]/2)
    x_rec_pad = 200
    y_rec_pad = 150

    y_lane_pad      = 200
    x_lane_mid      = int(frame_2.shape[1]/2)
    y_lane_third    = int((frame_2.shape[0]/3)*2)
    x_lane_pad_up   = 75 
    x_lane_pad_down = 500 

    frame_2 = cv2.rectangle(frame_2,(x_rec_mid-x_rec_pad, y_rec_mid - y_rec_pad+50 ), (x_rec_mid + x_rec_pad ,y_rec_mid + y_rec_pad+50 ), (255,0,0), 3)

    #line left bottom
    frame_2 = cv2.line(frame_2,(x_lane_mid - x_lane_pad_down, y_lane_third + y_lane_pad), (x_lane_mid - x_lane_pad_up, y_lane_third), (0,255,0), 3)
    #line right bottom
    frame_2 = cv2.line(frame_2,(x_lane_mid + x_lane_pad_down, y_lane_third + y_lane_pad), (x_lane_mid + x_lane_pad_up, y_lane_third), (0,255,0), 3)
    #line upper
    frame_2 = cv2.line(frame_2,(x_lane_mid - x_lane_pad_up, y_lane_third), (x_lane_mid + x_lane_pad_up, y_lane_third), (0,255,0), 3)

    x_1_low = x_lane_mid    -   x_lane_pad_up - 50
    x_2_low = x_lane_mid    +   x_lane_pad_up + 50
    y_up    = y_lane_third  
    y_low   = y_lane_third  +   y_lane_pad

    frame_2, coords_in_roi, distance_in_roi =  object_in_roi(frame_2, name, box_coord, x_1_low, x_2_low, y_up, y_low, DIST_H_per_FRAME)

    coords_in_roi = box_coord
    distance_in_roi = DIST_H_per_FRAME
    
    return frame_2, coords_in_roi, distance_in_roi

def object_in_roi(frame_2, name, box_coord, x_1_low, x_2_low, y_up, y_low, DIST_H_per_FRAME):
    coords_in_roi = []
    distance_in_roi = []
    length = len(box_coord)
    for i in range(length):
        obj_x_centre = (box_coord[i][0] + box_coord[i][2]) // 2
        obj_y_centre = (box_coord[i][1] + box_coord[i][3]) // 2
        cv2.circle(frame_2,(obj_x_centre, obj_y_centre), 8, (0,0,0), -1)

        if (((obj_x_centre >= x_1_low) and (obj_x_centre <= x_2_low)) and (obj_y_centre >= y_up) and (len(DIST_H_per_FRAME) !=0)):
            # coord_pos = [box_coord[i][0], box_coord[i][1], box_coord[i][2], box_coord[i][3]]
            print("ok[!]")
            coords_in_roi.append(box_coord[i])
            distance_in_roi.append(DIST_H_per_FRAME[i])
            YELLOW = (0,255,255)
            cv2.rectangle(frame_2, (box_coord[i][0] , box_coord[i][1]), (box_coord[i][2], box_coord[i][3]), YELLOW, 3)
        else:
            GREEN = (0,255,0)
            cv2.rectangle(frame_2, (box_coord[i][0] , box_coord[i][1]), (box_coord[i][2], box_coord[i][3]), GREEN, 3)
    # print(distance_in_roi)
    return frame_2, coords_in_roi, distance_in_roi

