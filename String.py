# '#' is for comments, just like this line. Just for the reference. Does'nt involve while running the code
# Strings in Python are surrounded by either single quotes or double quotes. Anything that is between ' or " is considered a text by Python.
# To write muiltiple lines of text, we should use the double quotes three times """

a = """  Lorem ipsum dolor sit amet,
consectetur adipiscing elit.
sed do eiusmod tempor incidunt.  """
print(a)

#Python indexing starts from 0. That means the first character in a string has the position 0 and it continues to 1, 2, 3,...
#Use square brackets[] to access a particular element of the string. Give the element's index number in the [] brackets.

print(a[6])

#Use len() funcction to return the length of a string

print(len(a))

#Use 'in' keyword to check if a certain phrase is present in a string. It returns Boolean value.

print("elite" in a)
print("elit" in a)

# id() function gives the unique location of the given object
# dir() function gives all the properties of the given object

print(id(a))    #By using the id function, we can see that the memory location address of the object is unique when you assign a different value to the same variable.
print(dir(a))        #This proves that the string is immutable which means a string value cannot be updated

# Slicing in Python can return a range of characters. The syntax is like variable followed by square brackets, inside the brackets specify the index number from where
 #the slicing should start and then the range of how many characters you need, both separated by a column

print(a[2:12])
 
 # If you specify no index and give only the range after the column, slicing starts from beginning i.e 0
 # Similarly, if you specify no range but only index, then slicing will happen upto the last character

# String Modification
 # upper() returs the string in upper case, lower() returns the string in lower case

print(a.upper())
print(a.lower())

 # strip() removes any white spaces in the beginning or the end
print(a.strip())

 # replace() method replaces a string character with the given one
print(a.replace("e", "f"))
 # To find out how many times a character is repeated in a string, use count() function
print(a.count("e"))

 # split() method splits the string into substrings if it finds instances of the separator

b = a.split(",")
print(b)  

# String Concatenation. Use + to concatenate two strings
b = "Ut enim ad minim veniam, quis nostrud exercitation"
c = a + b
print(c)

# Reverse a string. There is no built in function to reverse a String in Python
 #So, the best practice is to slice the string backwards as follows [::-1]

print(b[::-1])
 