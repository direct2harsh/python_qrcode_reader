import cv2
import numpy as np
import os
from pyzbar.pyzbar import decode, Decoded
from typing import List
import time




def capture(cameraId:int):
    cam = cv2.VideoCapture(cameraId)
    cam.set(3,480)
    cam.set(4,640)
    last_yield_time = 0.0

    while True:
        success, img = cam.read()
        item:Decoded
        current_time = time.time()
        
        if  current_time - last_yield_time >= 2:
            decoded_objects = decode(img)
            last_yield_time = current_time
            for item in decoded_objects:  
                data = item.data.decode("utf-8")
                print(data)            
                pts = np.array([item.polygon],np.int32)         
                cv2.polylines(img, [pts],True,(255,0,255),2)
                cv2.putText(img,data,(item.rect[0],item.rect[1]-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
                # yield data
        cv2.imshow("Result",img)
        print("waiting")
        cv2.waitKey(100)


def captureStream(url:str):
    cam = cv2.VideoCapture(url)
    cam.set(3,1080)
    cam.set(4,1920)
    last_yield_time = 0.0

    while True:
        success, img = cam.read()
        item:Decoded
        current_time = time.time()        
        if current_time - last_yield_time >= 2:
            decoded_objects = decode(img)
            last_yield_time = current_time
            item:Decoded
            for item in decoded_objects:  
                data = item.data.decode("utf-8")
                print(data)            
                pts = np.array([item.polygon],np.int32)         
                cv2.polylines(img, [pts],True,(255,0,255),2)
                cv2.putText(img,data,(item.rect[0],item.rect[1]-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
                yield data
        cv2.imshow("Result",img)
        print("waiting")
        cv2.waitKey(100)




    
        

