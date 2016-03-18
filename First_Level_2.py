# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:17:19 2015

@author: Ashish Yadav
"""

import numpy as np
from PIL import Image
import os  
from sklearn import svm
from sklearn.externals import joblib


def fun(l):
    le=len(l)
    for i in range(0,le):
        if l[i]!='1' and l[i]!='0':
            return 0;

    return 1;

def main():
    test_path, test_dirs, test_files = os.walk("Level_One_Images").next()
    test_count = len(test_files)
    testSize=1#test_count
    bigListTest=np.zeros((testSize,3*300*300))
    count=0;
    testDir="Level_One_Images"
    y_test=np.zeros(testSize)
    
    name=""

    clf_road = joblib.load("Model_Road\model_road");
    clf_ocean = joblib.load("Model_Ocean\model_ocean");
    clf_building = joblib.load("Model_Building\model_building");
    #clf_mountain = joblib.load("Model_Mountain\model_mountain");
    clf_tree = joblib.load("Model_Tree\model_sky");
    clf_sand = joblib.load("Model_Sand\model_sand");
    clf_sky = joblib.load("Model_Sky\model_sky");
    clf_people = joblib.load("Model_People\model_sky");
    clf_snow = joblib.load("Model_Snow\model_snow");
    clf_rock = joblib.load("Model_Rock\model_rock");
    print "going for second for"
    count=0
    for fn in os.listdir(testDir):
        name="";
        bigListTest=np.zeros((testSize,3*300*300))
            
        name=fn
        
            
        if os.path.isfile(testDir+"/"+fn):
            #print (fn)
            if(fn.endswith(".JPEG")):
                #name="";                
                print 'rishabh'
                im=Image.open(testDir+"/"+fn);
                
                pix=im.load();
                #print im.size
                
                
                print 'name'
                print fn                
                k=0;
                for i in range(0,300):
                    for j in range(0,300):
                        col=3*k
                        bigListTest[count,col]=(pix[i,j][0])
                        bigListTest[count,col+1]=(pix[i,j][1])
                        bigListTest[count,col+2]=(pix[i,j][2])
                        k=k+1;
                #y_test[count]=float(fn[0])        
                #print y_test[count]
                #count=count+1
                print "testList Size:",(bigListTest.shape)            
     
    
                X_test=bigListTest
                
                
                
                
                
                dec = clf_tree.decision_function(X_test)        
                print y_test
                print np.sign(dec)
    
  
	 
                y_out=np.zeros(len(dec))
                print len(dec),len(y_test)    
                for i in range(0,len(dec)):
                    if(dec[i]>0):
                        y_out[i]=1
                        name="1"+name;
                    else:
                        name="0"+name;
                
                
                
                
                
                
                dec = clf_road.decision_function(X_test)        
                print y_test
                print np.sign(dec)
    
 
	 
                y_out=np.zeros(len(dec))
                print len(dec),len(y_test)    
                for i in range(0,len(dec)):
                    if(dec[i]>0):
                        y_out[i]=1
                        name="1"+name;
                    else:
                        name="0"+name;        
                
                
                
                
                
                dec = clf_people.decision_function(X_test)        
                print y_test
                print np.sign(dec)
    
 
	 
                y_out=np.zeros(len(dec))
                print len(dec),len(y_test)    
                for i in range(0,len(dec)):
                    if(dec[i]>0):
                        y_out[i]=1
                        name="1"+name;
                    else:
                        name="0"+name;
                        
                        
                        
                        
                        
                dec = clf_snow.decision_function(X_test)        
                print y_test
                print np.sign(dec)
    
 
	 
                y_out=np.zeros(len(dec))
                print len(dec),len(y_test)    
                for i in range(0,len(dec)):
                    if(dec[i]>0):
                        y_out[i]=1
                        name="1"+name;
                    else:
                        name="0"+name;
                
                
                
                
                dec = clf_ocean.decision_function(X_test)        
                print y_test
                print np.sign(dec)
    
 
	 
                y_out=np.zeros(len(dec))
                print len(dec),len(y_test)    
                for i in range(0,len(dec)):
                    if(dec[i]>0):
                        y_out[i]=1
                        name="1"+name;
                    else:
                        name="0"+name;
            
            
            
                
                 
    
                
                        
                        
                  
                
                """     
                 
                dec = clf_mountain.decision_function(X_test)        
                print y_test
                print np.sign(dec)
    
 
	 
                y_out=np.zeros(len(dec))
                print len(dec),len(y_test)    
                for i in range(0,len(dec)):
                    if(dec[i]>0):
                        print 'M'
                        y_out[i]=1
                        name=name+"1";
                    else:
                        name=name+"0";
                        
                        
                      
                
                """  
                dec = clf_sand.decision_function(X_test)        
                print y_test
                print np.sign(dec)
    
 
	 
                y_out=np.zeros(len(dec))
                print len(dec),len(y_test)    
                for i in range(0,len(dec)):
                    if(dec[i]>0):
                        y_out[i]=1
                        name="1"+name;
                    else:
                        name="0"+name;
                    
                dec = clf_sky.decision_function(X_test)        
                print y_test
                print np.sign(dec)
    
 
	 
                y_out=np.zeros(len(dec))
                print len(dec),len(y_test)    
                for i in range(0,len(dec)):
                    if(dec[i]>0):
                        y_out[i]=1
                        name="1"+name;
                    else:
                        name="0"+name;
                     
                     
                
                        
                        
                   
                dec = clf_rock.decision_function(X_test)        
                print y_test
                print np.sign(dec)
    
 
	 
                y_out=np.zeros(len(dec))
                print len(dec),len(y_test)    
                for i in range(0,len(dec)):
                    if(dec[i]>0):
                        y_out[i]=1
                        name="1"+name;
                    else:
                        name="0"+name;
                
                
                
                
                dec = clf_building.decision_function(X_test)        
                print y_test
                print np.sign(dec)
    
 
	 
                y_out=np.zeros(len(dec))
                print len(dec),len(y_test)    
                for i in range(0,len(dec)):
                    if(dec[i]>0):
                        y_out[i]=1
                        name="1"+name;
                    else:
                        name="0"+name;
                        
                
                im1 = im;
                print name
                im1.save("Final_Images\\" + name + ".JPEG")
                name=""




    
    
    print "done";
    
    
    
    
if __name__=="__main__":
    main()