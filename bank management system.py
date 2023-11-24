print("_"*40)
print("      bank management system     ")
print("_"*40)

data={}
list1=["name","address","phone","govt id","account type","amount"]

def take_data():
    acc_num=input("enter account number:")
    for item in list1:
        list2.append(input("enter%s:"%item))

        data[acc_num]=dict(zip(list1,list2))
        print("account created")
        print("__________________")


def other_options():
   ch=int(input("1. check balance \n2. withdrow \3.deposit \n enter choice;"))
   if ch==1:
       print("availble balance:",data[acc_num]["amount"])
       print("__________________")

   elif ch==2:
        amt=int(input("enter amount to withdrow:"))
        new_amt=int(data[acc_num]["amount"])-amt
        data[acc_num]["amount"]=new_amt
        print("_______________________")
        print("withdrow successful")
        print("available balance :",data[acc_num]["amount"])
        print("______________________")
   elif ch==3:
        amt=int(input("enter amount to deposit:"))
        new_amt=int(data[acc_num]["amount"])+amt

        data[acc_num]["amount"]=new_amt
        print("_____________")
        print("deposit successfull")
        print("availble balance:",data[acc_num]["amount"])
        print("____________________________")
    

while True:
    list2=[]
    ch=int(input("1.new customer\n 2.existing customer\n 3.exit\n enter choice:"))
    if ch==1:
        take_data()
    if ch==2:
        acc_num=input("enter your account number")
        if acc_num in data:
         print("record found")
         other_options()
        else:
         print("record not found")
    if ch==3:
        break
           
   


