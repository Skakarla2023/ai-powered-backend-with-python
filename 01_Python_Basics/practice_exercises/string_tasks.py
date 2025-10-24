s = "hello world"

print(len(s))

for x in s:
    print(x)


print(s[:1])
print(s[2:])
print(s[:-1])

print("is" not in s)

if "is" not in s:
    print(" is is absent in s")

# convert into uppercase
print(s.upper())

# convert into lowercase
print(s.lower())

# to remove whitespaces use strip()
print(s.strip())

# the replace function replaces a string with another string
print(s.replace("h","t"))


a = "hello"
b = "world"
# string concatenation
c = a+b
print(c)

c = a+" "+b
print(c)

# string formatting in python, 
# usually we cannot print numbers and string together in python, for that we use fstrings
cost = 59
txt = f"The bag costs {cost} rupees"
print(txt)

txt2 = f"The price is {cost:.3f} rupees"
print(txt2)

# to insert a special character inside a string use \(backslashes)
print("What's so \"special\" about VS")
