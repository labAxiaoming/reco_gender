# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:57:01 2019

@author: Administrator
"""
import face_recognition
import cv2
#import os
import numpy as np



def get_standard_face_landmarks_list(img):
    face_landmarks_list = face_recognition.face_landmarks(img)
    x=[]
    y=[]
#    face_landmarks_list2=face_landmarks_list.copy()
    (x0,y0)=face_landmarks_list[0]['nose_tip'][3]
    face_landmarks = face_landmarks_list[0]
#    for face_landmarks in face_landmarks_list:
    for facial_feature in face_landmarks.keys():
        for pos in face_landmarks[facial_feature]:
            x.append(pos[0]-x0)
            y.append(pos[1]-y0)
    xm=max([abs(xi) for xi in x])
    xo=[xi/xm for xi in x]                        
    ym=max([abs(yi) for yi in y])
    yo=[yi/ym for yi in y]             
#    return [xo,yo]
    return xo+yo

from sklearn.externals import joblib
#joblib.dump(clf,'filename.pkl') #save
#clf=joblib.load('filename.pkl')  #load
clf=joblib.load('filename2.pkl')  #load


cap=cv2.VideoCapture(0)
process=True
Gender=''#初始化
top, right, bottom, left=1,1,1,1#初始化
boy_girls=[0,0]
while True:
    ret,img0=cap.read()
#    img.shape[0]
    if ret==1:
        img=cv2.resize(img0,(int(img0.shape[1]/4),int(img0.shape[0]/4)))
        if process:
#            try:
#                test_img=get_standard_face_landmarks_list(img)
                
#                boy_girl=clf.predict([test_img])
            face_locations = face_recognition.face_locations(img)
            face_encodings = face_recognition.face_encodings(img, face_locations)
            if len(face_locations)>0:
                boy_girls=clf.predict(face_encodings)
                
#                if boy_girl==1:
#                    Gender='boy'
#                else:
#                    Gender='girl'
#            except:
#                1+1
#            face_locations = face_recognition.face_locations(img)
        for (top, right, bottom, left), boy_girl in zip(face_locations,boy_girls):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            if boy_girl==1:
                Gender='boy'
            else:
                Gender='girl'
#        else:
#            1+1
                # Draw a box around the face
            cv2.rectangle(img0, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(img0, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img0, Gender, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        process=not process
#        Gender=''#初始化
#        top, right, bottom, left=1,1,1,1#初始化
        cv2.imshow('img',img0)   
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()  




