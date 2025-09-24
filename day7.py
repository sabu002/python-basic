# function- block of a code that perform a specific task, rub only when we called it .yesle reusability badhaucha ,code organized hunxa r debugging ma help garxaa
''' syntax: def function_name():
         // code of block
         '''
# execute garna ko lagi call garnu parxa function
# simple progarm to tp print hello world using function
def hello():          #function defination
    print("hello world")
hello()               #function calling

# program that greets the user using function
def greet(n):  #n = name hunxa mainly name nai lekhxam but
    print(f"welcome {n}")
name = input("Emter your name : ")
greet(name)

#yesari nme garna milxa using main function
def main():
    nam = input("Emter your name : ")
    gree(nam)
def gree(n):  #n = name hunxa mainly name nai lekhxam but
    print(f"welcome {n}")

main()

# parameter ma default value rakheko kehi naidida sabita dinxa
def greeting(namee = "sabita"):
    print (f"hello! {namee}")
namee = input("Emter your name : ")

greeting()
greeting(namee)

#task 2 temperature converter celsius to farenhite
def convert_temperature(celsius):
    farehnite = (celsius*1.8)+32
    return farehnite
# farenh = convert_temperature(34)
# print(farenh)
print(f"temperature in fahrenhite: {convert_temperature(34)}")

# taking input from user
def convert_temperature(celsius):
    farehnite = (celsius*1.8)+32
    return farehnite
celsius = int(input("enter a temperature in celsius: " ))
print(f"temperature in fahrenhite: {convert_temperature(celsius)}")

#program to find maximun number among three no.
def maximun(a,b,c):
    # return max(a,b,c)
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

a = int(input("enter a number: "))
b = int(input("enter a number: "))
c= int(input("enter a number: "))
print(f"the largest number among {a},{b},{c} = {maximun(a,b,c)}")


# buld a simple calculator that perform addition, sunstraction, multiplication and division according to the user input using the concept of functional programming

def sum(a,b):
    return a+b
def  diff(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return "Division ny zero error"
  
        return a/b
    
print("simple calculator")
choice = input("Enter a choice 1/2/3/4 : ")
a= int(input("enter a number"))
b= int(input("enter a number"))
if choice == "1":
    print(f"{a}+{b} = {sum(a,b)}")
elif choice == "2":
    print(f"{a}-{b} = {diff(a,b)}")
elif choice == "3":
    print(f"{a}*{b} = {mul(a,b)}")
elif choice == "4":
    print(f"{a}/{b} = {div(a,b)}")
else:
    print("wrong choice")





  
  
