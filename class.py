# class MyFirstClass:
#     name = "diksha"
#     age  = 20

#     def getName(self):
#         print(self.name)

# firstObject = MyFirstClass()
# print(firstObject) 

# firstObject.getName()
# print(firstObject.name)

# class Student:
#     def __init__(self):
#         self.name = ""
#         self.age = 0
#         self.gender = ""
#         self.grade = ""

# mayur = Student() # return the data and store in mayur
# print(mayur)

# mayur.name = "Mayur valvi"
# mayur.age = 20
# mayur.gender = "Male"
# mayur.grade = "10th"

# print(mayur.name)
# print(mayur.age)
# print(mayur.gender)
# print(mayur.grade)

# class Student:
#     def __init__(self,name,age,gender,grade):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.grade = grade
    
#     def PrintDetails(self):
#         print("NAME:",self.name)
#         print("AGE:",self.age)
#         print("GENDER:",self.gender)
#         print("GRADE:",self.grade)


# mayur = Student("Mayur valvi","20","Male","10th") # return the data and store in mayur
# print(mayur)

# # mayur.name = "Mayur valvi"
# # mayur.age = 20
# # mayur.gender = "Male"
# # mayur.grade = "10th"
# mayur.PrintDetails()

# print(mayur.name)
# print(mayur.age)
# print(mayur.gender)
# print(mayur.grade)

# class ExampleClass:
#     def __init__(self,val = 1):
#         self.first = val

#     def set_second(self,val):
#         self.set_second = val

# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5

# print(example_object_1)

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

# class Classy:
#     def method(self,par):
#         print("method",par)

# obj = Classy()
# obj.method(1)

# class Classy:
#     def method(self):
#         print("method")

# obj = Classy()
# obj.method(1)

#self method
# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia,self.var)

# obj = Classy()
# obj.var = 3
# obj.method()


# inheritance----
# class Star:
#     def __init__(self,name,galaxy):
#         self.name = name
#         self.galaxy = galaxy

# sun = Star("sun","milky way")
# print(sun)

# class Star:
#     def __init__(self,name,galaxy):
#         self.name = name
#         self.galaxy = galaxy
#     def __str__(self):
#         return self.name + " in " + self.galaxy

# sun = Star("sun","milky way")
# print(sun)   

# #two level inheritance
# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# for c1s1 in [Vehicle,LandVehicle,TrackedVehicle]:
#     for c1s2 in [Vehicle,LandVehicle,TrackedVehicle]:
#         print(issubclass(c1s1,c1s2),end ="\t")
#     print()


# #inheritance class variable
# class Super:
#     supVar = 1

# class Sub(Super):
#     subVar = 2

# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)

# #with constructor
# class Super:
#     def __init__(self):
#         self.supVar = 11

# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 12

# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)

# three level inheritance------
# class Level1:
#     variable_1 = 100
#     def __init__(self):
#         self.var_1 = 101
#     def fun_1(self):
#         return 102
    
# class Level2(Level1):
#     variable_2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var_2 = 201
#     def fun_2(self):
#         return 202
    
# class Level3(Level2):
#     variable_3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301
#     def fun_3(self):
#         return 302
    
# obj = Level3()
# print(obj.variable_1,obj.var_1,obj.fun_1())
# print(obj.variable_2,obj.var_2,obj.fun_2())
# print(obj.variable_3,obj.var_3,obj.fun_3())

#CLASS VARIABLE TO COUNT THE OBJECT------
# class ExampleClass:
#     counter=0
#     def __init__(self,val=1):
#         self.__first = val
#         ExampleClass.counter +=1

# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)

# print(example_object_1.__dict__,example_object_1.counter)
# print(example_object_2.__dict__,example_object_2.counter)
# print(example_object_3.__dict__,example_object_3.counter)

# class ExampleClass:
#     counter=0
#     def __init__(self,val=1):
#         # self.__first = val
#         ExampleClass.counter +=1
#         if  val %2!=0:
#             self.a= 1
#         else:
#             self.b = 1

# example_object = ExampleClass(1)
# print(example_object.a)
# print(example_object.b)#error has occured

#try-except to solve error-----
# class ExampleClass:
#     counter=0
#     def __init__(self,val=1):
#         # self.__first = val
#         ExampleClass.counter +=1
#         if  val %2!=0:
#             self.a= 1
#         else:
#             self.b = 1

# example_object = ExampleClass(6)

# try:
#     print("a=",example_object.a)
# except AttributeError:
#     try:
#         print("b=",example_object.b)
#     except AttributeError:
#         print("the error has occured! sliently passing it")


#using hasattr function
# class ExampleClass:
#     counter=0
#     a = 1
#     def __init__(self,val=1):
#         # self.__first = val
#         ExampleClass.counter +=1
#         if  val %2!=0:
#             self.a= 1
#         else:
#             self.b = 1

# example_object = ExampleClass(1)

# if hasattr(example_object,'a'):
#     print("a=",example_object.a)

# if hasattr(example_object,'b'): #with help of object
#     print("b=",example_object.b)

# print(hasattr(ExampleClass,'b')) #with help of class
# print(hasattr(ExampleClass,'a'))

