#coding:utf-8
'''
Created on 2019年3月18日

@author: Administrator
'''
from UtilePackage.OperationExcel import OperationExcel
from Data.Get_data import GetData
from Base.RunMethod import RunMethod
from Control.DataControl import Control
import json

class Depend(object):
    def __init__(self,file_name,sheet_id,case_id=None):
        self.file_name=file_name
        self.sheet_id=sheet_id
        self.case_id=case_id
        self.operation=OperationExcel(file_name,sheet_id)
        self.control=Control(file_name,sheet_id)
        self.data=GetData(file_name,sheet_id)
    #根据case_id找到当前行内容
    def get_case_lines_data(self):
        rows_data=self.operation.get_rows_data(self.case_id)
        return rows_data
    
    #执行依赖测试，获取结果
    def run_dependent(self):
        run_method=RunMethod()
        row=self.operation.get_rows_num(self.case_id)
        request_data=self.data.get_case_requestdata_value(row)
        url=self.data.get_case_request_url_value(row)
        method=self.data.get_case_request_mothod_value(row)
        header=self.data.get_case_header_value(row)
        depend_case=self.control.is_depend(row)
        
        if depend_case!=None:
            depend1=Depend(self.file_name,self.sheet_id,case_id=depend_case)
            return depend1.run_dependent()
        else:
            res=run_method.run_main(method, url, request_data, header)
        return res
    #根据依赖的key值，去取依赖测试的值
    def get_data_for_key(self):
        row=self.operation.get_rows_num(self.case_id)
        key=self.data.get_case_request_depend_value(row)
        json=self.run_dependent()
        try:
            return json.dumps(self.run_dependent())[key]
        except:
            print ("无法转换json")
            
    #修改当前请求的key对应的值
    
        