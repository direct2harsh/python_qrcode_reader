import cv2
import numpy
import os
from pyzbar.pyzbar import decode, Decoded
from typing import List


def readFile(path:str):
    img = cv2.imread(path)
    value = decode (img)
    return value


def readFolder(path:str)-> List:
    result = []
    for item in os.listdir(path):
        img = cv2.imread(f"{path}{item}")
        value = decode(img)
        barcode: Decoded
        for barcode in value:
            result.append(barcode)
    return result
