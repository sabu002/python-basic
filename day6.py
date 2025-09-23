'''
looping and iterative statements ->repeating a block of code multiple times. kunai pane code lai repetitive garnu parxa vane
for loop -particular condition hamle specify garxam tesanusar run garxa
while loop-jaba samma condition match hunna taba samma run vayerahanxa
'''
#for loop
fruits = ["apple","mango","kiwi","banana","graphes"]
for fruit in fruits:
    print(fruit)

# range function -range(starting index,ending value yo include hunna,steps=> by default 1 hunxa) 
my_list = list(range(1,11)) #hamle list ma convert garna parxa
print(my_list)

my_list1 = list(range(1,11,2)) 
print(my_list1)

r = range(5)
print(r)      #output:range(0, 5) 
print(type(r))   #output:<class 'range'>

# range function on loop
for i in range(1,21):
    print(i)

for i in range(1,21):
    print( i, end=" ")  #side by side print hunxa

    #for loop to print odd number from 1 to 20
for i in range(1,21):
    if i % 2 != 0:
        print(i)
        print()

 #next way
for i in range(1,21,2):
    print(i,end=" ") 
    print()

      #to print odd number

for i in range(0,21,2):
    print(i,end=" ")   #to print even number

fruits = ["apple","mango","kiwi","banana","graphes"]
for fruit in fruits:
    print(f"{fruit}: {len(fruit)}")

my_dict = {
    "1" : "apple",
    "2" :"banana",
    "3" :"mango"
}
for key in my_dict:
    print(key)   # key matra access garna milxa yessari
for k in my_dict:               #output:1:apple
    print(f"{k}:{my_dict[k]}")         # 2:banana
                                        #3:mango

#   by using count
fruits = ["apple","mango","kiwi","banana","graphes"]
count = 0
for fruit in fruits:          #output:1:apple
    count = count + 1          # 2:mango
    print(f"{count}:{fruit}")   #3:kiwi
                                #4:banana
                                 #5:graphes


# while loop
count = 0
while count <= 10:
    print("i am a happy soul")
    count +=1

# conditon true huda infinite loop chalxa
# while True:
#     print("happy")

 #break
for i in range(1,10):
    if i == 4:
        break
    print(i)

#continue- eauta particular iteratation matra matra skip garxa
for i in range(1,10):
    if i == 4:   #4 matra skip garxa aaru jasta ko testai print garxa
       continue
    print(i)
print()
  

for i in range(1,10):
    if (i == 4) or (i==5) or (i==6): #4,5r 6 skip garxa aaru run garxa 
        continue
    print(i)
print()


for i in range(1,10):
    if i in [4,5,6]:  # same mathi ko jastai 4,5r 6 lai skip garxa
        continue
    print(i)

#skip wala lai print garna ko lagi
skipped_list = []
for i in range(1,10):
    if i in [4,5,6]:
        skipped_list.append(i)
    print(i)
print(skipped_list)