'''
Created on 17-Feb-2018

@author: Chino Steve
'''

class CGPA:
    def __init__(self,DAA,COA,DBMS,MATHS4,PDC,cgpa):
        self.__DAA = DAA
        self.__COA = COA
        self.__DBMS = DBMS
        self.__MATHS4 = MATHS4
        self.__PDC = PDC
        self.cgpa = cgpa
    def cal_cgpa(self):    
        self.cgpa = (int(self.__DAA) + int(self.__COA) + int(self.__DBMS) + int(self.__MATHS4) + int(self.__PDC))/5
        print('CGPA of Student is ',self.cgpa)
obj = CGPA('0','0','0','0','0','0')
setattr(obj, '_CGPA__DAA', 90)
setattr(obj, '_CGPA__COA', 85)
setattr(obj, '_CGPA__DBMS', 95)
setattr(obj, '_CGPA__MATHS4', 90)
setattr(obj, '_CGPA__PDC', 85)
obj.cal_cgpa()