#coding:utf-8
'''
Created on 2019年3月18日

@author: Administrator
'''
class DataConfig:
    id='0'
    moudle='1'
    url='2'
    header='3'
    run='4'
    request_way='5'#请求类型
    
    case_depend='6'#case依赖
    data_depend='7'#依赖的返回值
    field_depend='8'#请求数据依赖值
    data='9'
    expect='10'
    result='11'
    

    #获取caseid
    def get_case_id(self):
        return int(DataConfig.id)
    #获取case模块
    def get_case_moudle(self):
        return int(DataConfig.moudle)
    #获取case的url
    def get_case_url(self):
        return int(DataConfig.url)
    #获取case的header
    def get_case_header(self):
        return int(DataConfig.header)

    #获取case的run值
    def get_run(self):
        return int(DataConfig.run)

    #获取case的request_way

    def get_requestWay(self):
        return int(DataConfig.request_way)

    
    #获取用例的case_depend

    def get_case_depend(self):
        return int(DataConfig.case_depend)


    #获取case的data_depend(依赖的返回值)

    def get_data_depend(self):
        return int(DataConfig.data_depend)

    #获取case的field_depend（依赖字段）
    def get_field_depend(self):
        return int(DataConfig.field_depend)

    #获取case的data
    def get_data(self):
        return int(DataConfig.data)

    #获取case的expect

    def get_expect(self):
        return int(DataConfig.expect)

    #获取case的result
    def get_result(self):
        return int(DataConfig.result)
    