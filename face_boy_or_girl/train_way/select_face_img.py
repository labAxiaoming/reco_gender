# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:04:43 2019

@author: Administrator
"""
import face_recognition
import cv2
import os


imgdir='girl'


imgdir_face=imgdir+'_face'

if imgdir_face not in os.listdir():
    os.mkdir(imgdir_face)
imglist=os.listdir(imgdir)
j=-1
for i,img in enumerate(imglist):
    try:
        img_temp=cv2.imread(imgdir+'/'+img)
        face_locations = face_recognition.face_locations(img_temp)
    
        if len(face_locations)==1:
            j+=1
            top,right,bottom,left=face_locations[0]
            img_face=img_temp[top:bottom,left:right,:]
            cv2.imwrite(imgdir_face+'/'+str(j)+'.jpg',img_face)
    except:
        continue

#            cv2.imwrite('E:/sk_py/request_img/'+imgdir_face+'/'+str(i)+'.jpg',img_face)



imgdir2='boy'
imgdir_face2=imgdir2+'_face'

if imgdir_face2 not in os.listdir():
    os.mkdir(imgdir_face2)
imglist2=os.listdir(imgdir2)
jj=-1
for j,img2 in enumerate(imglist2):
    try:
        img_temp2=cv2.imread(imgdir2+'/'+img2)
        face_locations2 = face_recognition.face_locations(img_temp2)
    
        if len(face_locations2)==1:
            jj+=1
            top,right,bottom,left=face_locations2[0]
            img_face2=img_temp2[top:bottom,left:right,:]
            cv2.imwrite(imgdir_face2+'/'+str(jj)+'.jpg',img_face2)
    except:
        continue