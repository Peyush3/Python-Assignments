# Question 1

print("<Question 1>")
# Recursive Python function to solve tower of hanoi
# n is number of disks
# A, C, B are the name of rods
def TowerOfHanoi(n , from_rod, aux_rod, middle_rod):
	if n == 0:
		return
	TowerOfHanoi(n-1, from_rod, middle_rod, aux_rod)
	print("Move disk",n,"from rod",from_rod,"to rod",aux_rod)
	TowerOfHanoi(n-1, middle_rod, aux_rod, from_rod)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
print("\n")


# Question 2

print("<Question 2>")

# Defining factorial function
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
        
# Defining ncr function
def ncr(n,r):
    x=factorial(n)/(factorial(n-r)*factorial(r))
    return int(x)

n=int(input('Enter the size of pascals triangle:'))
   
print("Using iteration:")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") 

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	
print("\n\n")

print("Using Recurssion:")

def pascals_triangle(n,original_length=n):
    if n == 0:
        return
    pascals_triangle(n-1,original_length)
    #printing the spaces
    print('  '*(original_length-n), end='')

    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        start = start * (n - i) // i
    print()
pascals_triangle(n)
print("\n")



# Question 3
print("<Question 3>")

print()
print("<3A>")
def fun(a,b):
    quotient=a//b
    remainder=a%b
    print("Quotient:",quotient)
    print("Remainder:",remainder)
    result=[quotient,remainder]
    return result

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
result=fun(a,b)
print(result)
print("Callable:",callable(fun))

print()
print("<3B>")
print("a is zero:",a==0)
print("b is zero:",b==0)
print("quotient is zero:",result[0]==0)
print("remainder is zero:",result[1]==0)

print()
print("<3C>")
d=[4,5,6]
result=result+d
print(result)
a_list=[]
for i in result:
    if i>4:
        a_list.append(i)
print("The values greater than 4:",a_list)

print()
print("<3D>")
a_set=set(a_list)
print(a_set)

print()
print("<3E>")
immutable_set=frozenset(a_set)
print("The required immutable set:",immutable_set)

print()
print("<3F>")
print("The required max value is:",max(immutable_set))
print("The required hash value is:",hash(max(immutable_set)))
print("\n")


#QUESTION 4
print("ANSWER 4 ")
class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object destroyed")

student1 = Student("Peyush Jindal", 21103092)
print(f"The name of the student it {student1.name} and SID is {student1.roll_no}.")
#deleting object
del student1
print("\n")


#QUESTION 5

print("ANSWER 5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 

employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

print()

# part a
print("<Part A>")
employee1.salary = 70000
print(f"The updated salary of {employee1.name} is {employee1.salary}")

# part b
print()
print("<Part B>")
del employee3
print("Record of Viren deleted", end='')
print("\n")


# Question 6

print("<Question 6>")
def anagram(word):
    if len(word)==1:
        return [word];
    partial_words=anagram(word[1:])
    char=word[0]
    result=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result        


George_word=input("Please give a word-")
Possible_words=anagram(George_word)
Barbie_word=input("Give a word-")
print("Possible Words-",Possible_words)
print("If Barbie's word lies in the list,then their friendship is real.")

if Barbie_word in Possible_words:
    print("Friendship is real.")
else:
    print("Friendship is fake.")