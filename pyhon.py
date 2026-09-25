# string

# my_string="Hello world"
# print(my_string)

# string slicing
# 1.

# a="Hello, world!"
# print(a[0:5])

# 2.
# a="Hello, world!"
# print(a[-6:-1])

# 3.
# a="Hello, world!"
# print(a[0:12:2])

# 4.
# a="Hello, world"
# print(a[::-1])


# modifying string
# 1. 
# s="Hello, world!"
# new_s=s.replace("world","python")
# print(new_s)

# 2.
# a="Hello world!"
# print(a.upper())
# print(a.lower())


# string concatenation
# 1.
# a1="Hello"
# a2="world"
# result=a1+","+a2+"!"
# print(result)

# 2.
# words=("python", "is", "awesome")
# sentence=" ".join(words)
# print(sentence)


# Format strings
# 1.
# name="Alice"
# age="25"
# formatted_string=f'My name is {name}, and I am {age} years old'
# print(formatted_string)


# Escape characters
# a="Hello world"
# print("Hello\nworld")

# print("Hello\tworld")

# print("Hello\'world")

# print("Hello\" world")

# print("Hello\\world")


# string methods
1
# s="Hello, world!"
# print(len(s))

# print(s.strip())

# print(s.split())

# print(s.find("world"))

# print(s.count("Hello"))

# print(s.startswith("Hello"))

# print(s.endswith("world!"))




# list

# a=[1,2,3,'python',4.5]
# print(a)

# a=['apple','banana','cherry']
# print(a[1])
# print(a[-1])

# a=[10,20,30,40,50]
# print(a[1:4])

# a=['apple','banana','cherry']
# a[1]='orange'
# print(a)

# a=[1,2,3,4,5]
# a[1:3]=['a','b']
# print(a)

# a=['apple','banana']
# a.append('cherry')
# print(a)

# a=['apple','banana']
# a.insert(1,'cherry')
# print(a)

# a=['apple','banana']
# b=['cherry','orange']
# a.extend(b)
# print(a)

# a=['apple','banana','cherry']
# a.remove('banana')
# print(a)

# a=['apple','banana','cherry']
# popped_item=a.pop(1)
# print(popped_item)
# print(a)

# a=['apple','banana','cherry']
# del a[1]
# print(a)

# a=['apple','banana','cherry']
# a.clear()
# print(a)

# a=[1,2,3,2,4]
# print(a.count(2))

# a=['apple','banana','cherry']
# print(a.index('banana'))

# a=[1,2,3]
# a.reverse()
# print(a)

# a=[3,1,2]
# a.sort()
# print(a)

# a=['apple','banana','cherry']
# b=a.copy()
# print(b)

# a=[3,5,1,4,2]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# a=[3,1,2]
# sorted_list=sorted(a)
# print(sorted_list)

# a=['apple','banana','cherry']
# b=a.copy()
# print(b)

# b=a[:]


# a=['apple','banana']
# b=['orange','cherry']
# c=a+b
# print(c)


# a=['apple','banana']
# b=['orange','cherry']
# a.extend(b)
# print(a)



# string
# 1.
# my_string="hello"
# print(my_string)

# 2.
# a="Python"
# print(a.lower())

# 3.
# A="Hello world"
# print(A.replace("world","python"))

# 4.
# a="hello"
# print(a[1:4])

# 5.
# a="Hello"
# print(a[::-1])

# 6.
# a="hello"
# b="world"
# c=a+" "+b
# print(c)

# 7
# a="hi"
# print(a*3)

# 8
# a="concatenate"
# b="cat"
# print(b in a)

# 9
# a="banana"
# print(a.count("a"))

# 10
# a=" hello world "
# print(a.strip())

# 11
# a="hello"
# print(a.find("o"))

# 12
# a="a,b,c,d"
# print(a.split(","))

# 13
# a=["a","b","c"]
# result="".join(a)
# print(result)

# 14
# a="abcdef"
# print(a[0:6:2])


# 15
# a="banana"
# print(a.replace("a","@"))

# 16
# a="hello123"
# print(a.isalnum())

# 17
# a="python"
# print(a.capitalize())

# 18
# a="hello world"
# print(a.title())

# 19
# a="python"
# print(a.replace("o",""))

# 20
# a="madam"
# print(a==a[::-1])


# list
# 1
# a=[1,2,3]
# a.append(4)
# print(a)

# 2
# a=[10,20,30]
# a.remove(20)
# print(a)

# 3
# a=[5,3,9,1]
# a.sort()
# print(a)

# 4
# a=[1,2,3,4,5]
# print(a[1:4])

# 5
# a=[1,2,3,4]
# print(a[::-1])

# 6
# a=[1,2]
# b=[3,4]
# a.extend(b)
# print(a)

# 7
# a=[7,8]
# print(a*2)

# 8
# a=[1,2,3,4]
# print(3 in a)

# 9
# a=[1,2,2,3,2]
# print(a.count(2))

# 10
# a=["a","b","c","d"]
# del a[3]
# print(a)

# 11
# a=["a","b","c"]
# a.insert(1,"x")
# print(a)

# 12
# a=[10,20,30,40]
# a[2]=99
# print(a)

# 13
# a=range(5)
# b=list(a)
# print(b)

# 14
# a=[1,2,3,4,5,6]
# print(a[1:6:2])

# 15
# a=[1,2,3]
# a.clear()
# print(a)

# 16
# a=[4,5,6]
# a.copy()
# print(a)

# 17
# a=[1,2,3]
# a=[(a)]
# print(a)

# 18
# a=[1,2]
# b=[3,4,5]
# a.extend(b)
# print(a)

# 19
# a=["hello"]*3
# print(a)

# 20
# a=[10,20,30,40]
# popped_item=a.pop(2)
# print(popped_item)

# del a[2]
# print(a)



tuple
# 1
# a=[1,2,3,4]
# print(a.index(4))

# 2
# a=(10,20,30)
# b=list(a)
# print(b)

# 3
# a=[1,2,3]
# b=tuple(a)
# print(b)

# 4
# a=("a","b","c","d")
# print(a[1:3])

# 5
# a=("x","y","z")
# print("x" in a)

# 6
# a=(5,3,9,1)
# print(max(a))

# 7
# a=(1,2,3)
# print(a*2)

# 8
# a=(1,2,2,3,2)
# print(a.count(2))

# 9
# a=("dog","cat","mouse")
# print("cat"in a)

# 10
# a=(1,2,3,4,5)
# print(a[::-1])

# 11
# a="hello"
# b=tuple(a)
# print(b)

# 12
# a=(1,2)
# b=(3,4)
# c=a+b
# print(c)

# 13
# a=(1,2,3,4)
# result=[a[0],a[3]]
# print(result)

# 14
# a=(10,20,30,40)
# b=list(a)
# b[2]=99
# a=tuple(b)
# print(a)

# 15
# a=(1,2,3)
# (first,middle,last)=a
# print(first)
# print(middle)
# print(last)

# 16
# a=("a","b")
# b=("c","d")
# c=a+b
# print(c)

# 17
# a=(1,2,3)
# nested=a,
# print(nested)

# 18
# a=(1,2,3)
# b=(3,2,1)
# print(a==b)

# 19
# a=([1,2])
# b=([3,4])
# c=a+b
# print(c)

# 20
# a=(1,[2,3],4)
# a.extend(5)
# print(a)




