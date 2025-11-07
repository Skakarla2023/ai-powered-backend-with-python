# A list is one of the built-in data structures in python where we store a group of items in a single variable.
# A list is an ordered collection of items where the items are indexed and changeable(add,change or remove)
# A lis can contain duplicate items also
mylist = ["focus","fun","career","life","focus"]
print(mylist)
print("\n")

# You can modify the items in the list
mylist[2]="joy"
print(mylist)
print("\n")

# Get the length of the list using len()
print(len(mylist))
print("\n")

# List items can be of any datatype
list1=[1,2,3,4]
list2=[True, False, False, True]
list3=["a","b","c","d"]
print(type(list1))
print(type(list2))
print(type(list3))
print("\n")

# The list() constructor
lista = list(('a','b','c'))
print(lista)
print("\n")

# Change values in a range
mylist[1:3]=["motivation","preserverance","grit"]
print(mylist)

# You can insert a new item in a list without modifying other values
mylist.insert(2,"dream")
print(mylist)

# Use append() to add items to the list, but append() adds items at the end of the list
mylist.append("courage")
print(mylist)

# To append elements from another list to the current list, use the extend() method.
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
mylist2=["belief","discipline"]
mylist.extend(mylist2)
print(mylist)

# You can delete list items using del,remove,pop and clear
mylist.remove("joy")
print(mylist)
mylist.pop(1)
print(mylist)
del mylist[4]
print(mylist)
mylist.clear()
print(mylist)

