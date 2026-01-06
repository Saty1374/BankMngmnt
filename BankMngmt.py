import json  ### json means javascript object notation it is used to store all the data of the user related in it ,so that we dont have to always upload the data after opening the file. 
import string
import random
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []  ## This is the dummy data file in which all the updates related to the account will take place, and then it will send to the data.json file.

    try: ### Exceptional handling (try always comes with except)
        if Path(database).exists(): ## if there is any errpr in the path of json file
            with open (database) as fs: ## fs= file system, here we opened database in our file system
             data = json.loads(fs.read()) ## here fs.read reads the data present inside the database and then loads the json data inside the dummy data list.

        else:
            print("no such files exists")
    except Exception as err:
        print(f"an exception occurs as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:###updation of details in the database i.e json file (w=writes)
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountnumber(cls):
        alpha = random.choices(string.ascii_letters,k = 4)
        num = random.choices(string.digits,k = 5)
        spchar = random.choices("!@#$%^&*",k=2)## k is used to indicate the number of int or chars needed
        id = alpha+ num + spchar
        random.shuffle(id)
        return "".join(id)



    def Createaccount(self):
        info = {
            "name": input("tell your name:"), ## comma is important 
            "age" : int(input("tell your age:")),
            "email": input("tell your email:"),
            "pin": int(input("tell your 4 digit pin:")),
            "accountNo.": Bank.__accountnumber(),
            "Balance": 0
        }
        if info ['age'] < 18:
            print("sorry you are underage for making an account")
            if len(str(info['pin'])) !=4:
                print("sorry input a pin greater or equal to 4 digit")
        else:
            print("account created successfully")
            for i in info:
                print(f"{i} : {info[i]}")## it shows up on the screen all the details of the user 
            print("please note down your account number")

            Bank.data.append(info)

            Bank.__update()

    def depositmoney(self):
        accountno = input("Enter your account number: ")
        pin = int(input("Enter your pin:"))

        userdata = [i for i in Bank.data if i['accountNo.'] == accountno and i['pin'] == pin ] ###LIST COMPREHENSION(IMP)

        if userdata == False:
            print("Wrong account details")
        else:
            amount = int(input("Enter the amount u want to deposit:"))
        if amount > 10000 or amount < 0:
            print("Deposit money b/w 0 to 10000")
        else:
            userdata[0]['Balance'] += amount  ### VERY IMPORTANT - userdata ek dictoinary hai aur usme sirf ek hi elemnt hai to uske position ke hisab se search krna prega ,0th index waale element me balance khojo
            
            Bank.__update()
           
            print(f"{amount} credited to your account")
            print(f"updated data:{userdata}")

 
    def withdrawmoney(self):
         accountno = input("Enter your account number: ")
         pin = int(input("Enter your pin:"))

         userdata = [i for i in Bank.data if i['accountNo.'] == accountno and i['pin'] == pin ] ###LIST COMPREHENSION(IMP)

         if userdata == False:
             print("Wrong account details")
         else:
             amount = int(input("Enter the amount u want to withdraw:"))
         if amount > 20000:
             print("Itna nhe niklega 20000 tk nikal")
             if amount > userdata[0]['Balance']:
                 print("Paisa Kama MAdharchod")
         else:
             userdata[0]['Balance'] -= amount  ### VERY IMPORTANT - userdata ek dictoinary hai aur usme sirf ek hi elemnt hai to uske position ke hisab se search krna prega ,0th index waale element me balance khojo
            
             Bank.__update()
           
             print(f"{amount} deducted from your bank")
             print(f"updated data:{userdata}")

    def showdetails(self):

         accountno = input("Enter your account number: ")
         pin = int(input("Enter your pin:"))

         userdata = [i for i in Bank.data if i['accountNo.'] == accountno and i['pin'] == pin ] 

         print("your details are: /n/n/n")
         for i in userdata[0]:
             print(f"{i}: (userdata[0]{i})")

    def updatedetails(self):

         accountno = input("Enter your account number: ")
         pin = int(input("Enter your pin:"))

         userdata = [i for i in Bank.data if i['accountNo.'] == accountno and i['pin'] == pin ] 

         updation = input("kya update krna chahte ho bhai?:")

         if updation == 'name':
             newname = input("Enter your new name:")
             userdata[0]['name'] = newname
             print(userdata)
             
         elif updation == 'email':
             newemail = input("Enter your new email:")
             userdata[0]['email'] = newemail
             print(userdata)

         elif updation =='pin':
             newpin = int(input("Enter your new pin:"))
             userdata[0]['pin'] = newpin
             print(userdata)
        
         else:
             print("ye change nhe hoga")


         Bank.__update()
         print("Details updated")

    
    def deletedetails(self):

         accountno = input("Enter your account number: ")
         pin = int(input("Enter your pin:"))

         userdata = [i for i in Bank.data if i['accountNo.'] == accountno and i['pin'] == pin ] 

         if userdata == False:
             print("wrong details")
         else:
             check = input("Enter y for deletion of your account or n:")
             if check == "n" or "N":
                 print("bypassed")
             else:
                 index = Bank.data.index(userdata)
                 Bank.data.pop(index)
                 print("account deleted successfully")

         Bank.__update()
                 
                 
                 

user = Bank()
print("Press 1 for creating the account")
print("Press 2 for depositing money")
print("Press 3 for withdrawing money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting the account")

check = int(input("tell your response:"))

if check == 1:
     user.Createaccount()

if check == 2:
     user.depositmoney()

if check == 3:
     user.withdrawmoney()
         
if check == 4:
     user.showdetails()

if check == 5:
     user.updatedetails()

if check == 6:
     user.deletedetails()