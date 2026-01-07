# n=int(input("Enter an integer:"))
# for i in range (n):
#     print("hello world")

# n=int(input("Enter an integer:"))
# for i in range (1,n,1):
#     print(i)

# n=int(input("Enter an integer:"))
# for i in range (n,0,-1):
#     print(i)

# n=int(input("Enter an integer:"))
# for i in range(n,(n*10)+1,n):
#     print(i)

# sum=0
# n=int(input("Enter an integer:"))
# for i in range(1,n+1,1):
#     sum=sum+i

# print(f"the sum of all the number upto {n} is:{sum}"")


# fact=1
# n=int(input("Enter an integer:"))
# for i in range(1,n+1,1):
#     fact=fact*i

# print(f"Factorial of numbers upto {n} is: {fact}")


 
# n=int(input("Enter a number:"))
# even=0
# odd=0
# for i in range(1,n+1):
#      if i%2 == 0:
#         even = even + i 
#      else:
#         odd = odd + i
# print(f"The sum of all even numbers are {even} and all odd numbers are {odd}")

#  INDENTATION MATTERS A LOT IN PYTHON!!!!!!!


# FACTORS PRINT

# n=int(input("Enter a number:"))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)



##### PERFECT NUMBER is the one whose factors sum is equal to the number itself.

# n=int(input("ENter a number:"))
# sum=0
# for i in range (1, n):
#     if n%i == 0:
#         sum=sum+i
         
# if sum==n:
#             print("its a perfect number")
# else:
#             print("Not a perfect number")

    


# ******PRIME NUMBER OR NOT******  IMPORTANTTT
# n=int(input("ENter a number:"))
# count=0 
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1

# if count ==2:
#     print("Your number is prime")  
# else:
#     print("Not a prime number")



# ***STRINGS REVERSING AND QUESTIONS****

# a="Insert string here"
# b=""
# for i in range (len(a)-1,-1,-1):
#     b+=a[i]

# if (a==b):
#         print("Its a Pallindrome")
# else:
#     print("Not a pallindrome")



# ********** IMPORTANT QUESTIONNNN**********

# str1 = "P@#yn26at^&i5ve"
# print("Length of your string is:")
# print(len(str1))


# dig=0
# char=0
# symbol=0

# for i in str1:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         symbol+=1

# print(f"No. of digits are {dig}\nNo. of characters are {char}\nNo. of symbols are {symbol}")






# WHILE LOOPS 
# 1. REVERSING THE NUMBER AND PRINTING IT AS A REVERSED NUMBER(we use mod and floor division for this)



# a=int(input("Enter a number:"))

# while a>0:
#     print(a % 10)
#     # a = a // 10


# a=int(input("Enter a number:"))

# rev=0

# while a>0:
#     rev= rev * 10 + (a % 10)
#     a = a // 10

# print(rev)


# 2. CHECK WHETHER A NUMBER IS PLLINDROME OR NOT

# a=int(input("Enter a number:"))

# copy=a
# rev=0

# while a>0:
#     rev= rev * 10 + (a % 10)
#     a = a // 10

# print(f"Reverse of the entered number is: {rev}")

# if rev == copy:
#     print("the number is a pallindrome")
# else:
#     print("not a pallindrome")





# *****GUESSING GAMEEEE*******(import library used)

# import random
# num= random.randint(1,100)

# tries=0

# while True:
#     guess=int(input("guess a number between 1 to 100:"))

#     if num == guess:
#         tries+=1
#         print(f"You selected the right number and took {tries} tries to guess it.")

#     elif guess>num:
#         tries+=1
#         print("GO lower")

#     elif guess<num:
#         tries+=1
#         print("GO Higher")

#     else:
#         tries+=1
#         print("Invalid number!")
  

# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print( )
total=0
while True:
    x= int(input("enter the num:"))

    if x>0:
        total+=x
    elif x==0:
        print("wrong input!!!")
        print(f"sum till now is {total}")



 