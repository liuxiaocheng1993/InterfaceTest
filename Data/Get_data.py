#coding:utf-8
'''
Created on 2019年3月18日

@author: Administrator
'''
from UtilePackage.OperationExcel import OperationExcel
from Data.DataConfig import DataConfig

class GetData(object):
    def __init__(self,file_name=None,sheet_id=None):
        '''
        self.file_name=file_name
        self.sheet_id=sheet_id
        '''
        self.operation=OperationExcel(file_name,sheet_id)
        self.data=DataConfig()
    
    #获取excel行数，就是用例个数
    def get_case_lines(self):
        return self.operation.Get_excel_lines()
    
    
    #获取case的id值
    def get_case_id_value(self,row):
        
        col=self.data.get_case_id()
        return self.operation.Get_cell_value(row, col)
    #获取case的模块值
    def get_case_moudle_value(self,row):
        
        col=self.data.get_case_moudle()
        return self.operation.Get_cell_value(row, col) 
       
    #获取case的url值
    def get_case_request_url_value(self,row):
        col=self.data.get_case_url()
        #拿到单元格值

        return self.operation.Get_cell_value(row,col)
    #获取case的header值
    def get_case_header_value(self,row):
        col=self.data.get_case_header()
        #拿到单元格值
        return self.operation.Get_cell_value(row,col)
    
    #获取case的是否运行值
    def get_case_run_value(self,row):
        col=self.data.get_run()
        #拿到单元格值
        return self.operation.Get_cell_value(row,col)
    
    #获取case请求方式
    def get_case_request_mothod_value(self,row):
        col=self.data.get_requestWay()
        #拿到单元格值
        return self.operation.Get_cell_value(row,col)
    #获取case依赖值
    def get_case_depend_value(self,row):
        col=self.data.get_case_depend()
        #拿到单元格值
        return self.operation.Get_cell_value(row,col)
    #获取case依赖的返回值
    def get_case_request_depend_value(self,row):
        col=self.data.get_data_depend()
        #拿到单元格值
        return self.operation.Get_cell_value(row,col)
    #获取case数据依赖字段
    def get_case_data_depend_value(self,row):
        col=self.data.get_field_depend()
        #拿到单元格值
        return self.operation.Get_cell_value(row,col)
    #获取case请求数据
    def get_case_requestdata_value(self,row):
        col=self.data.get_data()
        #拿到单元格值
        return self.operation.Get_cell_value(row,col)
    
    #获取case预期结果
    def get_case_expect_value(self,row):
        col=self.data.get_expect()
        #拿到单元格值
        return self.operation.Get_cell_value(row,col)
    
    #获取case结果
    def get_case_result_value(self,row):
        col=self.data.get_result()
        #拿到单元格值
        return self.operation.Get_cell_value(row,col)

'''
if __name__=="__main__":
    demo=GetData()
    print demo.data
    print 111111
    sss=demo.get_case_request_mothod_value(0)
    print sss
'''
    
    
    
    
    
    
    