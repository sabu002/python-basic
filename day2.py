''' data cleaning using
lstrip()-- left side ko space hatauna use hunxa
rstrip()--right side ko space hatauna use hunxa
 strip()--allrounder use hunxa(lstrip r rstrip ko kam eakai patak ma garxa-first r last
   ko hatauxa but middle ko hataudaina middle hatauna replace nai use garnna parxa)
 replace()  --- string ko character lai aru character le replace garna use hunxa'''
  #name = "    ---- my ----sister's naem is sujata 1 23 __"-->present value
  #name= "my sister's name is sujata "==>after cleaning
name = "  sabita" #there is space in front of sabita so we have to clean it
new_name = name.lstrip()
print(new_name)
address ="kathmandu  " #space is at the end of katmandu
new_address = address.rstrip()
print(new_address)
  #if there is space on both side we can use lsrtrip and rstrip at the same time
my_name = "  my name is sabita  "
cleaned_name = my_name.lstrip().rstrip()# hamela ny_name.lstrip() garera ane paxi .rstrip() ne garna sakinxa
print(cleaned_name)
name1 = "sabita  ** khanal"
cleaned_name1 =  name1.replace("  ** "," ") #yesma "  **  " vako thau ma " " space le replace garxa
print(cleaned_name1)
#dheerai data huda pattern  specify garera pani apply garna sakinxa wa replace garna sakinxa
# starting ma space navayera arru huda jastai underscore __ huda
name2 = "__sabita"
cleaned_name2 = name2.lstrip("__") # yesma __ specify gare jasari nai specify garna parxa k remove garna cha tyo (specify nagare data clean hunna)
print(cleaned_name2)

new_name2 = "sabita__"
cleaned_name3 = new_name2.replace("__","")
print(cleaned_name3)

new_name4 = "__sabita--"
cleaned_name4 = new_name4.lstrip("__").rstrip("--")
print(cleaned_name4)

nam = " abcdef "
clean_nam = nam.strip() # first r last ko space hatauxa 
print(clean_nam)
my_nam = "1sabitakhanal2"
clean_nam1 = my_nam.strip("12")# ysema 1 r2 hatauxa yesma order specify nagare pane hunxa "21" lekhera pane hatauna sakinxa
print(clean_nam1)

sentance = "    ---- my ----sister's name is sujata 1 23 _"

''' duita step ma hataune 
step 1 - strip use garera first r last ko hataune
step 2- replace user garera middle ko hataune
'''
clean_sentance = sentance.strip(" -123_")
print(clean_sentance)
clean_sentance_final = clean_sentance.replace(" ----"," ")
print(clean_sentance_final)
 #hample single step ma ne garna milxa yeslai
clean_sentancee = sentance.strip(" -123_").replace(" ----"," ")
print(clean_sentancee)

name6 = "--- My name ___ is Ram 123 Karki __"
clean_name6 = name6.strip(" -_").replace(" ___ "," ").replace(" 123 "," ")
print(clean_name6)
