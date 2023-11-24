print("")
print("_________________")
print("*****welcome to student management system*****")

sms=open("database.txt","a+")

def viewname():
    sms=open("database.txt","r")
    for i in sms:
        print(i)
    sms.close()

def addname():
    sms=open("database.txt","a+")
    a=input("enter the new student name:")
    a=a+'\n'
    sms.write(a)
    print("student name added")
    sms.close()

def removename():
    sms=open("database.txt","a+")
    a=input("search student name to remove:")
    a=a+'\n'
    sms=seek(0)
    rn=sms.readlines()
    if a in rn:
        rn.remove(a)
        print("remove student name from list",a)
        s=''
        s=''.join([str(i)for i in rn])
        f1=open('database txt','w')
        f1.close()
    else:
        print("student not found")
    sms.close()

def searchname():
    sms=open("database.txt","r")
    a=input("search student name:")
    readfile=sms.read()
    if a in readfile:
             print("student found",a)
    else:
        print("student not found")
    sms.close()

while True:
    print("         ")
    print("1. to view student list")
    print("2. to add new list")
    print("3. to remove the data")
    print("4. to search_name")
    print("5. exit")
    option=input("enter your choice:")
    if option=='1':
        viewname()
    elif option=='2':
        addname()
    elif option=='3':
        removename()
    elif option=='4':
        searchname()
    elif option=='5':
        exit()
    else:
         print("wrong input")
    g=input("do you want to continue this(y/n):")
    print("___________________")
    if(g=="y"):
        continue
    elif(g=="n"):
        break

























              
