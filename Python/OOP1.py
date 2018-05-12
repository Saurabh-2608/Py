class MyClass:
    
    doc = 'Test Class'
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
    @classmethod
    def pass1(cls,a,b): 
        return cls(a,b) 
    @staticmethod
    def pass2(doc):
        print(doc)  
obj = MyClass.pass1(10,20)    
#obj = MyClass(10,20.20)
obj.hello()
MyClass.pass2("  ")
#obj1 = MyClass(10,20)
#obj1.hello()  
#print(obj.doc)
'''print(obj1.doc)
print(obj.__dict__)  
print(obj.__doc__)   
print(obj.__module__) 
print(MyClass.__name__) 
print(MyClass.__bases__) '''