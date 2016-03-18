# -*- coding: utf-8 -*-
"""
Created on Sun May 03 21:37:47 2015

@author: Ashish Yadav
"""

import os
import Image

imageFile = "h.jpg"
im1 = Image.open(imageFile)

width = 200
height = 200

im2 = im1.resize((width, height), Image.ANTIALIAS)

im2.save("h_new.jpg");