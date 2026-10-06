# 1. creat a tuple (1,2,3,4) and access the element 3 using indexing 

# my_tuple=(1,2,3,4)

# print(my_tuple.index(4))

# output

# 3

# 2. convert the tuple (10,20,30) into a list

# a=("10","20","30")

# b=list(a)

# print(b)

# output

# ['10', '20', '30']

# 3. convert the list [1,2,3] into a tuple

# a=["1","2","3"]

# b=tuple(a)

# print(a)

# 4. from the tuple ("a","b","c","d"),extract ("b","c") using slicing

# a=("a","b","c","d")

# print(a[1:3])

# output

# ('b', 'c')

# 5.check if "x" exists inside the tuple ("x","y","z")

# a=("x","y","z")

# b="x"

# print("x" in (a))

# output

# True

# 6. given(5,3,9,1), find the maximum value using a tuple function

# a=(5,3,9,1)

# print(max(a))

# output

# 9

# 7. given (1,2,3), creat a new tuple (1,2,3,1,2,3)using tuple operations only

# a1=(1,2,3)

# a2=(1,2,3)

# joined_a=a1+a2

# print(joined_a)

# output

# (1, 2, 3, 1, 2, 3)

# 8.count how many times 2 apperas in (1,2,2,3,2)using tuple operatins

# a=(1,2,2,3,2)

# print(a.count(2))

# output

# 3

# 9. find the index of cat in ("dog","cat","mouse")

# a= ("dog","cat","mouse")

# print(a.index("cat"))

# output

# 1


# 10. Reverse (1,2,3,4,5) using slicing

# a=(1,2,3,4,5)

# print(a[::-1])

# output

# (5, 4, 3, 2, 1)

# 11. combine(1,2) and(3,4) into(1,2,3,4) using tuple operations

# a1=(1,2)

# a2=(3,4)

# joined_a=a1+a2

# print(joined_a)

# output

# (1, 2, 3, 4)

# 12.convert "hello" into a tuple of characters

# a=("hello")

# b=tuple(a)

# print(b)

# output

# ('h', 'e', 'l', 'l', 'o')

# 13.convert(1,2,3,4)into the list [1,4] by extracting only first $ last elements

# a=(1,2,3,4)

# result=[a[0],a[3]]

# print(result)

# output

# [1, 4]

# 14. given a tuple (10,20,30,40), replace the value 30 with 99

# a=(10,20,30,40)

# temp_list=list(a)

# temp_list[2]=99

# a=tuple(temp_list)

# print(a)

# output

# (10, 20, 99, 40)

# 15. using unpacking, extract a=1, b=2, c=3 from (1,2,3)

# my_tuple=(1,2,3)

# (a,b,c)=my_tuple

# print(a)

# print(b)

# print(c)

# output

# 1

# 2

# 3

# 16.creat a nested tuple:turn (1,2,3) into ((1,2,3),)

# a=(1,2,3)

# nested=a,

# print(nested)

# output

# ((1, 2, 3),)

# 17. Merge ("a","b") with ("c","d") to get a single tuple ("a","b","c","d")

# a=("a","b")

# b=("c","d")

# joined_tuple=a+b

# print(joined_tuple)

# output

# ('a', 'b', 'c', 'd')

# 18. check if tuple (1,2,3)is equal to its reverse

# a=(1,2,3)

# b=(3,2,1)

# print(a==b)

# output

# False

# 19.convert a tuple of lists ([1,2],[3,4]) into a single flat [1,2,3,4]

# a=([1,2])

# b=([3,4])

# joined_list=a+b

# print(joined_list)

# output

# [1, 2, 3, 4]

# 20. given(1,[2,3],4), add 5 inside the inner list so result becomes (1,[2,3,5],4)

# list1=(1,[2,3],4)

# list1[1].append(5)

# # list1.extend(list2)

# print(list1)

# output

# (1, [2, 3, 5], 4)