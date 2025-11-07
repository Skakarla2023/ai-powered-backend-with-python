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

# Loop through list items using for loop or while loop
mylist=[1,2,3,4,5,6,7]
for i in mylist:
    print(i)
for i in range(len(mylist)):
    print(mylist[i])
i=0
while i<len(mylist):
    print(mylist[i])
    i=i+1

# You can sort a list by using sort() function
list1=[6,3,5,1,8,9,4]
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

def myfunc(n):
    return n-1
    
list2=[34,68,32,90,55,12,14,5]
list2.sort(key=myfunc)
print(list2)


# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

# You can use the reverse function to reverse a list
list2.reverse()
print(list2)

# You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


# Join 2 liss using the + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
