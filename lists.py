#*******TWO WAYS TO CALL 

# l =[34,2984,9284,922.99,90]

#1st way

# for i in range(len(l)):
#     print(l[i])

#2nd way

# for i in l:
#     print(i)




# Q.1

# l = [23,12,-34,90,-43,33]

# for i in l:
#     if i>0:
#         print("Positive number")
#     else:
#         print("NEgative number")

# or 

# print("Positive numbers are:")
# for i in l:
#     if i>=0: 
#         print(i)

# print("Negative numbers are:")
# for i in l:
#     if i<0:
#         print(i)




# Q.2

# l=[23,21,33,12,11,54,32]
# sum=0

# for i in range(len(l)):
#     sum=sum+l[i]

# print(sum/len(l))


# Q.3

# l=[23,203,21,843,842,830,49,83984]

# grtnum=l[0]
# index=0

# for i in range (len(l)):
#     if l[i] > grtnum:
#         grtnum = l[i]
#         index= i

# print(f"Greatest number will be:{grtnum}")
# print(f"Index would be {index}")



# Q.3 and Q.4 are good ones



# Q.4

# l=[23,203,21,843,842,830,49,83984,900]

# largest=l[0]
# Sec_largest=l[0]

# for i in range (len(l)):
#     if l[i] > largest:
#         Sec_largest = largest
#         largest = l[i]

#     elif l[i] > Sec_largest:
#         Sec_largest = l[i]
    
# print(f"LArgest number is {largest} and 2nd largest number is {Sec_largest}")
        
    

# Q.5
# LIST SORTING

# l=[23,24,25,27,28,29,11]

# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue

#     else:
#         print("Not sorted")
#         break
         
# else:
#      print("The list is sorted")


