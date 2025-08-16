import os
import platform
import time
import sys
def clear():
    command = 'cls' if platform.system().lower() == 'windows' else 'clear'
    os.system(command)
def calc(a, b, symbol):
    if(symbol=="/"):
        return a/b
    elif(symbol=="*"):
        return a*b
    elif(symbol=="+"):
        return a+b
    elif(symbol=="-"):
        return a-b
    else:
        return None
game_state=True
def matheng(symbol):
    if(symbol=="/"):
        return "quotient"
    elif(symbol=="*"):
        return "product"
    elif(symbol=="+"):
        return "sum"
    elif(symbol=="-"):
        return "diffrence"
    else:
        return None
dict1={
    'arthemetic' : '1',
    'temperature' : '2',
    'converter'    : '3',
}
dict2={
    'HCF'    :'4',
    'LCM'    : '5',
    'Quadratics' : '6',
}

print("Hello!")
print("Welcome to Calculator!")
print("ASCII")
print(f"""MODES:
{
    dict1
}\n
Others:
{
    dict2
}\n""")
mode = input("Enter mode:\n")
while game_state==True:
    if(mode == "1"):
        symbol = input("Enter mode:(/,*,+,-)")
        m=float(input("enter first number"))
        n=float(input("enter second number"))
        print(f"{calc(m, n, symbol)} is the {matheng(symbol)}.")
        usin=input("continue?")
        if usin.lower()=='y':
            continue
        else:
            print("Thanks!bye!")
            break
    else:
        print("Sorry, Not available!")
        sys.exit()
    