# 1. Create a set with values {1, 2, 3, 4} .

# a={1,2,3,4}
# print(a)

# output
# {1, 2, 3, 4}


# 2. Add the value 5 to the set {1, 2, 3, 4} using a set method.

# a={1,2,3,4}
# a.add(5)
# print(a)

# output
# {1, 2, 3, 4, 5}


# 3. Remove the value 3 from the set {1, 2, 3, 4} using a set method.

# a={1,2,3,4}
# a.remove(3)
# print(a)

# output
# {1, 2, 4}


# 4. Check if 2 exists in the set {1, 2, 3, 4} .

# a={1,2,3,4}
# print(2 in a)

# output
# True


# 5. Convert the list [1, 2, 2, 3, 4, 4] into a set to remove duplicates.

# a=[1,2,2,3,4,4]
# b=set(a)
# print(b)

# output
# {1, 2, 3, 4}



# 6. Convert the tuple (10, 20, 30) into a set.

# a=(10,20,30)
# b=set(a)
# print(b)

# output
# {10, 20, 30}


# 7. Find the union of sets {1, 2, 3} and {3, 4, 5} .

# set1={1,2,3}
# set2={3,4,5}
# result=set1.union(set2)
# print(result)

# output
# {1, 2, 3, 4, 5}


# 8. Find the intersection of sets {1, 2, 3} and {3, 4, 5} .

# set1={1, 2, 3} 
# set2={3, 4, 5}
# result=set1&set2
# print(result)

# output
# {3}


# 9. Find the difference between sets {1, 2, 3, 4} and {3, 4} .

# set1={1,2,3,4}
# set2={3,4}
# result=set1-set2
# print(result)

# output
# {1, 2}


# 10. Create a copy of the set {5, 6, 7} using a set method.

# a={5,6,7}
# print(a.copy())

# output
# {5, 6, 7}


# 11. Remove all elements from the set {1, 2, 3} using one set method.

# a={1,2,3}
# print(a.remove())

# output



# 12. Check whether {1, 2} is a subset of {1, 2, 3} .

# a={1,2}
# b={1,2,3}
# print(a.issubset(b))

# output
# True


# 13. Check whether {1, 2, 3} is a superset of {1, 2} .

# a={1,2,3}
# b={1,2}
# print(a.issuperset(b))

# output
# True


# 14. Find the symmetric difference between {1, 2, 3} and {3, 4, 5} .

# a={1,2,3}
# b={3,4,5}
# result=a^b
# print(result)

# output
# {1, 2, 4, 5}


# 15. Add multiple elements {8, 9, 10} into {1, 2, 3} using a set method.

# a={8,9,10}
# a.update([1,2,3])
# print(a)

# output
# {1, 2, 3, 8, 9, 10}


# 16. Remove a random element from the set {1, 2, 3} using a set method.

# a={1,2,3}
# removed_item=a.pop()
# print(removed_item)

# output
# 1


# 17. Check if two sets {1, 2, 3} and {3, 2, 1} are equal.

# a={1,2,3}
# b={3,2,1}
# print(a==b)

# output
# True


# 18. From the list [1, 2, 2, 3, 4, 4, 5] , extract only unique values using a set.

# a= frozenset([1,2,2,3,4,4,5])
# print(a)

# output
# frozenset({1, 2, 3, 4, 5})


# 19. Convert the set {1, 2, 3} into a list.

# a={1,2,3}
# b=list[a]
# print(b)

# output
# list[{1, 2, 3}]


# 20. From {1, 2, 3, 4, 5} , remove {2, 4} using a set method.

# a={1,2,3,4,5}
# b={2,4}
# result=(a.difference_update(b))
# print(a)

# output
# {1, 3, 5}