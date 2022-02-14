# Assignment 3
# Name: Peyush Jindal
# SID: 21103092


# Question 1

string_1=input("Enter Any String: ")
list=string_1.split() 
dict={} #initializing an empty dictionary
if len(list) ==1:   #if statement will be implemented when a single word is entered
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   #else statement eill be implemented when more than one word is entered in a string
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")


# Question 2

month=int(input("Enter the month: "))


if(month in [1,3,5,7,8,10,12]):
    day=int(input("Enter day:"))
    if(1<=day<=31):
        year=int(input("Enter the year:"))
        if(1800<=year<=2025):
            print("Date-",day,"/",month,"/",year)
            if(month==12 and day==31):
                print("Next Date-","1/1/",year+1)
            elif(day==31):
                print("Next Date-","1/",month+1,"/",year)
            else:
                print("Next Date-",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month in[4,6,9,11]):
    day=int(input("Enter day:"))
    if(1<=day<=30):
        year=int(input("Enter the year:"))
        if(1800<=year<=2025):
            print("Date-",day,"/",month,"/",year)
            if(day==30):
                print("Next Date-","1/",month+1,"/",year)
            else:
                print("Next Date-",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month==2):
    year=int(input("Give year-"))
    if(1800<=year<=2025):
        day=int(input("Give day-"))
        if(year%4==0):
            if(1<=day<=29):
                print("Date-",day,"/",month,"/",year)
                if(day==29):
                    print("Next Date-","1/",month+1,"/",year)
                else:
                    print("Next Date-",day+1,"/",month,"/",year)              
            else:
                print("invalid day")
        else:
            if(1<=day<=28):
                print("Date-",day,"/",month,"/",year)
                if(day==28):
                    print("Next Date-","1/",month+1,"/",year)
                else:
                    print("Next Date-",day+1,"/",month,"/",year)       
            else:
                print("invalid day")     
    else:
        print("invalid year")
else:
     print("invalid month")


# Question 3

input_list = input('Enter elements of the list: ')
user_list = input_list.split()

print('Input List: ', input_list)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
output_list =[(user_list[i], user_list[i]**2) for i in range(len(user_list))]

print(output_list)

print("\n")


# Question 4

Grade_points=int(input("Give a number between 4 and 10 including them-"))
if(Grade_points==4):
    print("Your Grade is 'D' and poor performance")
elif(Grade_points==5):
    print("Your Grade is 'C' and Below Average performance")
elif(Grade_points==6):
    print("Your Grade is 'C+' and Average performance")
elif(Grade_points==7):
     print("Your Grade is 'B' and Good performance")
elif(Grade_points==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(Grade_points==9):
    print("Your Grade is 'A' and Excellent performance")
elif(Grade_points==10):
    print("Your Grade is 'A+' and outstanding performance")
else:
    print("error")
print("\n")


# Question 5

Word="ABCDEFGHIJK"

counter=1

#we first identify the pattern which says that
#we need to first leave gaps equal to (counter-1) where counter tells
#the row no. and the alphabets should decrease after every row 

while(counter<7):
    print(" "*(counter-1),Word[0:11-((counter-1)*2)])
    counter=counter+1

print("\n")


# Question 6

sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

#part a. print the dictionary
print("a.",students)

#part b. sort acc to the names
print("b.",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#part c. sort acc to the SIDs
print("c.",{k:v for k,v in sorted(students.items())})

#part d. search for a student by their SID
sid = int(input("Search Name with SID: "))
print("d.",students[sid])


# Question 7

first_num=int(input("Enter first number:"))
second_num=int(input("Enter second number:"))
#now it will keep on printing the sequence till you say y and to stop it say n
series=[first_num,second_num]
n="y"
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("Give y to contnue and n to stop going further-")
print("Fibonacci series:",series)

#now lets find average of the resultant fibonacci series
sum=0
for i in series:
    sum=sum+i
print("Average of the sequence:",sum/len(series))


# Question 8

Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

#(a)
required_Set_1=Set1^Set2
print("a.",required_Set_1)

#(b)
required_Set_2=Set1^(Set2^Set3)
print("b.",required_Set_2)

#(c)
required_Set_3=(Set1&Set2)|(Set2&Set3)|(Set1&Set3)
print("c.",required_Set_3)

#(d)
new_Set={1,2,3,4,5,6,7,8,9,10}
required_Set_4=new_Set-Set1
print("d.",required_Set_4)

#(e)
required_Set_5=new_Set-(Set1|Set2|Set3)
print("e.",required_Set_5)