#private var----(use double underscore to private the var)
# class Python:
#     population = 1
#     victims = 0
#     def __init__(self):
#         self.length_ft = 3
#         self.__venomous = False

# myObj = Python()
# print("myObj.population:",myObj.population)
# print("myObj.victims:",myObj.victims)
# print("myObj.length_ft:",myObj.length_ft)
# print("myObj.__venomus:",myObj.__venomous) #private variable it gives error when the obj call
# print("myObj.__venomus:",myObj._Python__venomous)

# #NAME MANLING METHOD (HIDDEN FUNCTION)----
# class Classy:
#     def visible(self):
#         print("visible")

#     def __hidden(self):
#         print("hidden")

# obj = Classy()
# obj.visible()    #ouput:visible
# try:
#     obj.__hidden()   #This Fails
# except:
#     print("failed")     #output:failed
# obj._Classy__hidden()  #OP : HIDDEN

# obj = Classy()
# print(type(obj))
# print(type(obj).__name__) # to read the class name 

# #ISINSTANCE ----
# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# my_vehicle = Vehicle()
# my_land_vehicle = LandVehicle()
# my_tracked_vehicle = TrackedVehicle()

# for obj in [my_vehicle,my_land_vehicle,my_tracked_vehicle]:
#     for c1s in [Vehicle,LandVehicle,TrackedVehicle]:
#         print(isinstance(obj,c1s),end ="\t")
#     print()

#ISOPERATOR---

# class SampleClass:
#     def __init__(self,val):
#         self.val = val

# object_1 = SampleClass(0)
# object_2 = SampleClass(2)
# object_3 = object_1
# object_3.val +=1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val,object_2.val,object_3.val)

# string_1 = "Mary had a little"
# string_2 = "Mary had a little lamb"
# string_1 += " lamb"

# print(string_1 == string_2,string_1 is string_2)

#str method---
# class Super:
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return "My name is " + self.name + "."
    
# class Sub(Super):
#     def __init__(self,name):
#         Super.__init__(self,name) #constructor calling of the parent class.

# obj = Sub("Andy")
# print(obj)


# #SUPER METHOD----
# class Super:
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return "My name is " + self.name + "."
    
# class Sub(Super):
#     def __init__(self,name):
#         super().__init__(name) #use super method...

# obj = Sub("Andy")
# print(obj)

#multiple inheritance----
# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
    
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
    
# class Sub(SuperA,SuperB):
#     pass

# obj = Sub()
# print(obj.var_a,obj.fun_a())
# print(obj.var_b,obj.fun_b())

#MULTI LEVEL INHERITANCE PROBLEM--- (so the ans is bottom to top approach)

# class Level1:
#     var = 100
#     def fun(self):
#         return 101
    
# class Level2(Level1):
#     var = 200
#     def fun(self):
#         return 201 #override the value
    
# class Level3(Level2):
#     pass

# obj = Level3()
# print(obj.var,obj.fun()) #python having bottom to top appraoch so the ans is level2 value


#MULTIPLE INHERIITENCE problem ---
# class Left:
#     var = "L"
#     var_left = "LL"
#     def fun(self):
#         return "Left"

# class Right:
#     var = "R"   # same name as left.var
#     var_right = "RR"
#     def fun(self):    #same name as left.fun
#         return "Right"
    
# class Sub(Left,Right):
#     pass
# obj = Sub()
# print(obj.var,obj.var_left,obj.var_right,obj.fun()) # in this case checks left-right oder determines precedence


# #POLYMORPHISM----

# class One:
#     def do_it(self):
#         print("do_it from one")

#     def doanything(self):
#         self.do_it()  #call the self do_it and this is the obj of class two

# class Two(One):
#     def do_it(self):  
#         print("do_it from two")

# one = One()
# two = Two()
# one.doanything()   #output do_it from one
# two.doanything()

# #MRO--have 2 rule  occur in multi level and multiple inheritance problm 
# # 1. is bottom to top in multilevel inheritance  and 2. left to right order precednece in multiple inheritance.

# #TRY EXCEPT
# def reciprocal(n):
#     try:
#         n = 1/n
#     except ZeroDivisionError:
#         print("division failed")
#         return None
#     else:
#         print("everthing went fine")
#         return n
    
# print("----------------")
# print("reciporal(2):",reciprocal(2))#use else
# print("----------------")
# print("reciporal(0):",reciprocal(0))
# print("----------------")
    
# #FINALLY -- used for cleanup oper.. and always executes in last
# def reciprocal(n):
#     try:
#         n = 1/n
#     except ZeroDivisionError:
#         print("division failed")
#         n= None
#     else:
#         print("everthing went fine")
        
#     finally:
#         print("its time to goodbye")
#         return n
    
# print("----------------")
# print("reciporal(2):",reciprocal(2))#use else
# print("----------------")
# print("reciporal(0):",reciprocal(0))
# print("----------------")

#EXCEPTION CLASS IS BUILT IN PYHTON
try:
    i = int("hello!")
except Exception as e:  # gives first error
    print(e) 
    print(e.__str__())  #gives second error

#own exception
class MyZeroDivisionError(ZeroDivisionError):
    pass
 
def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")
    
do_the_division(False)