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
class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101
    def fun_1(self):
        return 102
    
class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    def fun_2(self):
        return 202
    
class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301
    def fun_3(self):
        return 302
    
obj = Level3()
print(obj.variable_1,obj.var_1,obj.fun_1())
print(obj.variable_2,obj.var_2,obj.fun_2())
print(obj.variable_3,obj.var_3,obj.fun_3())