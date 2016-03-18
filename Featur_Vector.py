# -*- coding: utf-8 -*-
"""
Created on Fri May 08 14:37:32 2015

@author: Ashish Yadav
"""

import numpy as np
from PIL import Image

import os  


def main():
    train_path, train_dirs, train_files = os.walk("C:\Users\Ashish Yadav\Desktop\Folders\ALL\ML\ML_Project\Tree").next()
    train_count = len(train_files)
    print 'file_count'
    print train_count
    
    
    test_path, test_dirs, test_files = os.walk("C:\Users\Ashish Yadav\Desktop\Folders\ALL\ML\ML_Project\Test").next()
    test_count = len(test_files)
    
    
    trainSize=train_count
    testSize=test_count
    bigList=np.zeros((trainSize,3*300*300))
    bigListTest=np.zeros((testSize,3*300*300))
    count=0;
    testDir="skyTest"
    trainDir="skyTrain"
    y_train=np.zeros(trainSize)
    y_test=np.zeros(testSize)
    #../downloads/sky/no_sky/   
    for fn in os.listdir(trainDir):
        #print "in for"
	if os.path.isfile(trainDir+"/"+fn):
            #print (trainDir+"/"+fn)
            if(fn.endswith(".JPEG")):
                filename=trainDir+"/"+fn
		im=Image.open(filename);
                
                pix=im.load();
                #print im.size
                
                k=0;
                for i in range(0,300):
                    for j in range(0,300):
                        col=3*k
                        bigList[count,col]=(pix[i,j][0])
                        bigList[count,col+1]=(pix[i,j][1])
                        bigList[count,col+2]=(pix[i,j][2])
                        k=k+1;
                #print fn[4]
		#print fn[4]
                y_train[count]=fn[4]        
                #print y_train[count]                
                count=count+1

    count=0
    for fn in os.listdir(testDir):
        if os.path.isfile(testDir+"/"+fn):
            #print (fn)
            if(fn.endswith(".JPEG")):
                im=Image.open(testDir+"/"+fn);
                
                pix=im.load();
                #print im.size
                
                k=0;
                for i in range(0,300):
                    for j in range(0,300):
                        col=3*k
                        bigListTest[count,col]=(pix[i,j][0])
                        bigListTest[count,col+1]=(pix[i,j][1])
                        bigListTest[count,col+2]=(pix[i,j][2])
                        k=k+1;
                y_test[count]=fn[4]        
                #print y_test[count]
                count=count+1
    print "testList Size:",(bigListTest.shape)            
    ###################################
    
    
    
    X_train=bigList
    X_test=bigListTest
    
    
    train_file=np.asarray(X_train);
    np.savetxt("D:\Train_File.txt",train_file,delimiter=",",fmt='%s');
    
    test_file=np.asarray(X_test);
    np.savetxt("D:\Test_File.txt",test_file,delimiter=",",fmt='%s');    
    
    y_train_file=np.asarray(y_train);
    np.savetxt("D:\Train_File.txt",y_train_file,delimiter=",",fmt='%s');    
    
    
    print "done";
if __name__=="__main__":
    main()
