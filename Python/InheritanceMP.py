from abc import ABC, abstractmethod
class A:
    @abstractmethod
    def name(self):
        pass
    
class B(A):
    def name(self):
        print("Sharma")
    
class C(A):
    def name(self):
        print("KIIT")

   
obj = B()
obj.name()
obj1 = C()
obj1.name()