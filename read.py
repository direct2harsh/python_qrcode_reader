import cv2
import numpy as np
import os
from pyzbar.pyzbar import decode, Decoded
from typing import List
from PIL import Image
from io import BytesIO
from kraken import binarization




def readFilePath(path:str):
    """Read one file with path and return the decoded value"""
    img = cv2.imread(path)
    value = decode (img)
    return value


def readFolder(path:str)-> List[Decoded]:
    """Read all the files in the folder and return the list of decoded values"""
    result:List[Decoded] = []
    for item in os.listdir(path):
        img = cv2.imread(f"{path}/{item}")


        # Enable below code to try the sharpen kernal 
        sharpen_kernel = np.array([
                    [0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]
                ])
        sharpen = cv2.filter2D(img, -1, sharpen_kernel)


        # To enable median blur
        # cv2.medianBlur(img,5)


        # To try threshold
        ret, bw_im = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
   
        value = decode(bw_im)
        barcode: Decoded
        for barcode in value:
            result.append(barcode)
            data = barcode.data.decode("utf-8")
            print(data)
            pts = np.array([barcode.polygon],np.int32)     
            cv2.polylines(bw_im, [pts],True,(255,0,255),2)
            cv2.putText(bw_im,data,(barcode.rect[0],barcode.rect[1]-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2) 
        cv2.imshow("Result",bw_im)
        cv2.waitKey(5000)
    return result


def readFile(content: bytes)-> List[Decoded]:
    """Read one file with path and return the decoded value"""
    result: List[Decoded]  = []
    image = Image.open(BytesIO(content))    
    value = decode (image)
    barcode: Decoded
    for barcode in value:
        result.append(barcode)
    return result



def readFolderKraken(path:str)-> List[Decoded]:
    """Read all the files in the folder and return the list of decoded values"""
    result:List[Decoded] = []
    for item in os.listdir(path):        
        im = Image.open(f"{path}/{item}")
        bw_im = binarization.nlbin(im)


        # Save the file on disk        
        bw_im.save("/home/harshvardhan/Documents/Hobbies/computer vision/barcode_reader/output.jpg")
        img = cv2.imread("/home/harshvardhan/Documents/Hobbies/computer vision/barcode_reader/output.jpg")

        # Try medianBlur
        cv2.medianBlur(img,5)
        # sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen_kernel = np.array([
                            [0, -1, 0],
                            [-1, 5, -1],
                            [0, -1, 0]
                        ])
        sharpen = cv2.filter2D(img, -1, sharpen_kernel)
        
        value = decode(bw_im)
        barcode: Decoded
        for barcode in value:
            result.append(barcode)
            data = barcode.data.decode("utf-8")
            print(data)
            pts = np.array([barcode.polygon],np.int32)     
            cv2.polylines(img, [pts],True,(255,0,255),2)
            cv2.putText(img,data,(barcode.rect[0],barcode.rect[1]-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2) 
        cv2.imshow("Result",img)
        cv2.waitKey(5000)
    return result

