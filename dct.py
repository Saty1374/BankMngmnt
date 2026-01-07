# d1 = {1:44, 2:45, 3:46, 4:47, 5:48}
# d2 = {6:49, 7:50, 8:51, 9:52, 10:53}

# d1[4] = 90 #updating 
# d1[6] = 100 #creating
# del d1[5] #deleting

# print(d1)

#Traversing in dictionary

# for i in d1:      for i in d1.keys():   for i in d1:
#     print(i)           print(i)             print d[i]


# help(dict)

# q.1 merging two dictionaries

# for i in d2:
#     d1[i] = d2[i]

# print(d1)

#q.2  to sum all the values in a dictionary

# sum=0
# for i in d1:
#     sum+= d1[i]

# print(sum)


# q.3 count the frequencies of each element  ********IMPORTANT

# a= [1,1,1,2,2,2,3,3,3,4,4,5,6,6,6,6]

# d={}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# print (d)


    

# q4. Combining two dictionaries by adding values for the similar keys

# d1={20:100, 21:103, 22:105, 23:200}
# d2={23:409, 24:510, 22:511, 26:900}


# sum=0
# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]


# print(d1)
 
    



