'''
Data structure -set of container jas ma value hunxa jaslai manipulate garna sakinxa ane access ne garna sakinxa
list,
frozenset,
sets,tuple,
dictionary'''
# list -> mutable data structure(modify garna sakinxa)
# tupple => immutable data structure(modify garna mildaina)
# sets => unique value hunxa ane unordered(index bata access garna mildaina) 
# dictionaries-> key value pair ma hunxa ane key jahila uniue hunxa
# jastai "name":"sabita",
# "ph_no":637475475 yo immutable hunxa list lai key ma rakhna mildaina but as a value ma rakna milxa but tupple lai as a key ma rakhna milxa 

#List
 #list =[1,2,3,4"sabita",True,3.5]
 # empty_list = []
l1 = [1,2,4,5,"samip",True,3.5]
print(l1)      #output:[1, 2, 4, 5, 'samip', True, 3.5]
print(l1[3])   #output:5
print(type(l1))  #output:<class 'list'>:

el = []
print(el)       #output:[]
print(type(el))  #output:<class 'list'>

#indexing of list -> particiular element lai nikalna ko lagi
''' 0 bata start hunxa
[0,1,2,3,4......] for positive ko lagi neagtive index ko lagi last bata -1 bata start hunxa
if we have n no. of element in a list
the range of index is 0 to (n-1) samma hunxa 
if we have 10 elements range 0 to (10-1)=9 samma hunxa
'''
l3 = ["ram","sabita","kalyann",True,4,5.6]
print(l3[2])          #output: kalyann
print(type(l3[2])) 
print(l3[-2])    #output:  <class 'str'>
#-1 index gives the last element yesbata last to element easily access garna sakinxa

x = [1,2,3,4,5,6,7,8,9]
sqr_x = [ a **2 for a in x] #list compression => eauta list  bata particular operation perform garera naya list banauna sakinxa
print(x)      #output:[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sqr_x)   #output: [1, 4, 9, 16, 25, 36, 49, 64, 81] naya list create hunxa square gareko wala ko


l4 = ["ram","sabita","kalyann",True,4,5.6,"nepal","python","happy","Numbpy",3,2,13,7.55]
'''
last element
second last element
the fifth element
'''
print(l4[-1])
print(l4[-6])
print(l4[4])
print(l4[len(l4)-1]) #last element dinxa

#Slicingg list[starting index:ending index] ensing index samma print hunna matlab include hunna 
print(l4[1:6])
print(l4[3:]) # 3 index bata last samma ko dinxa 
#if eauta matra index r colon(:) diyam vane tehi index bata start hunxa
print(l4[:])  # : [:] yo matra  lekhda purai list nai print hunxa
print(l4[:3])  #[:3] starting bata matlb [0]  ondex bata start hunxa last index include navaye aaru print hunxa
print(l4[-4:])
print(l4[-7:-5])
print(l4[-13:])
print(l4[1::2])



# list function/method  = given list ma nai change gardixa
# 1. append -> last ma elemtnt thapne kam garxa  suntax:
# list.append("elemets naya thapne wala")
# 2. insert -> index anusar add garxa   syntax: list.insert(index,"thapna parne value")
# 3. sort -> aarenge garne order ma
# 4.reverse
# 5 pop -> remove a last element ane value return  garxa
# 6, remove-> value remove garna milxa jun  paranthesis() bhitra send garxam tyo vakue start bata herda xitoo vetayenxa tehi remone garxa ("ram") ram remove garxa list bata
l4.append("khanal")
print(l4)
print(l4.append("fruits"))
print(l4)   #output:['ram', 'sabita', 'kalyann', True, 4, 5.6, 'nepal', 'python', 'happy', 'Numbpy', 3, 2, 13, 7.55, 'khanal', 'fruits']  fruits last ma add hunxa
l4.insert(2,"ghimiree")  #2 index ma ghimiree add hunxa
print(l4)


my_list =[23,43,66,43,56,45]
my_list.sort()
print(my_list)  #output:[23, 43, 43, 45, 56, 66]
my_list.sort(reverse=True) ##output:[66, 56, 45, 43, 43, 23] desending ma print garxa
print(my_list)

# without changing original list sirting can be done 
l5=[1,3,4,5,6,7]
temp = l5
print(l5)
temp.sort()
print(temp)

# each element lai xutta xuttai acess garne through loop
l5=[1,3,4,5,6,7]
for i in range(len(l5)):
    print(l5[i])

# revere garna ko lagi
print(l4[::-1]) #both reverse garna use hunxa 
l4.reverse()
print(l4)

print(l4.pop())  #last element remove hunxa r pop le delete vako return ne garxaa
print(l4)

l4.remove("kalyann") # kalyann remove garxa list bata
print(l4)
l4.clear() #list lai nai clear gardinxa 
print(l4)  #output:[]  empty list auxa

'''Tuples => immutable hunxa change,add modify,remove garna mildaina  indexing and slicing same as tupple
function/method
1. count()  kate ota value xa count garxa
2.index() index return garxa
'''
my_tupple = (3,5,3,78,3,56,33,"ERAm",True,"happy")
print(my_tupple)
t1 = () #empty tupple
print(t1)
t2 = (1)
print(t2)
print(type(t2))  # output: integer aauxa kina vane tupple huna lo lagi comma le seprate garnu parxa 
# if tupple1 = (1,) vane matra tupple hunxa eauta value ko
# my_tupple[2] = 4   #yesari value change garna mildaina
# print(my_tupple)
print(type(my_tupple))  #output:<class 'tuple'>
num = my_tupple.count(3)  #count(1) rakhda True ko value ne 1 count garxa
print(num)
index3 = my_tupple.index(3)
print(index3)

# Set  -> stores unique values ane unordered hunxa(indexing hunna)
my_set = {1,2,64,2,4,2}
my_set1 = (1)
print(my_set1)
print(my_set)    #output:{64, 1, 2, 4}  value duplicate hunna

print(type(my_set))   #output:<class 'set'>

# function/method in set
#add()  value add garxa set ma but kaha garxa thaha hunna
# remove()  jun value dinxam tyo remove garxa
my_set.add(65)
print(my_set)
my_set.remove(1)
print(my_set)


#dictionaries -{"key":"value"} pair ma hunxa key unique huna parxa r immutable huna paryo
dict = {}  
print(dict)
print(type(dict))
dict1 = {
    'name' : 'sabita',
    'address' : 'bhaktapue',
    'hobby' : 'singing'
}
print(dict1)
print(dict1.keys()) # .keys le key matra dinxa dictionary ko
print(dict1.values()) #values matra dinxa

