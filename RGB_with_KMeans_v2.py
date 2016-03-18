# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:35:12 2015

@author: Ashish Yadav


 Getting RGB values"""

import numpy as np
import collections
from PIL import Image
from sklearn.cluster import MiniBatchKMeans
from matplotlib import pyplot as plt





def add_value(L):
    n=len(L);
    sum=0;
    for i in range(0,n):
        sum=sum+L[i];
    
    return sum;
    

def main():
    im=Image.open("h.jpg");
    
    pix=im.load();
    print im.size
    
    
    w=im.size[0];
    h=im.size[1];
    
    lst = [];
    k=0;
    for i in range(0,w):
        for j in range(0,h):
            lst.append(pix[i,j]);
            k=k+1;
            #print pix[i,j]," ";
        #print "\n"
    
    
    #print lst
    
    n=len(lst)
    #print len(lst)
    #d={};
    
    
    arr = np.ones(n);
    
    
    arr_list = np.array(arr).tolist()
    
    #print arr_list;
    
    #pixels = np.array(pix).tolist()
    
    #print pixels;
    
    temp = collections.defaultdict(list)
    for p, ele in zip(lst, arr_list):
        temp[p].append(ele)
            
            
    #print temp;
    
    
    
    d={}
    s=0;
    for key,value in temp.iteritems():
        s=add_value(value)
        d[key]=s;
        
        
    #print d;
    
    
    
    
    d_list=[]    
    for key, value in d.iteritems():                
        tmp = [key,value]                
        d_list.append(tmp)
        
    d_pixel_list=[];
    
    for key in d.iteritems():
        temp2=[key];
        d_pixel_list.append(temp2);
        
    b=np.asarray(d_pixel_list);
    
    c=np.asarray(lst);

    X=np.zeros((len(lst),3));    
    for i in range (0, len(lst)):
        X[i,0]=lst[i][0];
        X[i,1]=lst[i][1];        
        X[i,2]=lst[i][2];
        
    
            
            
            
            #print 'd1_list'
            #print d1_list
        
    a=np.asarray(d_list);
            #print 'array'
            #print             

    print 'a';

    #print a;
    
    #print 'b';    
    
    print b;
    
    #print 'c';
    
    #print c;
    #np.savetxt("C:\Users\Ashish Yadav\Desktop\ALL\ML\ML_Project\File.txt",a,delimiter=",",fmt='%s');

    
    
    cluster = MiniBatchKMeans(n_clusters=2);
    
    y = cluster.fit_predict(lst);
    d2=cluster.cluster_centers_    ;
    print 'c_new';
    
    #print c;
    
    print 'y';
    
    #print y;
    print d2;
    
       
    #print 'cluster';
    
    #print cluster;

    result=np.zeros((len(y),3));        
    for i in range (0,len(y)):
        result[i,:]=d2[y[i]];
        
    print result;
    
    
    image_matrix=np.zeros((h,w,3));
    k=0;
    print w,h;

    for j in range(0,w):
        for i in range(0,h):
        
            image_matrix[i,j,0]=round(result[k][0]);
            image_matrix[i,j,1]=round(result[k][1]);
            image_matrix[i,j,2]=round(result[k][2]);            
            k=k+1;
        

    np.savetxt("Cluster.txt",image_matrix,delimiter=",",fmt='%s');  
    
    img = Image.fromarray(image_matrix, 'RGB')
    img.save('r.png')
    plt.imshow(image_matrix, interpolation='nearest')
    plt.show()
    print d2;
    print "done";
if __name__=="__main__":
    main()