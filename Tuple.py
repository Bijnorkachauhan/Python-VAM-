# Tuple is used to store multiple data
# Ordered: Tuples maintain the order of elements. The first element index is 0
# Immutable: Once a tuple is created, its elements cannot be changed, added, or removed.
# Allow Duplicates: Tuples can contain duplicate values.
# Indexed: Elements in a tuple can be accessed using their index.
# Heterogeneous: Tuples can store elements of different data types (e.g., integers, strings, floats).


# Creating a tuple
my_tuple = ("apple", "banana", "cherry", "apple", 42, 3.14)
# Accessing elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
# Checking the length of the tuple
print("Length of the tuple:", len(my_tuple))
# Slicing a tuple
print("Sliced tuple (first three elements):", my_tuple[:3])
# Checking for an element in the tuple
if "banana" in my_tuple:
    print("Banana is in the tuple")
# Cannot modify elements..