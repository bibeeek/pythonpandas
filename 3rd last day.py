"""class Car:  
    CAR: A vehicle representaton
    milage="16.00"
    name_outer="KIA-KIA"
    __korean_car="KIA"

    def __init__(self, name, build_year):
        self.name = name #Kia
        self.build_year = build_year #2012
        print("__init__ > Object created")
    
    def __del__(self):
        print("Object Deleted")

    def property(self,*args):
        country=args[0]
        color=args[1]
        return self.name+ " built on "+self.build_year+" from "+country+ " , coloured: "+color+" >> milage is "+self.milage
 
    @classmethod #classmethod must have a reference to a class object as the first parameter
    def property_class(cls,*args):#cls for Car
        country=args[0]
        color=args[1]
        # return cls.name+ " built on "+cls.build_year+" from "+country+ " , coloured: "+color+" >> milage is "+cls.milage
        # return "@ClassMethod from "+country+ " , coloured: "+color+" >> milage is "+cls.milage
        return cls.name_outer+ " from "+country+ " , coloured: "+color+" >> milage is "+cls.milage


    @staticmethod #similar to classmethod but doesn't take any obligatory parameters (like a class method)
    def property_static(*args):
        country=args[0]
        color=args[1]
        # return Car.name_outer+ " from "+country+ " , coloured: "+color+" >> milage is "+Car.milage
        return "@StaticMethod from "+country+ " , coloured: "+color+" >> milage is "+Car.milage
        

print("\nCar Object Created")
obj = Car("Kia","2012");

print("obj.milage : ",obj.milage)
print("__korean_car : ",Car._Car__korean_car) #will not run obj.__korean_car or Car.__korean_car #Mangling
print("obj.property() : ",obj.property("Korea","Silver Grey"))
#print("@classmethod : ",Car.property_class("Korea","Red"))
#print("@staticmethod) : ",Car.property_static("Korea","Red"))
#print(obj.__dict__)
#print(Car.__dict__)


Class: callable __call__


class A:
    Class A, displaying Arguments

    def __init__(self):
        print("An instance of A was initialized")

    def __del__(self):
        print("instance willl be  deleted")
        
    
    def __call__(self, *args, **kwargs):
        print("Arguments are:", args, kwargs)
              
print(A.__doc__)
x = A() #creating Object x
z=A()
p=A()
print(x.__doc__)

print("\nCalling the instance:")
p(3, 4, x=11, y=10)

print("Let's call it again:")
x(3, 4, x=11, y=10)
del x
del z
del p"""



"""
Class: inheritance
"""

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print("Calling parent constructor")

   def parentMethod(self):
      print('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print("Parent attribute :", Parent.parentAttr)

class animal:
    place="zoo"
    def __init__(self):
        print("this is animal class")
        

class Child(Parent,animal): # define child class
   def __init__(self):
      print("Calling child constructor")

   def childMethod(self):
      print('Calling child method')


      

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
print(c.place)

