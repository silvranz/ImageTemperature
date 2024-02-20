import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

acceptedFile = (".jpg",".jpeg",".png")

def AdjustmentValueValidation(valueString):
    try:
        valueInt = int(valueString)
        return True
    except ValueError:
        return False

def OutputFileValidation(filePath):
    if not os.path.exists(filePath) and os.path.isdir(filePath):
        print("Folder not found")
        return False
    return True

def InputFileValidation(filePath):
    if not filePath.endswith(acceptedFile):
        print("We only accept ",acceptedFile,"file")
        return False
    
    if not os.path.isfile(filePath):
        print("File not found")
        return False
    
    return True

def Main():
    inputPath = ""
    while True:
        inputPath = input("Enter input file path:")
        if InputFileValidation(inputPath):
            break
    
    fileName = os.path.basename(inputPath)

    outputPath = ""
    while True:
        outputPath = input("Enter output file path:")
        if OutputFileValidation(outputPath):
            break

    outputFileName = ""
    if not os.path.exists(outputPath) or os.path.isfile(outputPath):
        outputFileName = outputPath
    else:
        outputFileName = os.path.join(outputPath, fileName)
    
    inputImage = cv2.imread(inputPath, cv2.IMREAD_COLOR)
    assert inputImage is not None, "file could not be read"
    
    adjustmentValue = 0
    while True:
        adjustmentValue = input("Enter adjustment temperature:")
        if AdjustmentValueValidation(adjustmentValue):
            break
    
    adjustmentValueInt = int(adjustmentValue)
    outputImage = np.ndarray(shape=np.shape(inputImage))
    for y,col in enumerate(inputImage):
        for x,val in enumerate(col):
            tempNewVal = val+[-adjustmentValueInt,0,adjustmentValueInt]

            if tempNewVal[0] > 255: 
                tempNewVal[0] = 255
            elif tempNewVal[0] < 0: 
                tempNewVal[0] = 0

            if tempNewVal[2] > 255: 
                tempNewVal[2] = 255
            elif tempNewVal[2] < 0: 
                tempNewVal[2] = 0
            
            outputImage[y,x] = tempNewVal
            
    cv2.imwrite(outputFileName,outputImage)
    print("Output image :",outputFileName)

if __name__ == "__main__":
    Main() 