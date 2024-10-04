# #list is used to store multiple data.
# #list store different type of data like int, string, float.
# #list can contain duplicate data.

# #create a list and store your friends name
# friendsName=["ivan","anshu","anjali","wani",33,26,28,5]

# #to access the data from list
# #to get the single data from list --> listVariableName[indexNo]
# print(friendsName[3])

# #to print the complete list
# for name in friendsName:
#     print(name)

# #operation on list ->
# #Append will add data at the last of the list
# friendsName.append("Naman")
# #insert will add the data based on the index no.
# friendsName.insert(0,"Devansh")
# friendsName.insert(18,"Devansh")       #store at the last of list
# #to print the complete list
# for name in friendsName:
#     print(name)






# friendsName=["ivan","anshu","anjali","wani",33,26,28,5]
# #to remove the data from list
# friendsName.remove("ivan")
# friendsName.remove("anjali")

# #to remove data using pop
# friendsName.pop()   #DELETE LAST VALUE.
# friendsName.pop(1)     #at particylar index.
# #to print the complete list
# for name in friendsName:
#     print(name)

# #to reverse the list
# friendsName.reverse()
# for name in friendsName:
#     print(name)
# print(" ")

# #to delete the complete list
# #friendsName.clear()







# #to print the complete list
# friendsName=["ivan","anshu","anjali","wani"]
# friendsName.append("rahul")
# friendsName.append("rohit")
# friendsName.append("kanak")
# # for name in friendsName[1:3]:   # 1 starting index, 3 endindex - 1
# for name in friendsName[2:6]:      # 2 included   6 not include
#     print(name)





friendsName=["ivan","anjali","anshu","wani"]
friendsName.append("rahul")
friendsName.append("rohit")
friendsName.append("kanak")
friendsName[0] = "ivan sharma"      # to update the value of a data.
print(friendsName)
friendsName.sort()                  # sort works only for char, string values...
for name in friendsName[:-1]:       #   (: print all ), ([-4:1] wani, rahul, rohit ), ([:-1] skip last.)
    print(name)

#to get the type
# type(mylist)

#Write a program to add 10 student name in list, Remove last value.
#Reverse the list

name=["Devansh","Prince","Viyom"]
name.append("Piyush")
name.append("Ayush")
name.append("Aryan")
print(name)