# 1. Write a program to check whether a number is positive, negative, or zero.

# a=10
# print(a,type(a))
# if a>0:
#     print("a is positive")
# elif a==0:
#     print("a is zero")
# else:
#     print("a is negative")


# output
# a is positive



# 2. Check if a number is even or odd.

# a=6
# if a%2==0:
#     print("even")
# else:
#     print("odd")


# output
# even



# 3. Given a number, check if it is greater than 100.

# a=50
# if a>100:
#     print("greater than 100")
# else:
#     print("not greater than 100")


# output
# not greater than 100



# 4. Check whether a person is eligible to vote (age ≥ 18).

# age=18
# if age>=18:
#      print("eligible to vote")
# else:
#      print("not eligible to vote")


# output
# eligible to vote



# 5. Given two numbers, print the greater number.

# a=10
# b=15
# if a>b:
#     print(a)
# else:
#     print(b)


# output
# 15



# 6. Given three numbers, print the largest number.

# a=10
# b=20
# c=30
# if a>=b and a>=c:
#     print(a)
# elif b>=a and b>=c:
#    print(b)
# else:
#   print(c)


# output
# 30


# 7. Check whether a year is a leap year.

# year=2024

# if year%4==0:
#     print("leap year")
# else:
#     print("not a leap year")


# output
# leap year


# 8. Given a mark, print:"Pass" if marks ≥ 40 "Fail" otherwise

# a=35
# if a>=40:
#     print("pass")
# else:
#     print("fail")


# output
# fail



# 9. Given a mark, print grades:
# A → ≥ 90
# B → ≥ 75
# C → ≥ 60
# Fail → below 60


# mark=80
# if mark >=90:
#     print("A")
# elif mark >=75:
#     print("B")
# elif mark >=60:
#     print("C")
# else:
#     print("fail")


# output
# B



# 10. Check if a character is a vowel or consonant.

# character ="a"
# if character in "aeiou":
#     print("vowel")
# else:
#     print("consonant")


# output
# vowel



# 11. Print numbers from 1 to 10 but stop when number is 6.

# for i in range(1,11):
#     if i==6:
#         break
#     print(i)


# output
# 1
# 2
# 3
# 4
# 5



# 12. Print numbers from 1 to 10 but skip number 5.

# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)


# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10


# 13. Use pass inside an if block and explain why it doesn’t cause an error.

# x=10
# if x>5:
#     pass
# print("program continues")


# output
# program continues
# if block cannot be empty. pass is used as a placeholder so python doesn't give an error



# 14. Print all even numbers between 1 and 20 .

# for i in range(1,21):
#     if i %2==0:
#         print(i)


# output
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20



# 15. Find the sum of numbers from 1 to 10.

# total=0

# for i in range(1,11):
#     total=total+i
# print(total)


# output
# 55



# 16. Check whether a given number is a multiple of both 3 and 5.

# a=15
# if a%3==0 and a%5==0:
#     print("multiple of both")
# else:
#     print("not a multiple")


# output
# multiple of both



# 17. Print "Hello" 5 times using a loop.

# for i in range(5):
#     print("hello")


# output
# hello
# hello
# hello
# hello
# hello



# 18. Given a list [1,2,3,4,5] , print only numbers greater than 3.

# a=[1,2,3,4,5]
# for num in a:
#     if num>3:
#         print(num)


# output
# 4
# 5



# 19. Advanced Login System
# Write a Python program to simulate a login system with the following rules:
# .The correct username is "admin" and the correct password is "1234" .
# .The user is allowed a maximum of 3 login attempts.
# .The username comparison should be case-insensitive.
# .The password comparison should be case-sensitive.
# .If the user enters correct credentials within the allowed attempts, display
#  Login successful .
# .If all attempts are used without success, display
#  Account locked .
# .After each failed attempt, display the number of attempts remaining.




# correct_username="admin"
# correct_password="1234"
# for a in range(3):
#    username = input("enter username: ")
#    password=input("enter password: ")
#    if username.lower()==correct_username and password==correct_password:
#        print("login successful")
#        break
#    else:
#        print("wrong username or paasword")
# else:
#     print("Account locked")




# 20. Enhanced Traffic Light Controller
# Write a Python program that acts as a traffic light controller with the following
# conditions:
# The program should accept either a color or a number as input.
# Use the mapping:
# 1 or "red" → Stop and wait for 60 seconds
# 2 or "yellow" → Ready and wait for 5 seconds
# 3 or "green" → Go and drive safely
# The program should handle inputs in a case-insensitive manner.
# If the input does not match any valid color or number, display
# Invalid signal .



# signal=input("Enter colour or number: ")
# signal=signal.lower()

# if signal=="1" or signal== "red":
#     print("Stop and wait for 60 seconds")

# elif signal=="2" or signal== "yellow":
#     print("Ready and wait for 5 seconds")

# elif signal=="3" or signal== "green":
#     print("Go and drive safely")

# else:
#     print("Invalid signal")




# LIST COMPREHENSION QUESTIONS

# 1. Given a list of numbers, write a program to find the sum of all numbers, the
# sum of even numbers, and the sum of odd numbers using list
# comprehension.


# numbers=[1,2,3,4,5]
# total=sum(numbers)
# even=sum([x for x in numbers if x %2==0])
# odd=sum([x for x in numbers if x %2 !=0 ])

# print(total)
# print(even)
# print(odd)


# output
# 15
# 6
# 9


# 2. Given a list of numbers, create a new list that contains only numbers
# greater than 10 and divisible by 3 using list comprehension.


# numbers=[10,15,20,25,30,35,40,45,50]
# a=[x for x in numbers if x>10 and x%3==0]
# print(a)

# output
# [15, 30, 45]


# 3. Given a list of numbers, create a new list containing only even numbers
# greater than 10 using list comprehension.


# numbers=[10,15,20,25,30,35,40,45,50]
# a=[x for x in numbers if x>10 and x%2==0]
# print(a)

# output
# [20, 30, 40, 50]



# 4. Given a list of strings, create a new list containing the length of each string
# using list comprehension.


# a=["apple","banana","cherry"]
# b=[len(x)for x in a]
# print(b)

# output
# [5, 6, 6]



# 5. Given a list of numbers, create a new list where:
# even numbers are replaced with "even"
# odd numbers are replaced with "odd"


# a=[1,2,3,4,5,6]
# b=["even" if x%2==0 else"odd"for x in a ]
# print(b)


# output
# ['odd', 'even', 'odd', 'even', 'odd', 'even']



