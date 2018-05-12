class MyClass:
    def fname(self):
        print("Saurabh")
    
class MyClass1(MyClass):
    def lname(self):
        print("Sharma")
    
class MyClass2(MyClass1):
    def college(self):
        print("KIIT")
   
obj = MyClass2()
obj.fname()
obj.lname()
obj.college()