#Joe Santantonio
#6/25/2020

import os
import shutil

start = r'\\server_ip\tributary\IDE\STOLTSpottingOutput'   #Source
copy = r'\\server_ip\tributary\IDE\History'                #History  
finish = r'\\server_ip\Shared\EDI\EDIQue\STOLT\pdf_out'    #Destination

for filename in os.listdir(start):
    if filename.endswith(".pdf"):

        #RENAME NO LONGER NECESSARY
        #Rename File -- Remove underscore
        #print("New name: "+filename.replace('_','')) [[debugging]]
        #newname = filename.replace('_','')
        #os.rename(os.path.join(source,filename), os.path.join(source,newname))

        #Move file shutil.move(source,destination)
        shutil.copy(os.path.join(start, filename), copy) 
        shutil.move(os.path.join(start, filename), finish)     
        continue
    else:
        continue
