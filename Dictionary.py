myDiction = {
    'name': 'Aung',
    'age' : 16,
    'adress': 'Yangon',
}

print (myDiction)

print (myDiction["adress"])

myDiction["adress"]="Tachileik"

for i in myDiction:
    print("i is",i)
    print(myDiction[i])