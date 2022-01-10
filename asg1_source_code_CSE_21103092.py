# assignment 1
# Name-Peyush Jindal
# SID=21103092

# Question 1

number_1=input("Enter first number:")
number_2=input("Enter first number:")
number_3=input("Enter first number:")

number_1=int(number_1)
number_2=int(number_2)
number_3=int(number_3)

# average
average=(number_1 + number_2 + number_3)/3
print(average)


# Question 2

# all values are in US dollars $

Gross_Income=input("Please enter gross income:")
Gross_Income=float(Gross_Income)

Standard_Deduction=10000

Dependents=input("Enter the number of dependents:")
Dependents=int(Dependents)

#  For each dependent, a taxpayer is allowed an additional $3,000 deduction.
Dependent_Deduction=3000

Taxable_Income=Gross_Income-Standard_Deduction-(Dependent_Deduction*Dependents)
# tax rate=20%
Tax=(Taxable_Income*20)/100
print("Tax:",Tax)


# Question 3

name= input("Please enter name:")
sid= input("Enter Student ID:")
sid=int(sid)
#  Enter Gender values:
#   ‘F’ for female
#   ‘M’ for male
#   ‘U’ for unknown
gender= input("Enter gender:")
course_name= input("Enter your course name:")
cgpa= input("Enter CGPA:")
cgpa=float(cgpa)
Student=[sid,name,gender,course_name,cgpa]
print(Student)


# Question 4

student_1_marks= int(input("Enter student 1 marks:"))
student_2_marks= int(input("Enter student 2 marks:"))
student_3_marks= int(input("Enter student 3 marks:"))
student_4_marks= int(input("Enter student 4 marks:"))
student_5_marks= int(input("Enter student 5 marks:"))

my_list=[student_1_marks,student_2_marks,student_3_marks,student_4_marks,student_5_marks]
my_list.sort()
print(my_list)


# Question 5

# part a
color=['Red','Green','White','Black','Pink','Yellow']
color.remove(color[3])
print("Part a Answer:",color)

# part b
color=['Red','Green','White','Black','Pink','Yellow']
color[3:5]=['Purple']
print("Part b Answer:",color)