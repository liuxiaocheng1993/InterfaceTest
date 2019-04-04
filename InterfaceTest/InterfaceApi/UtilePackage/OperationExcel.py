#coding:utf-8

'''
Created on 2019年3月18日

@author: Administrator
'''
import xlwt
import xlrd
from xlutils.copy import copy
from docutils.nodes import row
class OperationExcel(object):
    
    def __init__(self,file_name=None,sheet_id=None):
        
        if file_name:
            
            self.file_name=file_name
            self.sheet_id=sheet_id
            self.data=self.ReadExcel()
        else:
            self.file_name=r"C:\Users\Administrator\Desktop\interface.xls"
            self.sheet_id=0
            self.data=self.ReadExcel()
    #读Excel的操作,拿到sheet内容
    def ReadExcel(self):
        data=xlrd.open_workbook(self.file_name)
        tables=data.sheets()[self.sheet_id]
        return tables
    
    #拿到行数
    def Get_excel_lines(self):
        tables=self.data
        return tables.nrows
    #获取某个单元格的内容
    def Get_cell_value(self,row,col):
        return self.data.cell_value(row,col)
    #写入数据
    def WriteExcel(self,row,col,value):
        read_data=xlrd.open_workbook(self.file_name)
        r_sheet = read_data.sheet_by_index(self.sheet_id)
        write_data=copy(read_data)#先copy
        sheet_data=write_data.get_sheet(self.sheet_id)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)
    #根据对应的case_id找到对应的行
    def get_rows_num(self,case_id):
        col_data=self.get_cols_values()
        num=0
        for col_data in col_data:
            if case_id==col_data:
                return num
            num=num+1
    
    #根据对应的case——id找到行的内容
    def get_rows_data(self,case_id):
        row_num=self.get_rows_num(case_id)
        return self.get_row_values(row_num)
        
    
    #根据行号，找到该行的内容
    
    def get_row_values(self,row):
        tables=self.data
        return tables.row_values(row)  
    
    #获取某一列的内容
    def get_cols_values(self,col=None):
        if col!=None:
            return self.data.col_values(col)
        else:
            return self.data.col_values(0)
          
        
        
    

'''
if __name__=="__main__":
    
    demo=OperationExcel()
    print demo.data
    print demo.ReadExcel().nrows
    print demo.Get_cell_value(1, 2)
'''  
    