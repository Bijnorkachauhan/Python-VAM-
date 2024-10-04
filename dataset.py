# create a list, tuple, set, dict
# Add data pawan, manan, tanya, mukul
# delete pawan
# access all data
# update mukul to mukul sharma
# add manan and print the data

mylist=[]
mylist.append("pawan")
mylist.append("manan")
mylist.append("tanya")
mylist.append("mukul")
mylist.pop(0)
print(mylist)
mylist[2]="Mukul sharma"
print(mylist)
mylist.insert(3,"manan")
print(mylist)



print(" ")
names_set = {'pawan', 'manan', 'tanya', 'mukul'}
print(names_set)
names_set.remove('pawan')
print(names_set)
names_set.remove('mukul')
print(names_set)
names_set.add('mukul sharma')
print(names_set)
names_set.add('manan')
print(names_set)



print(" ")
names_tuple = ('pawan', 'manan', 'tanya', 'mukul')
names_list = list(names_tuple)
print(names_tuple)
names_list.remove('pawan')
names_list[2] = 'mukul sharma'
names_list.append('manan')
names_tuple = tuple(names_list)
print(names_tuple)



print("")
names_dict = {'pawan': 'pawan', 'manan': 'manan', 'tanya': 'tanya', 'mukul': 'mukul'}
del names_dict['pawan']
print(names_dict)
names_dict['mukul'] = 'mukul sharma'
names_dict['manan'] = 'manan'
print(names_dict)
