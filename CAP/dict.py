# 1. Create a dictionary with keys "name" and "age" and values "Nik" and 20 .

# a={"name":"Nik", "age":"20"}
# print(a)

# output
# {'name': 'Nik', 'age': '20'}


# 2. Access the value of key "name" from {"name": "Nik", "age": 20} .

# a={"name": "Nik", "age": 20}
# print(a["name"])

# output
# Nik


# 3. Add a new key "city" with value "Delhi" to {"name": "Nik", "age": 20} .

# a={"name": "Nik", "age": 20} 
# a["city"]="Delhi"
# print(a)

# output
# {'name': 'Nik', 'age': 20, 'city': 'Delhi'}


# 4. Update the value of "age" to 25 in {"name": "Nik", "age": 20} .

# a={"name": "Nik", "age": 20}
# a.update({"age":"25"})
# print(a)

# output
# {'name': 'Nik', 'age': '25'}


# 5. Delete the key "age" from {"name": "Nik", "age": 20} .

# a={"name": "Nik", "age": 20}
# del a["age"]
# print(a)

# output
# {'name': 'Nik'}


# 6. Check if the key "email" exists in {"name": "Nik", "age": 20} .

# a={"name": "Nik", "age": 20}
# b="email"
# print(b in a)

# output
# False


# 7. Get all keys from {"name": "Nik", "age": 20} using a dictionary method.

# a={"name": "Nik", "age": 20} 
# print(a.keys())

# output
# dict_keys(['name', 'age'])


# 8. Get all values from {"name": "Nik", "age": 20} using a dictionary method.

# a={"name": "Nik", "age": 20}
# print(a.values())

# output
# dict_values(['Nik', 20])


# 9. Convert the dictionary {"a": 1, "b": 2} into a list of (key, value) pairs.

# a= {"a": 1, "b": 2}
# b=list[a]
# print(b)

# output
# list[{'a': 1, 'b': 2}]


# 10. Create a dictionary from two lists: (use zip method) keys = ["name", "age"] values = ["Nik", 20] .

# keys=["name","age"]
# values=["Nik","20"]
# a=dict(zip(keys,values))
# print(a)

# output
# {'name': 'Nik', 'age': '20'}


# 11. Count how many keys are in {"a": 1, "b": 2, "c": 3} .

# a= {"a": 1, "b": 2, "c": 3}
# print(len(a))

# output
# 3


# 12. Merge two dictionaries {"a": 1} and {"b": 2} into one.

# a={"a": 1}
# a.update({"b": 2})
# print(a)

# output
# {'a': 1, 'b': 2}


# 13. Clear all elements from {"a": 1, "b": 2} using a dictionary method.

# a={"a": 1, "b": 2}
# a.clear()
# print(a)

# output
# {}


# 14. Copy the dictionary {"x": 10, "y": 20} using a dictionary method.

# a={"x": 10, "y": 20}
# a.copy()
# print(a) 

# output
# {'x': 10, 'y': 20}


# 15. Get the value of key "salary" safely from {"name": "Nik", "age": 20} without getting an error.

# a={"name": "Nik", "age": 20}
# print(a.get("salary"))

# output
# None


# 16. From {"a": 1, "b": 2, "c": 3} , remove the last inserted item using a dictionary method.

# a={"a": 1, "b": 2, "c": 3}
# b=a.popitem()
# print(b)

# output
# ('c', 3)


# 17. Given student = {"name": "Rahul", "marks": {"math": 90, "science": 85}} , access only the "science" marks.

# student = {"name": "Rahul", "marks": {"math": 90, "science": 85}}
# print(student["marks"]["science"])

# output
# 85


# 18. From the above student dictionary, update "math" marks to 95 .

# a={"name": "Rahul", "marks": {"math": 90, "science": 85}}
# a["marks"]["math"]=95
# print(a)

# output
# {'name': 'Rahul', 'marks': {'math': 95, 'science': 85}}


# 19. Add a new subject "english": 88 inside the "marks" dictionary.

# a={'name': 'Rahul', 'marks': {'math': 95, 'science': 85}}
# a["marks"]["english"]=88
# print(a)

# output
# {'name': 'Rahul', 'marks': {'math': 95, 'science': 85, 'english': 88}}


# 20. Delete the subject "science" from inside "marks" .

# a={'name': 'Rahul', 'marks': {'math': 95, 'science': 85, 'english': 88}}
# del a["marks"]["science"]
# print(a)

# output
# {'name': 'Rahul', 'marks': {'math': 95, 'english': 88}}