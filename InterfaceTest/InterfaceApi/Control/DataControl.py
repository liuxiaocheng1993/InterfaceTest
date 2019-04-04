#coding:utf-8
'''
Created on 2019年3月18日

@author: Administrator
'''
from Data.Get_data import GetData
import json
from Data.DataConfig import DataConfig

class Control():
    def __init__(self,file_name=None,sheet_id=None):
        '''
        self.file_name=file_name
        self.sheet_id=sheet_id
        '''
        self.data=GetData(file_name,sheet_id)
        self.dataconfig=DataConfig()
    
    
    
    #判断case是否返回header
    def is_header(self,row):
        header=self.data.get_case_header_value(row)
        if header=="yes":
            return 'header'
        else:
            return None
    
    #获取是否执行
    def get_is_run(self,row):
        run_moudle=self.data.get_case_run_value(row)

        if run_moudle=="yes":
            flag=True
        else:
            flag=False

        return flag
    #根据依赖key获取依赖值，这里针对json取值
    def get_data_for_json(self,row,jsons):
        key=self.data.get_case_data_depend_value(row)
        jsondata=json.load(jsons)
        return jsondata[key]
    #写入结果
    def write_result(self,row,value):
        col=self.dataconfig.get_result()
        self.data.operation.WriteExcel(row, col, value)
        
    #判断是否有依赖
    def is_depend(self,row):
        depend_case=self.data.get_case_depend_value(row)
        
        if depend_case:
            return depend_case
        else:
            return None
        
        