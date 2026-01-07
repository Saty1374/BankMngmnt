# def addition(a,b):
#     return (a+b)

# print(addition (23,43)) 

# CLASS, ATTRIBUTE, METHODS


# class Factory:
#     a=23 #Attribute (kyoki class ke andar aa rha hai)

    # def self(hello):#method
    #     print("how are u doing")
    
# print("hmko laar kuch smj nhe aa rha hai")

# print(Factory().a)
# Factory().self()

#Objects in Python(has all the powers related to class)

# obj= Factory()
# print(obj.a)
# obj.self()


#Constuctors - parameters ko maang skte hai iske help se yahan material, zips,pockets all are 

# class Factory:
#     def __init__(self,material,zips,pockets): #init -dender methods #self used as location transfer and mat.,zips,pckts are used as parameters
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#             print(f"you have {self.material} as material, {self.zips} zips and {self.pockets} pockets")
#             # showing methodd
            


# reebok = Factory("leather", 3 , 5)
# nike = Factory("cotton", 4, 6)

# print (nike.zips)
# reebok.show()


# types of attribute
# class attribute- a simple variable under class is called this. (Ex.- here a=23)
# Instance attribute- def __init__ (self,age) iske baad jo self.age = age likhte hai that is instance attribute

# types of methods
# 1. class methods- @classmethod

# class Myclass:
#     @classmethod
#     def hello(cls):
#         print ("how are you brother")

# obj= Myclass
# obj.hello()

# 2. static method- @staticmethod

# @staticmethod
# def static():
#     print("how are you")


# ****FOUR PILLARS****
# 1.Inheritence

# class Baap:
#     a= "Baap bete dono hi chutiye"
#     def show(self):
#         print("beta bakiyo ko chutiya bana rha hai")

# class Bete(Baap):
#     pass

# obj= Baap()
# print(obj.show())
# obj2 = Bete()
# print(obj2.show())


# super function****

# class Teacher:
#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(f"Hi my name is {self.name}")

 
# class Student(Teacher):
#     def __init__(self, name,studname):
#         super().__init__(name) # used to send the data to the class where originally this name has been initialized.
#         self.studname = studname

#     def show(self):
#         print(f"Hi my name is {self.name}, and my students name is {self.studname}")

# stud1 = Student("Ram", "Shyam")
# print(stud1.show())      

# main = Teacher("Ram")
# print(main.show())


#***Types of Inheritence 
# 1. Single inheritence
# simple jo sikhe hai inheritence me 

# 2. Multiple inheritence (code glat hai par aise hi hoga)
# class father:
#     def __init__(self,name):
#         self.name = name

# class mother:
#     def __init__(self,Mname):
#         self.Mname = Mname

# class child(mother,father):
#     def __init__(self, name, Mname, Cname):
#         super().__init__(name, Mname)
#         self.Cname = Cname

#     def show(self):
#         print("{self.name}, {self.Mname} and {self.Cname} are the members of a family")

# obj = child("Girish", "Shiwani", "Satyam")
# print (obj.show())


# 3. Multi levl Inheritence

# class Shoes:
#     def __init__(self,brand,size):
#         self.brand= brand
#         self.size= size

# class DelhiShoes(Shoes):
#     def __init__(self, brand, size, color):
#         super().__init__(brand, size)
#         self.color = color

# class MumbaiShoes(DelhiShoes):
#     def __init__(self, brand, size, color, price):
#         super().__init__(brand, size, color)
#         self.price = price

#     def show(self):
#         print(f"{self.brand}, {self.size}, {self.color},{self.price}")

# Nike = MumbaiShoes("Nike", 8, "Black", 2000)
# Reebok = MumbaiShoes("Reebok", 8, "Black", 2000)
# Puma = MumbaiShoes("Puma", 8, "Black", 2000)
# Nike.show()


# **2. Ploymorphism
# it basically means using a single keyword at differnt placed and at every place it have different meanings and works.
# like we use def_show(). 

# class Animal:
#     def show(self):
#         print("Hi there")

# class Human(Animal):
#     def show(self):
#         print("How are you doing?")

# obj = Human()
# obj.show()
####Here the self function for Animal got over ride and the child functions Self is used.


#  3.Encapsulation- 
# it simply provide privacy to your code, ab tk kya ho rha tha sh kuch public tha, tu kuch bhi access kr skta hai, kuch bhi change kr skte hai
# kisi bhi data ki privacy nhe thi pr using encapsulation techniques usually adding(_ = for protected and __ = Private)
# we can protect our data which we want to keep private. (__)Using double underscore with any methods give us the privacy
# now noone can access it.
# ex. def __show(self)



#4.ABSTRACTION
# we use abstract methods here and using that we can compulsarise some elements that should must be present while 
# defining the function


# from abc import ABC, abstractmethod

# class Animal(ABC):# abstract class
#     @abstractmethod

#     def make(self): #abstract method
#         print("hello")







######ADVANCED STUFFS ####


#****DECORATORS****


# def zindagidawwpar(func):
#     def wrapper():
#         print("Python,Xcel,sql,PowerBI for Data analytics first")
#         func()
#         print("and then comes with statistics,MLand more for data science.")
#     return wrapper
     
# @zindagidawwpar

# def DataScience():
#     print("Hi I am getting started in Data Feild")

# DataScience()


#***ARGS AND KWARGS***

# args- arguments (here when there are a no. of values given to calc on something we should not have to put all the values in the fumction, just use a star(*) as args and its done)
# kwargs- same as kwargs its just keyword arguments as a=3,b=4,c=45 so should not have to write every variable just use kwargs)

 
# def addition (*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)

# addition(74,343,43,234,2,4,2,4,335,566,246)

     

#***Lists, Dictonary and Set Comprehension****
# lists..
# ex.- even no.s saare likhne hai 1 se 20 tk 
# to we used to append i when we do with the hep of for statement
# so start with (i) here 

# l= [i for i in range (1,21) if i % 2 == 0] ## simply kisi ek bare se data me ek single element ko access krke usme changes krne ho to we use lists
# print(l)
     
#dictionary
# l={i: i*2 for i in range(1,21)}
# print(l)

#LAMBDA FUNCTION (shorter way of declaring the variables )
# addition= lambda a,b: a+b
# print(addition(12,493))

# addition= lambda 3543: "even" if a%2==0 else odd
# print(addition(3543))

#map,filter and zip
#1.Map
# a=[3,893,993,884,24,35]

# result = map(lambda x: x*2,a) #map provides a result on a list performed as the given function.
# print(list(result))

#2.FIlter
# def odd(x):
#     if x%2!=0:
#         return True
#     else:
#         return False
    
# a=[3,893,993,884,24,35]
# result = filter(odd, a)
# print(list(result))

#3.ZIP

