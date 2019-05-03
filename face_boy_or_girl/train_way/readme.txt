检测人脸并识别性别

1 运行getimg_from_request.py爬取女演员图到girl文件夹； 爬取男演员图到boy文件夹。另外关键词可更改。
之后要到girl删除有男脸成分的图片；boy类似。

2 运行face_ecoding_boygirl.py 分别将boy和girl脸提取出来，生成128特征向量，然后用SVM训练，生成 .pkl模型文件


