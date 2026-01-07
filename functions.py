# def pallindrome(st):
#     rev=""
#     for i in range (len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         print ("Its a pallindrome")
#     else:
#         print("Not a pallindrome")

# pallindrome("NAMAN")
# pallindrome("SATYAM")



# def hello():
#     return "hi how are u doing"

# print (hello())



def get_name(person):
    return person['name']

people=[
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

Names= list(map(get_name,people))
print(Names)



# people=[
#     {'name': 'Alice', 'age': 30},  
#     {'name': 'Bob', 'age': 25}
# ]
# def age_greater_than_27(person):
#     return person['age'] > 27 

# filtered_people= list(filter(age_greater_than_27,people))
# print(filtered_people)