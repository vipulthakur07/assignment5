#Question-1 (Leap year)
a=int(input("enter a year :"))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("It's a Leap year")
        else:
            print("Not a Leap year")
    else:
        print(" It's a Leap year")
else:
    print("Not a Leap year")

#Question-2 (Square or Rectangle)
len=int(input("enter length :"))
bre=int(input("enter breadth :"))
if len==bre:
    print("It's a square")
else:
    print("It's a rectangle"

#Question-3 (Age)
a=int(input("age of 1st persion :"))
b=int(input("age of 2nd person :"))
c=int(input("age of 3rd persion :"))
if a>b and a>c:
    print("first person is oldest")
elif b>a and b>c:
    print("second person is oldest")
else:
    print("third person is oldest")
if a<b and a<c:
    print("first person is youngest")
elif b<a and b<c:
    print("second person is youngest")
else:
    print("third person is youngest")

#question-4(work)
age=int(input("enter your age :"))
sex=input("sex?")
st=input("marital status?")
if (age>60 and age<20):
    print("Age must be between 20 and 60 years.")
else:
    if sex=='female':
        print("you'll work only in urban areas.")
    else:
        if age>20 and age<40:
            print("you can work anywhere.")
        else:
            print("you'll work only in urban areas.")

            
#Question-5 (shop)
quantity=int(input("enter the quantity :"))
quantity=quantity*100
if quantity>1000:
    quantity=quantity-(quantity*0.1)
print("Total Cost: Rs",quantity)

#Question-6 (Input integers)
a=[]
for i in range(0,10):
    b=int(input(""))
    a.append(b)
print(a)


#Question-7 (infinite loop)
a=0
while a==0:
    print("i am infinite")

#Question-8 (Square of list)
a=[]
b=[]
for i in range(0,3):
    num=int(input(""))
    a.append(num)
    b.append(num*num)
print(a)    
print(b)

#question-9(String , float, integer)
a= ['hey', 1,2,3,4,1.1,1.,1.3]
integers=[]
strings=[]
floats=[]
for i in range(0,8):
    if isinstance(a[i], int):
        integers.append(a[i])
    elif isinstance(a[i], str):
        strings.append(a[i])
    else:
        floats.append(a[i])
print(integers)
print(strings)
print(floats)

#question-10 (Range)
a=[]
for b in range(1,101):
    flag=0
    if b==2:
        a.append(b)
    else:
        for i in range(2,b):
            if b%i==0:
                flag=1
                break;
            else:
                flag=0
        if flag==0:
            a.append(b)
a.remove(1)
print(a)

#question-11 (Pattern)
for i in range(0,4):
    for j in range(0,i+1):
        print("*",end='')
    print("\r")


#question-12 (search and delete)
a=[]
for i in range(0,5):
    num=int(input(""))
    a.append(num)
num=int(input("enter the number you want to delete :"))
a.remove(num)
print(a)
