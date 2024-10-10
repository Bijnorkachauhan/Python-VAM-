import  numpy  as np

#assign array in numpy
myData = np.array([1,2,3,4])  
print(myData)  #[1 2 3 4]
print(type(myData))   #class 'numpy.ndarray'>

#update the data in array
myData[0] = 9
myData[1] = 10
myData[2] = 11
myData[3] = 12
print(myData)


# By For Loop
a = 9
for data in range(0,4):
    myData[data] = a + data
print(myData)


# By  using While Loop
i=0
x=12
while i < 4:
    myData[i] = x
    x=x-1
    i=i+1
print(myData)

#access the data from numpy array
for data in range(0,4):
    print(myData[data])
    
myFriends = np.array(["ivan","anshu","vani","anjali"])
for name  in myFriends:
    print(name) 
  
  
  #Reverse the array  
rev = np.flip(myFriends)
print(rev) 


myFriends.sort()
print(myFriends)
x = 3
while x>=0:
    print(myFriends[x])
    x = x-1



