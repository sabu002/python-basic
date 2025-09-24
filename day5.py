'''conditional statement -> block of code kunai condition meet huda run garna xa vanne
if syntax: if condition:
            ane indentition diyera code particular condition match huda run hune wala code
if else
if elif......else
    nested
    match case statements
    '''

a = -5
if a > 0:
    print("the number is positive")

num = int(input("enter a number : "))
if num > 0:
    print("given number is positive")
else:
    print("given number is negative")

''' if condition:
      statement(s)
      elif condition:
      statement(s)
      .........
      else:
      statement(s)
 '''
num = int(input("enter a number : "))
if num > 0:
    print("given number is positive")
elif num < 0:
    print("fiven number is negative")
else :
    print("given number is zero")

    #program to check whether a given number is odd or even
no = 4
if no % 2 == 0:
    print("given number is even")
else:
    print
    ("given number is odd")

number = int(input("enter a number : "))
if number == 0:
    print("Given number is zero")
elif number % 2 == 0:
    print("given number is even")
else:
    print("given number is odd")

# greatest among three number
num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
num3 = int(input("enter a number : "))
if (num1 > num2) and (num1 > num3):
    print("num1 is  largerst")
elif num2 > num3 :
    print("num2 is greatest")
else:
    print("num3 is largest")
''' 
ch  = sddss
match ch:
case1:
add
case2:
sub
case3:
pro
.....
.....
case _:
print()

'''

num5 = int(input("enter a first number :"))
num6 = int(input("enter a decond number :"))
ch = int(input("1. for addition\n 2.for  substraction\n 3. for product\n"))
match ch:
    case 1:
        sum =  num5 + num6
        print(f"{num5}+{num6}={sum}")
    case 2:
        diff =  num5 - num6
        print(f"{num5}-{num6}={diff}")
    
    case 3:
         pro =  num5 - num6
         print(f"{num5}*{num6}={pro}")

    case _:
        print("wrong choice")


