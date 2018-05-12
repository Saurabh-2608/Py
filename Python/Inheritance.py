class MyClass:
    
    #doc = 'Test Class'
    def __init__(self,st,st1):
        self.st = st
        self.st1 = st1
        """a = int(input("Enter a :"))
        b = int(input("Enter b :"))
        c = a + b
        print(c)"""
    def hello(self):
        print("Hello",self.st) 
        print("Hello",self.st1)
    '''@classmethod
    def pass1(cls,a,b): 
        return cls(a,b) 
    @staticmethod
    def pass2(doc):
        print(doc)'''
class MyClass1(MyClass):
    def __init__(self,st,st1,st2):
        MyClass.__init__(self, st, st1)
        self.st2 = st2
    def hello(self):
        MyClass.hello(self) 
        print("Hello",self.st2)
class MyClass2(MyClass):
    def __init__(self,st,st1,st3):
        MyClass.__init__(self, st, st1)
        self.st3 = st3
    def hello(self):
        MyClass.hello(self) 
        print("Hello",self.st3)    
     
obj1 = MyClass1(10,20,100)
obj1.hello()
obj2 = MyClass2(30,40,200)
obj2.hello()               