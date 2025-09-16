# print("hello world") first python code
# number is variable jun ma value store hunxa
number = 1 #int
name= "kumar" #string
point=3.14  #float
is_true= True  #boolean
#  data type in python

# to run python ctrl+alt+m= terminal open hunxa 
print(number)
print(type(number)) #class int
print(name)
print(type(name))#class str
print (point)
print(type(point)) #class float
print(is_true)
print(type(is_true)) #class bool
# python is object oriented ho class r object hunxa
# comment jun code run hunna but yesma information hunxa jasle garda hamro code aru programmer le bujhna sajilo hunxa  single line lai # use hunxa multi-line comment ko lagi
'''
these is a multi line comment  vs code ma ctrl+ forward lash(/)
'''

#taking input from user
num1 = input("enter a number:")
num2 = input("enter another number:")
sum= num1 +num2
print(num1)
print(type(num1)) #class string
print(num2)
print(type(num2)) #class string
print(sum) #output 34 aauxa for num1 =3 r num2 =4 ma string concatenate vayera aauxa so type casting ko concept yaha use hunx
# concept of type casting
# int()   -integer function jasle aru data type lai integer ma convert garxa
# float() - yesle float ma convert garxa
# bool()   -yele boolean ma convert garxa
# str()   - yesle string ma convert garxa
# aba sum garna ko lagi string lai integer ma convert garna parxa so
a =  int(input("enter a first number:"))
b =  int(input("enter a second number:"))
sum = a + b
print(sum) # for a = 3 r b = 4 ma output 7  aauxa
print(type(sum))
  

# print garne diggerent way haru
print("these is first day of learning python")
print("these","is","first","day","of","learning","python") # both ko output same hunxa comma le space dinxa
print("these","is","first","day","of","learning","python",sep="#") # sep le space ma # le replace garxa by default eauta matra space hunxa
print("hello world")
print("hello","world")
print("hello",end = " ") #duita hunxa yeuta "sep" r "end" hunxa
# end ko default value "\n"->escape character vanxa jasle new line ma layjanxa but end = " " dida space paxi aarko connect vayera aauxa  aauxa output hello world nai aauxa
print("world")



# String
name= "sabita"
print("my name is",name)
num = 1 
print(f"number is {num}") #f strring vanxa jasle garda string print garauna sajilo hunxa
num1 = 4.62636
print(f"the name is{num1:.2f}") #2 ota decimal number samma matra aauxa output ma 4.62 aauxa
num5 = float(input("enter a number 1"))
num6 = float(input("enter a number 2"))
sum = num5 + num6
dif = num5 - num6
pro = num5 * num6
div = num5 / num6
mod = num5 % num6
qua =  num5 // num6
print(f"the sum is{sum}")
print(f"the difference of{num5},{num6} is{dif}")
print(f"the product of{num5},{num6}is {pro}")
print(f"the division of{num5},{num6}is {div:.2f}")
print("the modulos is",mod)
print("the quatient is",qua)
