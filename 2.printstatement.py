
#Typecasting convert one data type to another data type.
price = 90.59
print(price)
print(type(price))

#convert to integer
payPrice= int(price)
print(payPrice)
print(type(payPrice))

#Convert int into string.
amount = 2500
stringAmount=str(amount)
print(stringAmount ,"and data type is ", type(stringAmount))
print("")



# #Convert string into int.
# gender="male"
# genderIntoInt = int(gender)
# print(gender,"and data type is ", type(gender))   #Conversion not possible because sting doesnt have a ascii number.
# print("")




#To take the input from user C language scanf
myName = input("Enter your name: ")
#input function has default return type as str.
myAge = input("Enter your age: ")   #......as a string.....
print("My name is ", myName , "and age is", myAge)

#Find the age in years. Then, born year and current year, given by user.
CurrentYear = int(input("Enter the current year:"))
bornYear = int(input("Enter the Born year:"))
age = CurrentYear - bornYear
print("The age is: ",age)




age=18
name="Devansh Ajmera"
salary=2599.89

#Show to pass the variable inside the print statement. 
#we have three ways to pass the variables to print statement.
#print("My name is " + name + " and salary : "+ salary + "and age : "+ age)

#Solution 1: replace + by , when data type is not string.
print("My name is",name ,"salary:",salary ,"and age:",age)

#Solution 2:  pass the variable in print statement with f{}
print(f"My name is {name} salary: {salary} and age: {age}")

#Solution 3: typecast the data into string
salaryString = str(salary)
ageString= str(age)
print("My name is " + name + " salary: "+ salaryString + " and age: "+ ageString)

#To find the type of data we need to use type() function.
print(type(name))
print(type(age))
print(type(salary))
print(type(name))
print(type(ageString))
print(type(salaryString))



#Currency Converter Rupees to USD, 1 USD equal to ₹84.
usd=int(input("Enter the currency in dollars: "))
rs=usd*84
print("USD = ",usd,"Rupees = ",rs)
print("")