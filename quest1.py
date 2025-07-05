
#class of integer is coi
def coi(a):
    if(a>0):
        print(f"{a} is a positive integer")
    elif(a ==0):
       print(f"{a} is zero")
    else:
        print(f"{a} is a negative integer")
#class of natural number is con
def con(a):
    int(a)
    if(a % 2 ==0):
        print(f"{a} is an even number.")
    else:
        print(f"{a} is a odd number.")
#divisible by six is ds
#you can modifiy to divisible by any number using prime factors!...although it may be tedious.
def ds(a):
    if a % 2 == 0:
        if a % 3 == 0:
            print(f"{a} is divisible by 6")
        else:
            print(f"{a} is not divisible by 6")
    else:
        print(f"{a} is not divisible by 6")
v=int(input("Enter a number to begin:"))
coi(v)
con(v)
ds(v)