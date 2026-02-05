# MINI CALCULATOR

def calculator(a,b,operation):
    if operation=="+":
        return a+b
    elif operation=="-":
        return a-b
    elif operation=="*":
        return a*b
    elif operation=="%":
        if a>b:
            return a%b
        else:
            print("This is not possible")

    else:
        print("There is no other operation specified")

print(calculator(5,6,"+"))   