# FILE HANDLING QUESTIONS


# 1. Write a program to create a file named data.txt and write the text
# "Hello File Handling" into it.


# file=open("basic/data.txt","w")
# file.write("Hello File Handling")
# file.close()



# 2. Write a program to read the contents of a file data.txt and display it on the
# screen.


# file=open("basic/data.txt","r")
# data=file.read()
# print(data)
# file.close()

# output
# Hello File Handling



# 3. Write a program to append the text "Python is awesome" to an existing file.


# file=open("basic/data.txt","a")
# file.write("\npython is awesome")
# file.close()

# output
# python is awesome



# 4. Write a program to count the number of lines present in a file.


# file=open("basic/data.txt","r")
# lines=file.readlines()
# print("Number of lines:",len(lines))
# file.close()

# output
# Number of lines: 2



# 5. Write a program to count the number of words in a file.


# file=open("basic/data.txt","r")
# data=file.read()
# words=data.split()
# print("Number of words:",len(words))
# file.close()

# output
# Number of words: 6



# 6. Write a program to copy the contents of one file into another file.


# file1=open("basic/data.txt","r")
# file2=open("basic/copy.txt","w")

# data=file1.read()
# file2.write(data)

# file1.close()
# file2.close()



# 7. Write a program to read a file and print only the lines that contain the word "Python" .


# file=open("basic/data.txt","r")
# for line in file:
#     if "python" in line.lower():
#         print(line)
# file.close()        

# output
# python is awesome



# 8. Write a program that reads numbers from a file and calculates their sum.

# file=open("basic/numbers.txt","r")
# total=0
# for i in file:
#     total=total+int(i)
#     print(total)
# file.close()    

# output
# 150



# ERROR HANDLING (EXCEPTION HANDLING) QUESTIONS


# 9. Write a program to handle a ValueError when the user enters invalid input (for
# example, entering letters instead of a number)

# try:
#     a=int(input("Enter a nuber:"))
#     print(a)
# except ValueError as e:
#     print(e)
# else:
#     print("Valid input")
# finally:
#     print("This wil alwayes be printed")


# output
# invalid literal for int() with base 10: 'q10'
# This wil alwayes be printed



# 10. Write a program to handle invalid input (user enters a string instead of a
# number).

# try:
#     a=int(input("Enter a number:"))
#     print("you entered:",a)
# except ValueError:
#     print("Invalid input")


# output
# Enter a number:Hi
# Invalid input



# 11. Write a program that handles file not found error while opening a file.

# try:
#     file=open("basic/data.txt","r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print("File not found")



# 12. Write a program using try , except , and else blocks.

# try:
#     a=int(input("Enter a number:"))
#     print(a)
# except ValueError as e:
#     print(e)
# else:
#     print("valid input")


# output
# 20
# valid input



# 13. Write a program using try , except , and finally to ensure a message
# "Program ended" is always printed.

# try:
#     a=int(input("Eter a number:"))
#     print(a)
# except ValueError as e:
#     print(e)
# finally:
#     print("program ended")


# output
# 50
# program ended



# 14. Write a program that catches multiple exceptions using multiple except
# blocks.

# try:
#     a=int(input("Enter first number:"))
#     b=int(input("Enter second number:"))
#     c=a/b
#     print(c)

# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)    
    


# 15. Write a program that raises a custom error when the user enters a negative
# number.

# a=int(input("Enter a number:"))
# if a<0:
#     raise ValueError("Negative number is not allowed")

# print("number:",a)



# MODULES & LIBRARIES (BUILT-IN + USERDEFINED)
# 🔹 Built-in ( math only)


# 16. Write a program that uses the math module to find the square root of a
# number.

# import math
# print(math.sqrt(20))

# output
# 4.47213595499958



# 17. Write a program that uses the math module to calculate power of a number.

# import math
# print(math.pow(2,3))

# outputt
# 8.0



# 18. Write a program that uses the math module to find the factorial of a number.

# import math
# print(math.factorial(5))

# output
# 120



# 🔹 User-Defined Modules


# 19. Create a user-defined module named calculator.py that contains functions
# for addition, subtraction, multiplication, and division.
# Import and use this module in another Python file.

# def add(a,b):
#     return a+b
# def substract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return(a/b)


# output
# 12
# 8
# 20
# 5.0



# 20. Create a user-defined module that contains a function to check whether a
# number is even or odd, and use it in another program.

# def even_odd(a):
#     if a%2==0:
#        return "Even"
#     else:
#        return "odd"


# output
# Even



# 21. Create a user-defined module with a function that returns the area of a
# circle, and import it in another file.


# import math

# def area(r):
#     return math.p*r*r


# output
# 314.1592653589793


