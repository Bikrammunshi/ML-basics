global room
global revenue

room={}
revenue={}

def hostel():

    print("------------WELCOME TO OYO----------")
    print("Enter 1 to start booking \t")
    print("Enter 2 to check if rooms are available \t")
    print("Enter 3 to get the revenue form the rooms \t")
    print("Enter 4 to get the room details \t")
    print("Enter y to enter your choice and enter no when you dont wanna enter anymore")
    y=input()
    while y=="y":
        ch=int(input("->"))
    
        if ch==1:
            print(" ")
            booking()

        elif(ch==2):
            print(" ")
            check()

        elif(ch==3):
            print(" ")
            fees()
    
        elif(ch==4):
            print(" ")
            details()

        else:
            exit()
        print("Enter y to enter your choice and enter no when you dont wanna enter anymore")
        y=input()
    

def booking():
    
    detail=[]
    k=len(room)+1
    fee = 0
    if len(room)<=20:
        i = eval(input("Enter the number of boarder you want to enter now \t"))
        if i>4:
            print("Sorry right now only 4 can be alloted max to one room enter the remaining to next room \t")
            print("Room left \t",20-len(room))
            exit()
        days = eval(input("Enter the numbee of days the boarder want to stay \t"))
        if i>2:
            fee += days*500*(i-1)
        else:
            fee += days*500
        while (i>0):
            name = input("Enter the name \t")
            sex = input("Enter the sex/gender nothing like 'karwa do' \t")
            age = input("Enter the age \t")
            number = input("Enter the phone number \t")
            detail.append([name,sex,age,number])
            i = i-1
        room.update({k:detail})
        revenue.update({k:fee})
    else:
        print("SORRY CURRENTLY NO MORE ROOM LEFT")
        
    

def check():
      if len(room)==20:
            print("SORRY NO MORE ROOM LEFT")
            return False
      else:
            print("ROOM IS LEFT \t",20-len(room))
            return True

def fees():
    pay=0
    for i in range(len(revenue)):
        y = int(revenue.get(i))
        pay= pay+y
        
    print("The payment earned from all the rooms is \t",pay)
    
def details():
    n=int(input("Enter the room number you want to get the details of "))
    detail=room.get(n)
    for i in range(len(detail)):
        print("Name \t",detail[i][0])
        print("Sex \t",detail[i][1])
        print("Age \t",detail[i][2])
        print("Contact Number \t",detail[i][3])
        
        
        
d=input("Enter the date: ")
date="DATE: "+d+"\n"
hostel()   
hostelfile=open('hf.txt','r+')
hostelfile.write("------------------OYO FILES--------------- \n")
hostelfile.write(d)
for i in range(len(room)):
    rooms="Room "+str(i+1)+":"+"\n"
    hostelfile.writelines(rooms)
    detail=[]
    detail=room.get(i+1)
    for j in range(len(detail)):
        names="Name \t"+detail[j][0]+"\n"
        sex="Sex \t"+detail[j][1]+"\n"
        age="Age \t"+detail[j][2]+"\n"
        contact="Contact Number \t"+detail[j][3]+"\n"
        hostelfile.write(names)
        hostelfile.write(sex)
        hostelfile.write(age)
        hostelfile.write(contact)
        hostelfile.write("\n\n\n")
    
    fee="Fees for room: "+str(i)+" is "+str(revenue.get(i+1))
    hostelfile.write(fee)
    