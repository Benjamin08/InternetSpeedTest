'''
Created on Jun. 15, 2021

@author: RFLXc
'''

from datetime import date
from _datetime import datetime

import speedtest  
  
  
st = speedtest.Speedtest()


def WriteDataToMasterList(dateToWrite, downSpeed, upSpeed):
    fileName = 'C:\\Users\\RFLXc\\new workspace\\InternetSpeedTest\\Data\\Test.txt'
    
    dataFile = open(fileName,"a")
    dataFile.write("\n")
    dataFile.write("date: " + dateToWrite)
    dataFile.write("\n")
    dataFile.write("our downspeed: " + downSpeed + " mbps")
    dataFile.write("\n")
    dataFile.write("our upspeed: " + upSpeed + " mbps")
    dataFile.write("\n")
    dataFile.close()
    

def FormateSpeedData():
    
    functionDownloadSpeed = st.download()
    functionUploadSpeed = st.upload()
    readingTime = datetime.now()
    
    functionDownloadSpeed = functionDownloadSpeed / 1000000
    functionUploadSpeed = functionUploadSpeed / 1000000
    
    print(readingTime)
    print('Our download speed is: ', round(functionDownloadSpeed,2))
    print('Our upload speed is: ', round(functionUploadSpeed,2))
    
    stringTime = str(readingTime)
    stringDown = str(round(functionDownloadSpeed,2))
    stringUp = str(round(functionUploadSpeed,2))
    
    WriteDataToMasterList(stringTime,stringDown, stringUp)
    
    
FormateSpeedData()
