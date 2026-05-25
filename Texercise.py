print("hello python")

Name = "Bob"
print(Name)
Age = 18
print(Age)
Country = "Myanmar"
print(Country)


Variable = {
    "Studentname" : "Bob",
    "Studentage"  : "18",
    "coursename"  : "python basic",  }

print(Variable)

print(Variable["Studentname"])

Variable["Studentage"]="16"

for i in Variable:
    print(i)
    print(Variable[i])


num1 = 50
print(num1)
num2 = 100
print(num2)



Name = input("enter your name")
age = input("enter your age")

print('hello' ,Name)

print("you are 20 years old", age)
print("you are" , age , "years old")


favcolour = input("enter you fav colour")

print("your fav colour is",favcolour)


A =10

B =20

print(A+B)
print(B-A)
print(A*B)
print(A/B)


Mark = int(input('enter your mark'))
if Mark >= 50:

    print("pass")

else:
    print("fail")

Age = int(input('enter your age'))
if Age >= 18:
    print('adult')
else:
    print('teen')

for i in range(10):
    print(i)


for Bob in range(5):
    print("Bob")


i =1
while i<=10:
    print(i)
    i +=1


fruits = ['berry','cherry','banan','strawberry',"watermelon",'apple']

print(fruits)

print(fruits[0])
print(fruits[-1])
 

Studentsname = ['Big','Bob','Ben','Boy','Bet']

for Name in Studentsname:
    print(Name)


User = { 
    'name' : "Bob",
    'age'  : "18",
    'corse': "python basic",
    }
print(User['name'])

print(User)


def hello(something):
    print("hello" , something)


hello("big")

def welcome(something):
    print("welcome",something)

welcome("world")   

def add():
    num1 = 20
    num2 = 20
    print(num1+num2)

add()

def add():
    A = 20
    B = 60
    print(B-A)

add()

def add():
    A = 20
    B = 20
    print(A*B)
add()

def division():
    A = 10
    B = 20
    print(A/B)
division()