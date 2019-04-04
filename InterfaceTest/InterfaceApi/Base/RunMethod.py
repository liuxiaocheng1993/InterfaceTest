#coding:utf-8
'''
Created on 2019年3月18日

@author: Administrator
'''
import requests
import json

class RunMethod:

    def post_main(self,url,data,header):

        res=None
        if header =="yes":
            res=requests.post(url=url,data=data,headers=header)
           
        else:
            res=requests.post(url=url,data=data)
        try:
            s=json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
            
            print(type(s))
            return s
        
        except:
            print(type(res.text))
            print(type(str(res.text)))
            return str(res.text)

    def get_main(self,url,data,header):
        res=None
        if header =="yes":
            res=requests.post(url=url,data=data,headers=header,verify=False)
        else:
            res=requests.post(url=url,data=data,verify=False)
        print type(res)   
        return res.text

    def run_main(self,method,url,data=None,header=None):

        res=None

        if method=='post':
            res=self.post_main(url,data,header)
        else:
            res=self.get_main(url,data,header)
        
        return res
'''   
if __name__=="__main__":
    url="http://mall.api.epet.com/v3/login.html"
    data={"do":"postSubmit","postsubmit":"r9b8s7m4","username":"刘小成","password":"123456lxc","system":"wap","isWeb":1,"version":303}
    header="no"
    a=RunMethod()
    a.post_main(url,data.header)
'''
