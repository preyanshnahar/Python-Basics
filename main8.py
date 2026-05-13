# OOP
# Object Oriented Programming 







# # Class is a blueprint for creating objects
# # Creating Class
# class Student :
#     name = "Preyansh"

# # Creating Object(Instance)
# s1 = Student()
# print(s1.name)








# init Function 
# Constructor
# All classes have a function called _init_(), which is always executed when the object is being initiated

# # Creating Class
# class Student :
#     def __init__(self,fullname) :
#         self.name = fullname

# # Creating Object
# s1 = Student("Preyansh")
# print(s1.name)












# class Student :
#     def __init__(self,name,marks) :
#         self.name = name 
#         self.marks = marks

# s1 = Student("Preyansh",90)
# s2 = Student("Nahar",91)

# print(s1.name)
# print(s1.marks)
# print(s2.name)
# print(s2.marks)










# # Two Types of constructors
# class Student :
#     # Default Constructor
#     def __init__(self) :
#         pass

#     # Parameterized Constructor 
#     def __init__(self,name) :
#         self.name = name 










# # Class and Instance Attributes

# class Student :
#     college = "temp" # Class Attribute
#     def __init__(self,name) :
#         self.name = name # Instance Attribute  









# # Methods are functions that belong to a class
# class Student :
#     def __init__(self,name) : 
#         self.name = name 
#     def get(self) :
#         print(self.name)


# s1 = Student("Preyansh")
# s1.get()









# # Take name and 3 subjects marks and print their average
# class Student :
#     def __init__ (self,name,mark1,mark2,mark3) :
#         self.name = name 
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3
    
#     def average(self) :
#         return (self.mark1 + self.mark2 + self.mark3)/3
    
# s1 = Student("Preyansh",81,85,89)
# print(s1.average())









# # Static Methods
# # Methods that dont use the self parameter

# class Student :
#     @staticmethod # Decorators
#     def college() :
#         print("Temp") 

# # Decorators allows us to wrap another function in order to extend the behaviour of the wrapped function without permanently modifying it 








# Four Pillars of OOPS

# 1. Abstraction
# Hiding the implementation details of a class and only showing the essetial features to user

# class Car_Engine :
#     def __init__ (self) :
#         self.acc = False 
#         self.brk = False
#         self.clt = False

#     def start(self) :
#         acc = True
#         clt = True
#         print("Car Engine has started")

# s1 = Car_Engine() 
# s1.start()


# 2. Encapsulation 
# Wrapping data and functions into a single unit

# 3. Inheritance

# 4. Polymorphism









# # Create account class with 2 attributes -> balance and account_no
# # Create methods for debit,credit, and printing the balance


# class Account :
#     def __init__ (self,name,number) :
#         self.name = name 
#         self.balance = 0
#         self.number = number

#     def debit(self,amount) :
#         self.balance -= amount
#         self.print()

#     def credit(self,amount) :
#         self.balance += amount
#         self.print()  

#     def print(self) :
#         print("Current Balance : ",self.balance)


# u1 = Account("Preyansh",123)
# u1.credit(100)
# u1.debit(100)
# u1.credit(100)
# u1.debit(50)
# u1.print()












# del
# Used to delete properties or object itself


# class Student :
#     def __init__(self,name) :
#         self.name = name 

# s1 = Student("Preyansh")
# print(s1.name)

# del(s1)
# print(s1) # Will give error

# s2 = Student("Nahar")
# print(s2.name)

# del(s2.name)
# print(s2)
# # print(s2.name) # Only name will give error since only this attribute is deleted









# Private (like) Attributes and Methods
# They are meant to be used only within class and are not accessible from outside the class

# class Student :
#     def __init__(self,name,pasw) :
#         self.name = name 
#         self.__pasw = pasw # This is now private class because of underscore
    
# s1 = Student("Preyansh",123)
# print(s1.pasw) # Not Safe and will throw error after declaring private







# 3. Inheritance 
# When one class is derived properties and methods of another class (parent/base)

# class car :
#     @staticmethod
#     def start() :
#         print("Car started")

#     @staticmethod
#     def stop() :
#         print("Car stopped")

# class BMW(car) :
#     def __init__(self,name) :
#         self.name = name 


# car1 = BMW("m1")
# car2 = BMW("m2")

# car1.start()
# car2.stop()









# Types of Inheritance
# Single Inheritance
# Multiple Inheritance
# Multi Level Inheritance







# Super Method
# It is used to access methods of parent class 

# class car :
#     def __init__(self,t) :
#         self.t = t

#     @staticmethod
#     def start() :
#         print("Car started")

#     @staticmethod
#     def stop() :
#         print("Car stopped")

# class BMW(car) :
#     def __init__(self,name,t) :
#         self.name = name 
#         super().__init__(t)



# car1 = BMW("m1","electric")
# print(car1.t) # Error if not declared 










# Class Method
# It is bound to the class and receives the class as an implicit first argument 
# Note :- Static method cannot access or modify class state and generally for utility

# class Student :
#     name = "Temp"
#     @classmethod # Decorator 
#     def name_change(self,name) :
#         self.name = name


# s1 = Student()
# print(s1.name)
# s1.name_change("Preyansh")
# print(s1.name)
# print(Student.name) # With class method it will change name = "Preyansh" , without it name = "Temp"







# # Property
# # Used on any method in the class to use the method as a property

# class Student :
#     def __init__(self,mat,phy,chm) :
#         self.mat = mat
#         self.phy = phy
#         self.chm = chm
#         # self.percentage = str((self.mat+self.phy+self.chm)/3) + "%"
#     @property
#     def calc(self) :
#         return str((self.mat+self.phy+self.chm)/3) + "%"
    

# s1 = Student(90,85,80)
# print(s1.calc) # Percentage will not change if property decorator not used 
# # print(s1.percentage)

# s1.phy = 80
# # print(s1.percentage) # Percentage will not change if property decorator not used 
# print(s1.calc) # Percentage will not change if property decorator not used 










# 4. Polymorphism (Operator Overloading)
# Same operator is allowed to have different meaning according to context
class Complex :
    def __init__(self,real,img) :
        self.real = real 
        self.img = img
    
    def show(self) :
        print(self.real,"i +",self.img,"j")

    # def add(self,num2) :
    #     new_real = self.real + num2.real
    #     new_img = self.img + num2.img
    #     return Complex(new_real,new_img)

    def __add__(self,num2) : # Dunder Function
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real,new_img)


num1 = Complex(1,4)
num1.show()
num2 = Complex(2,7)
num2.show()

# num3 = num1.add(num2)
# num3.show()

num3 = num1 + num2 
num3.show()














# Define circle with radius and write area and perimeter function
class circle :
    def __init__(self,rad) :
        self.rad = rad
    
    def area(self) :
        return 3.14 * self.rad * self.rad
    
    def per(self) :
        return 2 * 3.14 * self.rad












# Define Employee class with attribute role,department, and salary 
# Create engineer class that inherits itand has name and age

class Emp :
    def __init__(self,rol,dep,sal) :
        self.rol = rol 
        self.dep = dep
        self.sal = sal 
    
    def show(self) :
        print("Role :",self.rol)
        print("Department :",self.dep)
        print("Salary :",self.sal)

class Eng(Emp) :
    def __init__(self,name,age) :
        self.name = name 
        self.age = age
        super().__init__("Engineer","IT","100000")













# Create a class order which stores
# Use dunder __gt__ to convey
# order1 > order2 if price of order1 > price of order2

class Order :
    def __init__(self,item,price) :
        self.item = item
        self.price = price

    def __gt__(self,order2) :
        return self.price > order2.price
