#coding:utf-8
'''
Created on 2019年3月19日

@author: Administrator
结果的对比

'''

class CommonUtile:
    #判断一个字符是否在另一个字符串中
    def is_contain(self,str_one,str_two):
        flag=None
        '''
        我们经常从Excel读出来的是unicode
        ，进行比较某些python版本就会报错，要先转一下
        
        '''
        if isinstance(str_one, unicode):
            str_one=str_one.encode('unicode-escape').decode('string_escape')
        
        
        if str(str_one) in str_two:
            flag=True
        else:
            flag=False
        return flag
if __name__=="__main__":
    c=CommonUtile()
    a="1212121".decode("unicode-escape")
    print c.is_contain("str_one", "str_two")
