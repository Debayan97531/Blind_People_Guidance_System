from itertools import count
import cv2
import numpy as np

def calculate_distance(box_coord, frame_2, name):
    ''' This function is directly called from the main.py file for estimation of monocular distance

        ARGS        :   frame_2            ->   bounding box implemented image frame
                    :   name               ->   Names of the objects present for a single frame type:str
                    :   box_coord          ->   Coordinate of the bounding boxes 2D array containing positions of all the bojects for a single frame

        RETURNS     :   frame_2            ->   image containing distances of corresponding objects shown on frame
                    :   DIST_H_per_FRAME   ->   Array containing the estimated distances using virtual horizon method, of corresponding objects
                    :   DIST_2_per_FRAME   ->   Array containing the estimated distances using another method, of corresponding objects(not accurate enough)

        PARAMETERS  :   cam_height         ->   height at ehich the camera is set
                    :   frame_x            ->   width of the imported image frame
                    :   frame_y            ->   height of the imported image frame
                    :   virtual_horizon    ->   position of the virtual horizon(height)
                    :   n_objects          ->   number of objects detected in a single image frame
                    :   DISTANCE_H         ->   Estimated distances of the objects using virtual horizon method in metre
                    :   DISTANCE_2         ->   Estimated distance of the objects using a different method in metre(less accuracy)
    '''

    DIST_H_per_FRAME    =   []
    DIST_2_per_FRAME    =   []
    box_coord_2 = []
    frame_x, frame_y    =   frame_2.shape[1], frame_2.shape[0]
    n_objects           =   len(box_coord)

    height_threshold = frame_y -  (frame_y//3)*2 + 50 # to ommit detection of birds and street lamps
    frame_2, virtual_horizon, cam_height =  estimate_virtual_horizon(box_coord, frame_x, frame_y, frame_2, height_threshold)
    for i in range(n_objects): 
        x1, y1, x2, y2        =  box_coord[i][0], box_coord[i][1], box_coord[i][2], box_coord[i][3]
        if (y2 > height_threshold):
            object_name           =  name[i]
            box_coord_2.append([x1, y1, x2, y2])    
            DISTANCE_H, frame_2   =  distance_from_horizon(virtual_horizon, x1, y1,y2, cam_height, object_name, frame_2)
            DIST_H_per_FRAME.append(DISTANCE_H)

            ''' CALL DISTANCE_H RATHER THAN DISTANCE_2 FOR MORE ACCURATE RESULT '''

            # DISTANCE_2, frame_2   =  distance_estimation_2(frame_y, x1, y1, y2, object_name,cam_height, frame_2)
            # DIST_2_per_FRAME.append(DISTANCE_2)
        

    return DIST_H_per_FRAME, DIST_2_per_FRAME, frame_2, box_coord_2


def estimate_virtual_horizon(box_coord, frame_x, frame_y, frame_2, height_threshold):
        veh_width   =  1.40     # average width of a vehicle in m
        cam_height  =  1.42     # height of the camera in m
        sum_w_b     =  0
        sum_w_y     =  0
        n           =  len(box_coord)
        obj_count   =  0   
        
        # height_threshold = frame_y -  (frame_y//3)*2 + 50
        #this loop is used to calculate the average heigth and width if the bounding boxes
        for i in range(n):
            x1, y1, x2, y2  =  box_coord[i][0], box_coord[i][1], box_coord[i][2], box_coord[i][3]
            if (y2 > height_threshold):      
                sum_w_b         += (x2 - x1)
                sum_w_y         += y2
                obj_count       +=1

        avg_w_y     =  sum_w_y/obj_count    # average height of the last line of the bounding box
        avg_w_b     =  sum_w_b/obj_count    # average width of the bounding boxes in image

        virtual_horizon     =  avg_w_y - ((cam_height*avg_w_b)/veh_width)
        cv2.line(frame_2,(0,int(virtual_horizon)), (frame_2.shape[1], int(virtual_horizon)), (255,0,0), 2)

        # print(f"average height : {avg_w_y} ")
        # cv2.imshow("Virtual horizon", frame_2)

        return frame_2, virtual_horizon, cam_height


def distance_from_horizon(virtual_horizon, x1, y1, y2, cam_height, object_name, frame_2):
    focal_length    =  718.856
    DISTANCE_H      =  (focal_length * cam_height)/float(y2- virtual_horizon)

    GREEN = (0,255,0)
    # cv2.putText(frame_2, str(np.round(DISTANCE_H,2)), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, GREEN, 2)

    # print(f'DISTANCE 2 for {object_name} : {DISTANCE_H} m')
    return DISTANCE_H, frame_2


def distance_estimation_2(frame_y, x1, y1, y2, object_name,cam_height, frame_2):
    # --------- Variable declaration --------- #
    CAM_HEIGHT      =  cam_height              # Height at which the camear is fixed in the vehicle (in m)
    IMAGE_HEIGHT    =  frame_y                 # Height of the image (in pixels)
    VIEW_ANGLE      =  82                      # camera view angle in degrees
    FIELD_OF_VIEW   =  60                      # camera field of view in degrees
    # --------- Variable declaration --------- #

    Dp              =  IMAGE_HEIGHT - y2
    VAR_A           =  np.tan(VIEW_ANGLE - (FIELD_OF_VIEW//2))
    INR_VAR_A       =  (IMAGE_HEIGHT//2 - Dp)
    INR_VAR_B       =  (IMAGE_HEIGHT/(2*(np.tan(FIELD_OF_VIEW//2))))
    VAR_B           =  np.arctan(INR_VAR_A/INR_VAR_B)
    DISTANCE_2      =  CAM_HEIGHT * (np.tan(VIEW_ANGLE + VAR_B) - VAR_A)
    
    GREEN = (0,255,0)
    # cv2.putText(frame_2, str(np.round(DISTANCE_2,2)), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, GREEN, 2)

    print(f'DISTANCE 1 for {object_name} : {DISTANCE_2} m')
    return DISTANCE_2, frame_2