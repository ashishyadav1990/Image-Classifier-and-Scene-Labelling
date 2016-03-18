# -*- coding: utf-8 -*-
"""
Created on Sun May 03 11:11:20 2015

@author: Ashish Yadav
"""

#Finding Color name for a pixel


import numpy as np
import collections
from PIL import Image
from sklearn.cluster import MiniBatchKMeans
from matplotlib import pyplot as plt


def max1(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    elif(c>=a and c>=b):
        return c


def min1(a,b,c):
    if(a<=b and a<=c):
        return a
    elif(b<=a and b<=c):
        return b
    elif(c<=a and c<=b):
        return c



def main():
    #Reduce_Img_Size();          # Reduce Size of the Image
    for j in range(1,101):
        im=Image.open("Tree_BaseLine/_ (" + str(j) + ").JPEG");
        
        pix=im.load();
        #print im.size
        
        
        w=im.size[0];
        h=im.size[1];
        print w,h;
        
        lst = [];
        k=0;
        for i in range(0,w):
            for j in range(0,h):
                lst.append(pix[i,j]);
                k=k+1;
                #print pix[i,j]," ";
            #print "\n"
        
        
        #print lst
        
        
        
        color_num={"Black" : 0, "White" : 0, "Grey" : 0, "Red" : 0,
                   "Orange" : 0, "Yellow" : 0, "Green" : 0, "Blue" : 0,
                   "Pink" : 0, "Brown" : 0, "Skin" : 0}    
        color_list=[];
                   
        color_name = [];
        color_name.append("Red");
        color_name.append("Orange");
        color_name.append("Yellow");
        color_name.append("Green");
        color_name.append("Green");
        color_name.append("Green");
        color_name.append("Blue");
        color_name.append("Blue");
        color_name.append("Blue");
        color_name.append("Blue");
        color_name.append("Pink");
        color_name.append("Pink");
        color_name.append("Red");
        
        color = ''    
        
        
    
    
        Hue_arr = np.ones(13);
        Hue_arr[0]= 0; 
        for i in range(1,13):
            Hue_arr[i] = Hue_arr[i-1]+30;
            
            
            
        
        #lst_len=len(lst);
        #print 'length of list'
        #print lst_len
        
        
        for i in range(0,w):
            for j in range(0,h):
                pixel=pix[i,j];
                
                #print pixel;
                r=pixel[0];
                g=pixel[1];
                b=pixel[2];
                
                r_d=0.00;
                g_d=0.00;
                b_d=0.00;    
                
                r_d = r/255.0;
                g_d = g/255.0;
                b_d = b/255.0;
                
                Cmax=max(r_d,g_d,b_d);
                
                Cmin=min(r_d,g_d,b_d);
                
                #print 'Cmax'
                #print Cmax
                
                #print 'Cmin'
                #print Cmin    
                
                diff = (Cmax-Cmin);
                
                
                #print 'diff'
                #print diff
                
                if diff==0.0:
                    H_d=0.0;
                
                elif Cmax==r_d:
                    H_d = ((g_d -b_d)/diff)%6;
            
                elif Cmax==g_d:
                    H_d = ((b_d -r_d)/diff) + 2;
            
                elif Cmax==b_d:
                    H_d = ((r_d -g_d)/diff) + 4;
                    
                #print 'H_d'
                #print H_d
                    
                H=60*H_d;
                
                #print 'H'
                #print H
                
                H=round(H)%360;
                #Cmax=Cmax/255;
                #Cmin=Cmin/255;
                
                
                L = (Cmax + Cmin)/2.0;
                
                
                #print 'L'
                #print L
                
                if diff==0.0:
                    Sat=0.0
                else:
                    Sat = diff/(1-abs(2*L-1))
                
                
                
                #print 'Sat'
                #print Sat
                
                
                
                
                
                
                
                index=0;
                for i in range(0,13):
                    if H <= Hue_arr[i]:
                        index=i;
                        break;
                        
            
                #print 'index'
                #print index
            
                                  
                        
                H1 = abs(H - Hue_arr[(index-1)]);
                H2 = abs(H - Hue_arr[(index)])
                
                
                #print 'H1'
                #print H1
            
                #print 'H2'
                #print H2    
                
                
                
                #print H
                #print Sat
                #print L            
                
                
                if L>=0.0 and L<=0.015:
                    color = 'Black'
                elif L>=0.90 and L<=1.0:
                    color ='White'
                elif Sat>=0.0 and Sat<=0.015:
                    color ='Grey'    
                elif H >=15 and H<=30 and Sat>=0.15 and Sat<=1.0 and L>=0.40 and L<=0.90:
                    color='Skin'
                elif H >=5 and H<=40 and Sat>=0.15 and Sat<=1.0 and L>=0.15 and L<=0.40:
                    color='Brown'
                elif H1<H2:
                    #print 'Color_Name';
                    color =color_name[index-1];
                elif H1>=H2:
                    #print 'Color_Name';
                    color =color_name[(index)];    
                
                color_num[color] = color_num[color]+1
                #print color;
                
                
                
        
        color_list.append(color_num["Black"])
        color_list.append(color_num["White"]);
        color_list.append(color_num["Grey"]);
        color_list.append(color_num["Red"]);
        color_list.append(color_num["Orange"]);
        color_list.append(color_num["Yellow"]);
        color_list.append(color_num["Green"]);
        color_list.append(color_num["Blue"]);
        color_list.append(color_num["Pink"]);
        color_list.append(color_num["Brown"]);
        color_list.append(color_num["Skin"]);
        
        
        a=np.asarray(color_list);
                
        np.savetxt(str(j) + ".csv",a,delimiter=",",fmt='%s');
        print color_num
    
    
    
    
    
    
if __name__=="__main__":
    main()