# Assignment 2
# Name: Peyush Jindal
# SID: 21103092


#Question.1

input_string="Python is a case sensitive language"

# (a) part
# To find the length of the input string.
# We will use inbuilt funtion len()

print("a. Length of string is:",len(input_string))

# (b) part

# To reverse the order of the string in one line code.
#  we will use slicing method

print("b. Reversed string is:",input_string[::-1])

# (c) part
# Using Slice function store “a case sensitive” in new string.
# index of 'a' is 10 and index of 'e' in sensitive is 25

new_string=input_string[10:26]   

# printing new_string

print("c.",new_string)

# (d) part
# To replace “a case sensitive” with “object oriented”
# We will use a inbuit funtion  replace()

print("d.",input_string.replace('a case sensitive', 'object oriented'))

#(e) part
# To find index of substring “a” in the given input string.
# We will use find() function

print("e. The index of substring a is:",input_string.find('a'))

# (f) part
# To remove the white spaces from the given input string.
# We will use replace() function

print("f. The new string after removing white spaces is:",input_string.replace(" ",""))


# Question 2

# Store your name, SID, department name and CGPA into different variables.
# With the help of String formatting

Name = "Peyush Jindal"
SID = 21103092
CGPA = 9.9
Department = "CSE"

print("Hey, %s Here!" % Name)
print("My SID is %d" % SID)
print("I am from %s department and my CGPA is %s" % (Department, CGPA))


#Question.3

a=56
b=10

#(a) part

print("a.",a&b)

#(b) part

print("b.",a|b)

#(c) part

print("c.",a^b)

# (d) part

print("d. Left shift both a and b with 2 bits respectively are:",a<<2 ,b<<2)

#(e) part

print("e. Right shift a with 2 bits and b with 4 bits respectively are:",a>>2,b>>4)


# Question 4

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
 
if (num1 > num2) and (num1 > num3):
   largest_number = num1
elif (num2 > num1) and (num2 > num3):
   largest_number = num2
else:
   largest_number = num3
 
print("The largest number is:",largest_number)


# Question 5

s=input("Enter a string:")

if 'name' in s:
    print ("Yes")
else:
    print ("No")


#Question.6

length_1=int(input("Enter side length: "))
length_2=int(input("Enter side length: "))
length_3=int(input("Enter side length: "))

if length_1 + length_2 > length_3 and length_1 + length_3 > length_2 and length_3 + length_2 > length_1 :
    print("Yes,triangle can be formed")
else:
    print("No,triangle can not be formed")