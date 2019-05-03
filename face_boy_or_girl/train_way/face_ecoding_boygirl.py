# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:12:41 2019

@author: Administrator
"""
import face_recognition
import cv2
import os
import numpy as np



#def get_standard_face_landmarks_list(img):
#    
#    
#    
#    face_landmarks_list = face_recognition.face_landmarks(img)
#    x=[]
#    y=[]
##    face_landmarks_list2=face_landmarks_list.copy()
#    (x0,y0)=face_landmarks_list[0]['nose_tip'][3]
#    face_landmarks = face_landmarks_list[0]
##    for face_landmarks in face_landmarks_list:
#    for facial_feature in face_landmarks.keys():
#        for pos in face_landmarks[facial_feature]:
#            x.append(pos[0]-x0)
#            y.append(pos[1]-y0)
#    xm=max([abs(xi) for xi in x])
#    xo=[xi/xm for xi in x]                        
#    ym=max([abs(yi) for yi in y])
#    yo=[yi/ym for yi in y]             
##    return [xo,yo]
#    return xo+yo

#############################
#imgdir='tvb'
#imgdir_face=imgdir+'boy'
imgdir_face='boy'
imglist=os.listdir(imgdir_face)

nors=[]
for i,img in enumerate(imglist):
    img_temp=cv2.imread(imgdir_face+'/'+img)
    try:
        print(i)
        face_locations = face_recognition.face_locations(img_temp)
        face_encodings = face_recognition.face_encodings(img_temp, face_locations)[0]
        nors.append(face_encodings)
    except:
        continue

##############################
#imgdir2='tvb'
#imgdir2_face=imgdir2+'girl'
imgdir2_face='girl'   
imglist2=os.listdir(imgdir2_face)

nors2=[]
for i,img in enumerate(imglist2):
    img_temp=cv2.imread(imgdir2_face+'/'+img)
    try:
        print(i)
        face_locations = face_recognition.face_locations(img_temp)
        face_encodings = face_recognition.face_encodings(img_temp, face_locations)[0]
        nors2.append(face_encodings)
    except:
        continue
##########################
#nors2_np=np.array(nors2)
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.decomposition import PCA           #加载PCA算法包


train_l=300 #train data length
train_x=nors[:train_l]+nors2[:train_l]
train_y=train_l*[1]+train_l*[0]
test_x=nors[train_l:]+nors2[train_l:]
real_y=len(nors[train_l:])*[1]+len(nors2[train_l:])*[0]

#clf = SVC(gamma='auto')
#clf.fit(train_x, train_y) 
#pca=PCA(n_components=20)     #加载PCA算法，设置降维后主成分数目为2
#reduced_x=pca.fit_transform(train_x)#对样本进行降维
#clf = KNeighborsClassifier(15)
clf = SVC(gamma='auto')
clf.fit(train_x,train_y)



pre_y=clf.predict(test_x)

np.mean(np.equal(real_y,pre_y))

from sklearn.externals import joblib
joblib.dump(clf,'filename3.pkl')  #保存模型

#from sklearn.externals import joblib  #之后可以用这两行提取模型
#clf=joblib.load('filename.pkl')


