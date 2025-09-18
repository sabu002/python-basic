'''split() -string lai list ma convert garxa by default space ma split garxa
capitalize()-first letter capital garxa starting string ko matra
title()  -> first letter of each word capital garxa'''
# name = "  ---sujata @@ pathak 1 2 3__ " --> present value
# result =  "Sujata Pathak"
name = " ---sujata @@ pathak 1 2 3___"
new_name = name.strip(" -123_") .replace(" @@ "," ")     #output: "sujata @@ pathak  strip function le" replace pane use gareshe "sujata pathak aauxa"
print(new_name)
new_name_final = new_name.title() #output :"Sujata Pathak"-each word ko first letter capital garxa
print(new_name_final)
# first_name = Sujata and last_name = Pathak  banauna split use garxam r
first_name,last_name = new_name_final.split() #split le list ma convert garxa r 
# first_name  ma first element Sujata assign garxa r
# last_name ma pathak assign garxan
print(first_name)
print(last_name)
 
#  if name = ram bahadur thapa xa vane teslai first_name,middle_name r last_name ma split garna sakxam
name1 = "Ram Bahadur Thapa"
first_name1,middle_name1,last_name1 = name1.split()
print(first_name1)   #output:Ram
print(middle_name1)   #output:Bahadur
print(last_name1)     #output:Thapa
#    if name2  = ram#bahadur#thapa xa vane teslai split garna # use garxam # lai split garna specify garna parxa
name2 = "Ram#Bahadur#Thapa"
first_name2,middle_name2,last_name2= name2.split("#")
print(first_name2)
print(middle_name2)
print(last_name2)

name3 = "sujata pathak"
capital_name = name3.capitalize()
print(capital_name) # output:Sujata pathak (S capital vaxa suru ko string ko matra)

'''
name4 = "  __ firoj ##&& karki 123 @@
first_name = Firoj
last_name = Karki
'''
name4 = "  __ firoj ##&& karki 123 @@"
first_name4,last_name4 = name4.strip(" _123@").replace(" ##&&"," ").title().split()
print(first_name4)
print(last_name4)


phone_no = "(+977)9826363737"
new_phone_no = phone_no.replace("(+977)","")
print(new_phone_no) #output:9826363737

text = " $$ Samip ** % (+977)9826363737"
cleantext = text.strip(" $").replace(" ** % "," ").replace("(+977)","")
first_name5,phone_no5 = cleantext.split()
print(first_name5)
print(phone_no5)




