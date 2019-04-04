#coding:utf-8
'''
Created on 2019年3月18日

@author: Administrator
'''
import json
class OperationJson(object):
    def __init__(self,file_name=None):
        if file_name:
            self.file_name=file_name
            self.data=self.ReadJson()
        else:
            file_name=""
            self.data=self.ReadJson()
    #根据路径读取json值
    def ReadJson(self):
        with open(self.file_name) as fp:
            data=json.load(fp)
            return data
    #根据关键字，获取数据
    def get_data(self,key):
         return self.data[key]   
    
if __name__=="__main__":
    demo=OperationJson()
            
