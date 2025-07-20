import cv2
import numpy
import os
from pyzbar.pyzbar import decode, Decoded
from typing import List
from PIL import Image
from io import BytesIO



def readFilePath(path:str):
    """Read one file with path and return the decoded value"""
    img = cv2.imread(path)
    value = decode (img)
    return value


def readFolder(path:str)-> List[Decoded]:
    """Read all the files in the folder and return the list of decoded values"""
    result:List[Decoded] = []
    for item in os.listdir(path):
        img = cv2.imread(f"{path}{item}")
        value = decode(img)
        barcode: Decoded
        for barcode in value:
            result.append(barcode)
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
