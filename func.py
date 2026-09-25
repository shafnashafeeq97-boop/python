# 1. Write a function that takes a number as input and returns whether the
# number is even or odd.


# def check_number(a):

#    if a%2==0:
#         print("even")
#    else:
#         print("odd")

# check_number(6)


# output
# even



# 2. Write a function that takes three numbers as input and returns the largest
# number among them.

# def largest(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c

# print(largest(5,10,15))


# output
# 15



# 3. Write a function that takes a list of numbers as input and returns the sum of
# all elements in the list.


# def total(numbers):
#     return sum(numbers)
# print(total([5,10,15]))


# output
# 30



# 4. Write a function that takes a list of numbers as input and returns a new list
# containing only even numbers.


# def even_numbers(a):
#     return[num for num in a if num%2==0]

# print(even_numbers([1,2,3,4,5,6,7,8,9,10]))


# output
# [2, 4, 6, 8, 10]



# 5. Write a function that takes a string as input and returns the length of the
# string.


# def string_length(text):
#     return len(text)
# print(string_length("python"))

# output
# 6



# 6. Write a function that takes a string as input and returns the string in
# uppercase.


# def uppercase(text):
#     return text.upper()
# print(uppercase("python"))

# output
# PYTHON



# 7. Write a function that takes a number as input and returns whether the
# number is positive, negative, or zero.


# def check_number(a):
    
#    if a>0:
#       print("a is positive")
#    elif a==0:
#       print("a is zero")
#    else:
#       print("a is negative")

# check_number(10)


# output
# a is positive



# 8. Write a function that takes a number as input and returns True if the number
# is a multiple of both 3 and 5, otherwise returns False .


# def multipleof_3and5(a):
#     if a%3==0 and a%5==0:
#         return True
#     else:
#         return False

# print(multipleof_3and5(10))


# output
# False



# 9. Write a function that takes a list of numbers as input and returns the
# maximum value in the list.


# def maximum(numbers):
#     return max(numbers)
# print(maximum([10,30,40,20]))


# output
# 40



# 10. Write a function that takes marks as input and returns the grade according
# to the following rules:
# A for marks ≥ 90
# B for marks ≥ 75
# C for marks ≥ 60
# Fail for marks below 60


# def grade(marks):
#     if marks>=90:
#         return"A"
#     elif marks>=75:
#         return"B"
#     else:
#         return"C"

# print(grade(80))


# output
# B
   


# 11. Write a function that takes a price as input and returns the discounted
# price after applying a 10% discount.


# def discount(price):
#     return price-(price*10/100)

# print(discount(800))


# output
# 720.0



# 12. Write a function that takes a list of numbers as input and returns the count
# of even and odd numbers.


# def count_even_odd(a):
#     even=len ([num for num in a if num%2 ==0 ])
#     odd=len ([num for num in a if num%2 !=0 ])
#     return even, odd
        
# print(count_even_odd([1,2,3,4,5,6,7,8]))


# output
# (4, 4)



# 13. Write a function that takes a temperature in Celsius as input and returns
# the temperature in Fahrenheit.


# def celsius_to_fahrenheit(a):
#     return(a *9/5)+32

# print(celsius_to_fahrenheit(25))


# output
# 77.0


