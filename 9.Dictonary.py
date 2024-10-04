# Dictionary can store the data in key-value pair
#ordered, no duplicate, changeable
# name : Devansh

myInfo = {"name":"Devansh Ajmera","email":"d@gmail.com","mobile":"12345678","age":18,"name":"Devansh"}
print(myInfo)
print(type(myInfo))
print(myInfo["mobile"])
print("My name is" ,myInfo["name"],"mobile number is",myInfo["mobile"],"and age is", myInfo["age"], "and email is",myInfo["email"])
print(f"My name is {myInfo["name"]} mobile number is {myInfo["mobile"]} and age is {myInfo["age"]} and email is {myInfo["email"]}")

#to access the complete dictonary key...
for value in myInfo.keys():
    print(value)
#to access the complete dictonary value...
for value in myInfo.values():
    print(value)
# to upadate the values in dictonary...
myInfo["name"]="DEVANSH AJMERA"
myInfo["age"]=18
myInfo["email"]="d@outlook.com"
myInfo["mobile"]="12345678"
for i in myInfo.values():
    print(i)
print(" ")





myInfo.update({"gender":"male"})
for i in myInfo.values():
    print(i)


myInfo.pop("email")
print(" ")
for i in myInfo.keys():
    print(i)

del myInfo["mobile"]
print(myInfo)


