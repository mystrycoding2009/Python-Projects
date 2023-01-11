# Calculator in Python 

def add(a,b):
        answer = a + b
        print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")  # Add Function


def sub(a,b):
        answer = a - b 
        print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")  # Sub Function
    

def mul(a,b):
        answer = a * b
        print(str(a) + " * " + str(b) + " = " + str(answer) + "\n") # Multiply function


def div(a,b):
        answer = a / b
        print(str(a) + " / " + str(b) + " = " + str(answer) + "\n") # Divide function

# Choosing Loop of the user input
while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Divide")
    print("E. Exit")
    choice = input("input your choice")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input your First Number"))
        b = int(input("input your Second Number"))
        add(a,b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input your First Number"))
        b = int(input("input your Second Number"))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input your First Number"))
        b = int(input("input your Second Number"))
        mul(a,b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input your First Number"))
        b = int(input("input your Second Number"))
        div(a,b)
    elif choice == "e" or choice == "E":
        print("Program Ended")
        quit()


#lets run the program