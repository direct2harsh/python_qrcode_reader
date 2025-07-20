from fastapi import APIRouter, UploadFile,  File
import read
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import Decoded
from typing import List


router = APIRouter(prefix="/api",tags=["Read Barcode"])


@router.get("/filepath", description="If you want to decode file locally")
def read_file(path:str):
    data = read.readFilePath(path)
    return data[0].data.decode("utf-8")


@router.get("/folderpath", description="If you want to decode folder locally")
def read_folder(path:str):
    data:List[Decoded] = read.readFolder(path)
    results:List[str] =[]
    for item in data:
        results.append(item.data.decode("utf-8"))
    return results

@router.post("/fileupload",description="Upload a file and get all the barcode values as list")
async def decode_file(file:UploadFile = File(...)):
    content = await file.read()
    data:List[Decoded] = read.readFile(content=content)
    results:List[str] =[]
    for item in data:
        results.append(item.data.decode("utf-8")) 
    return results