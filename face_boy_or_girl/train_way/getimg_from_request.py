# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:14:43 2019

@author: Administrator
"""
import os
import re #导入正则表达式模块
import requests #python HTTP客户端 编写爬虫和测试服务器经常用到的模块
import time 
#定义函数方法

def spiderPic(html,keyword,savedir):
    i=0
    print('正在查找 ' + keyword +' 对应的图片,下载中，请稍后......')
    for addr in re.findall('"objURL":"(.*?)"',html,re.S):     #查找URL
        print('正在爬取URL地址：'+str(addr)[0:30]+'...')  #爬取的地址长度超过30时，用'...'代替后面的内容
        
        try:
            pics = requests.get(addr,timeout=100)  #请求URL时间（最大3秒）
        except requests.exceptions.ConnectionError:
            print('您当前请求的URL地址出现错误')
            continue
 
#        fq = open('D:\\img\\' + (keyword+'_'+str(random.randrange(0,1000,4))+'.jpg'),'wb')     #下载图片，并保存和命名
        if savedir not in os.listdir():
            os.mkdir(savedir)
        fq = open(savedir+'/'+str(time.time()).split('.')[0]+str(i)+'.jpg','wb')
        i+=1
        fq.write(pics.content)
        fq.close()
 
#python的主方法
if __name__ == '__main__':
    word ,dir= 'TVB女演员图片','girl'  #   爬取女脸 保存到 girl/文件夹
    word2 ,dir2= 'TVB男演员图片','boy'  #   爬取男脸 保存到 boy/文件夹 
    pageId=0
#    result = requests.get('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + word)
    result=requests.get('http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + "&pn="+str(pageId)+"&gsm=?&ct=&ic=0&lm=-1&width=0&height=0")
    result2=requests.get('http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word2 + "&pn="+str(pageId)+"&gsm=?&ct=&ic=0&lm=-1&width=0&height=0")

	#调用函数
for pageId in range(10):
    spiderPic(result.text,word,dir)
    spiderPic(result2.text,word2,dir2)
#    pageId+=10
#--------------------- 
#参考    
    #作者：符智生 
    #来源：CSDN 
    #原文：https://blog.csdn.net/csdn_fzs/article/details/79028705 
