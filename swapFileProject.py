from re import A


def swapFile():
    name = input("File 1: ")
    name2 = input("File 2: ")

    with open(name,'r') as a:
        dataa = a.read()

    
    with open(name2,'r') as b:
        datab = b.read()
    

    with open(name, 'w') as  a:
         a.write(datab)

    with open(name2, 'w') as  b:
         b.write(dataa)
        
    print("The swap has happened")

swapFile()



   