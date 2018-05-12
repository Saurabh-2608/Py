class MyClass:
    def __init__(self):
        self.st = st
        self.__st1 = st1
        """a = int(input("Enter a :"))
        b = int(input("Enter b :"))
        c = a + b
        print(c)"""
        
    def hello(self):
        print("Hello",self.st) 
        print("Hello",self.__st1) 
           
    
obj = MyClass('Saurabh','Mono')
obj.hello()    
print(obj.st)  
print(obj._MyClass__st1)   
print(hasattr(obj,'st'))  
#print(getattr(obj,'st'))   
setattr(obj,'_MyClass__st1', 100) 
obj.hello()
delattr(obj,'st') 
obj.hello()      