var = "hello"
print(var)
print("hello \nworld")
print("hello \tworld")
print(len("I am hungry"))
print(len(var))

# slicing
mystring = "Hello World"
print(mystring)
print(mystring[0])
print(mystring[-1])
newstring = "abcdefghijk"
print(newstring[3:6])
print(newstring[6:9])
print(newstring[::2]) #pulando dois caracteres - start:stop:step size

# string property and methods

name = "Sam"
name = "P" + name[1:]
print(name)
letter = "z"
letter = letter * 5
print(letter)

#Methods

print(newstring.upper())
print(newstring.lower())
print(mystring.split())

# Print Formatting and Strings

print("This is a String {}".format("INSERTED"))
print("The {} {} {}".format("fox", "brown", "quick"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
print("My name is {n} {s}".format(n="Felipe", s="Tocchetto"))
print("My Pets name are: {dog} and {cat}".format(dog = "Pablo", cat = "Carmen"))
