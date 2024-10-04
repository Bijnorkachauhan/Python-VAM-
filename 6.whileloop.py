
#while loop is used to perform iteration until condition will false

#print the no from 1 to 10 using while loop
x=1

while x < 11:
    print(x)
    x=x+1
print(" ")
#WAP to print the no from 10 to 1 using while loop
y = 10
while y > 0:
    print(y)
    y=y-1
print(" ")



# #WAP to print the pattern using while loop  1,3,5,9,11
# a=1
# while a < 12:
#     if a == 7 :
#         print()
#     else:
#         print(a)
#         a = a+2

a=1
while a < 12:
    if a !=7 and a % 2 == 1:   #a % 2 != 0:
        print(a)
    a = a + 1
