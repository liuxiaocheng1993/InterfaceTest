#coding:utf-8
'''
Created on 2019��3��29��

@author: Administrator
'''
import requests

import json

class cookies:
    
    def __init__(self,username=None,password=None):
        
        self.username=username
        self.password=password
        self.url="http://mall.api.epet.com/v3/login.html"
        if username==None:
            self.cookies=self.getdefualtcookies()
        else:
            self.cookies=self.getcookies()   
        
        
        
    def getdefualtcookies(self):
        data={"do":"postSubmit","postsubmit":"r9b8s7m4",
              "username":"刘小成","password":"123456lxc",
              "system":"wap","isWeb":1,"version":303}
        
        re=requests.post(url=self.url,data=data)
        
        cookis=requests.utils.dict_from_cookiejar(re.cookies)
        return cookis
    def getcookies(self):
        data={"do":"postSubmit","postsubmit":"r9b8s7m4",
              "username":self.username,"password":self.password,
              "system":"wap","isWeb":1,"version":303}
        
        re=requests.post(url=self.url,data=data)
        
        cookis=requests.utils.dict_from_cookiejar(re.cookies)
        
        return cookis
    def savecookies(self):
        dick=json.dumps(self.cookies)
        file=open('../Config/logincookies.txt','w')
        file.write(dick)
        file.close()
    def readcookies(self):
        file = open('../Config/logincookies.txt', 'r') 
        js = file.read()
        dic = json.loads(js)   
         
        file.close() 
        #print(dic)
        return dic
        
if __name__=="__main__":
    test=cookies()
    test.getcookies() 
    test.savecookies() 
    test.readcookies()  