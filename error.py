# a=10
# b=0
# print(a/b)

# ZeroDivisionError: division by zero



# name="john"
# age=26
# print(name+age)

# TypeError: can only concatenate str (not "int") to str



# number=int("world")
# print(number)

# ValueError: invalid literal for int() with base 10: 'world'



# a=["apple","banana","cherry"]
# print(a[4])

# IndexError: list index out of range



# a={"name":"john", "age":"26"}
# print(a["salary"])

# KeyError: 'salary'



# file=open("string.txt")

# FileNotFoundError: [Errno 2] No such file or directory: 'string.txt'



# try:
#     a=10
#     b=0
#     print(a/b)
# except Exception as e:
#     print(e)


# division by zero


# try:
#     a=10
#     b=0
#     c=a/b
# except Exception as e:
#     print(e)
# else:
#     print(c)
# finally:
#     print("This will always be printed")


# division by zero
# This will always be printed


# a=10
# if a>0:
#    raise ValueError("positive numbers are not allowed!")


# ValueError: positive numbers are not allowed!


# try:
#     file=open("noneexistent_file.txt","r")
# except FileNotFoundError:
#     print("The file does not exist.")



# class Car:
#     # Attributes
#     def __init__(self,make,model,year,price):
#         self.m=make
#         self.mo=model
#         self.y=year
#         self.p=price

#     # Methods
#     def display_info(self):
#         print(f"Car: {self.y} {self.m} {self.mo} {self.p}")


# # Creating an object (instance) of the car class
# Car1=Car("honda", "civic", "2022", "5000000")
# Car2=Car("ford", "mustang", "2001", "7000000") 

# Car1.display_info()
# Car2.display_info()
# print(Car1.p)




# class student:
#     def __init__(self,name,marks):
#         self.n=name
#         self.m=marks
        
 
#     def calculate_average(self):
#         total=sum(self.m.values())
#         average=total/len(self.m)
#         return average

    
#     def display_grade(self):
#         average=self.calculate_average
#         if average>=90:
#           grade="A"
#         elif average>75:
#           grade="B"
#         elif average>=50:
#            grade="C"
#         else:
#            grade="Fail"  
#            print(f"{self.n}average:{average:.f}{self.m}")