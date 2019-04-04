#coding:utf-8
'''
Created on 2019年3月18日

@author: Administrator
'''


import sys

sys.path.append(r"C:\Users\Administrator\Desktop\成果\InterfaceApi")
from Data.Get_data import GetData
from Base.RunMethod import RunMethod
from UtilePackage.OperationExcel import OperationExcel
from Control.DataControl import Control
from UtilePackage.CommonUtile import CommonUtile
from Control.DataDepend import Depend
from Report.SendEmail import SendEmail





class RunTest(object):
    def __init__(self):
        self.run_method=RunMethod()
        self.data=GetData(r"C:/Users/Administrator/Desktop/3333.xls", 0)
        self.control=Control(r"C:/Users/Administrator/Desktop/3333.xls", 0)
        #self.depend=Depend(r"C:/Users/Administrator/Desktop/3333.xls", 0)
        self.CommonUtile=CommonUtile()
        
    #程序执行
    def go_on_run(self):
        rows_count=self.data.get_case_lines()
        res=None
        n=0
        j=0
        for i in range(1,rows_count):
            is_run=self.control.get_is_run(i)
            if is_run==False:
                url=self.data.get_case_request_url_value(i)
                method=self.data.get_case_request_mothod_value(i)
                run=self.data.get_case_run_value(i)
                data=self.data.get_case_requestdata_value(i)
                header=self.data.get_case_header_value(i)
                expect=self.data.get_case_expect_value(i)
                is_depend=self.control.is_depend(i)
                if is_depend!=None:
                    row=OperationExcel().get_rows_num(is_depend)
                    depend=Depend(r"C:/Users/Administrator/Desktop/3333.xls", 0,is_depend)
                    #获取响应数据
                    denpen_reaponse_data=depend.get_data_for_key()
                    depend_key=self.data.get_case_data_depend_value(row)
                    #data[depend_key]=denpen_reaponse_data
                res=self.run_method.run_main(method,url,data,header)
                if self.CommonUtile.is_contain(expect, res):
                    self.control.write_result(i, "测试通过".decode('utf-8'))
                    n=n+1
                else:
                    self.control.write_result(i,"测试失败".decode('utf-8'))
                    
                    j=j+1
                print res
        
        to_list=['651525091@qq.com']
        sendemail=SendEmail("smtp.qq.com","1119864992@qq.com",to_list[0],"clefcofolgvcgied",rows_count
                            ,n,j)
        sendemail.send_mail()
                                            
            
            
if __name__=="__main__":
    runTest=RunTest()
    runTest.go_on_run()
    
    
    