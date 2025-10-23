# Python Variables and Datatypes

<img width="1503" height="358" alt="image" src="https://github.com/user-attachments/assets/9330bee5-0e2c-4798-a738-9bcd655d7577" />

```python
a = 5
print(a)

b = 5.6
print(b)

c = 0
print(c)
```

<img width="1298" height="53" alt="image" src="https://github.com/user-attachments/assets/25562fea-be7d-4afe-a1ff-c05ac9c1d978" />

```python
x = 4
print(x)
x = "Sally"
print(x)
```

Output:

```
x
Sally
```

<img width="1297" height="141" alt="image" src="https://github.com/user-attachments/assets/6bf24851-e0ab-49df-a202-09abb32d8ab5" />

```python
x = int(2.0)
y = float(12)
z = str(33)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))
```

Output:

```
2
12.0
33
<class 'int'>
<class 'float'>
<class 'str'>
```

<img width="1294" height="135" alt="image" src="https://github.com/user-attachments/assets/459cf9d9-2643-4da3-8023-3ab447037b2d" />

<img width="1906" height="380" alt="image" src="https://github.com/user-attachments/assets/9b57bd80-1e7a-4a55-842a-405bc7714361" />

<img width="1289" height="130" alt="image" src="https://github.com/user-attachments/assets/b58e3949-57cb-469c-a950-6d946c91020d" />

<img width="1311" height="364" alt="image" src="https://github.com/user-attachments/assets/f4cd52b3-a63c-4893-9200-144160b3dc37" />

<img width="1296" height="100" alt="image" src="https://github.com/user-attachments/assets/16d9299e-ff79-4e56-b0e3-28e5a6485233" />

<img width="1243" height="174" alt="image" src="https://github.com/user-attachments/assets/b207b1ff-decd-4577-9073-1b373087c032" />

<img width="1264" height="662" alt="image" src="https://github.com/user-attachments/assets/26803fd0-bab3-402b-a5dc-99233f50af6c" />

<img width="1257" height="183" alt="image" src="https://github.com/user-attachments/assets/a3a2f394-4af5-4b41-96f5-a2aa9f62681a" />

```python
x = 1

def func():
	print("Number:",x)
    
func()
print(x)
```

Output:

```
Number: 1
1
```

<img width="1232" height="71" alt="image" src="https://github.com/user-attachments/assets/5e809b68-9ada-4c75-9b0a-5890f5b98d37" />

```python
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
```

<img width="1267" height="169" alt="image" src="https://github.com/user-attachments/assets/b0a962c7-fd85-41ef-bbcd-3f74235b8fd1" />

```python
x = "awesome"
print("# outside the function")
print("Python is ",x)

def func():
    global x
    x = "fantastic"
    print("# inside the function")
    print("Python is ",x)
        
func()
```

Output:

```
# outside the function
Python is  awesome
# inside the function
Python is  fantastic
```

<img width="1247" height="592" alt="image" src="https://github.com/user-attachments/assets/710f7913-8425-4822-a0c4-55bca36ac842" />
