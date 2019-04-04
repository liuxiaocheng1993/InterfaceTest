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
            return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
        except:
            
            return str(res.text)

    def get_main(self,url,data,header):
        res=None
        if header =="yes":
            res=requests.post(url=url,data=data,headers=header,verify=False)
        else:
            res=requests.post(url=url,data=data,verify=False)
        return res.text

    def run_main(self,method,url,data=None,header=None):

        res=None

        if method=='post':
            res=self.post_main(url,data,header)
        else:
            res=self.get_main(url,data,header)
        
        return res