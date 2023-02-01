# As a dev, we need to obtain input data from the user and display the result back after doing the required operation with the data. 
 # To obtain data, we use input() function and to display it, we use print() function.

# We learnt about strings and thier formatting previously. Extensive string formatting may be verbose and might lead to errors and also the code may not be that easily readable
 # To minimise this problem, there is a feature introduced in Python 3.6 and later versions, which is called f-Strings
 # f-strings (Formatted String Literals) are string literals that have an f at the beginning anc curly braces containing expressions that will be replaced with their values.
  
  
# Here is an example program that covers the input functions and the fstrings
        # Self Introduction
        
f_name = input("First Name: ")
l_name = input("Last Name: ")
age = int(input("Age: " ))
designation = input("Designation: ")
company = input("Company: ")
experience = int(input("Experience in years: "))

intro = f"""Hi everyone, My name is {f_name.capitalize()} {l_name.capitalize()}.
I am {age} years old and I have been working as {designation.capitalize()}
for over {experience} years in {company.capitalize()} company.
By the end of this year, I'll be promoted to next level.""" 
print(intro)

