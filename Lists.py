def printNamelist(argNamelist):
    for name in argNamelist:
        print(name)

myNamelist = ["Aung Aung","Hla Hla","Mya Mya"]

print(len(myNamelist))

print(myNamelist[2])

printNamelist(myNamelist)

myNamelist[0]="Aung"

printNamelist(myNamelist)