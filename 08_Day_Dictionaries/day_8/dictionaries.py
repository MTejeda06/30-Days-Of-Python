# 30 days of python day 8 - Dictionaries

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog["Name"] = "Thor"
dog["Breed"] = "German Shepherd"
dog["Legs"] = 4
dog["Age"] = 3
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name":"Max",
    "last_name":"Hectorson",
    "gender":"Male",
    "age":21,
    "marital_status":"Single",
    "skills":["Guitar", "Bowling", "Writing", "Pickleball"],
    "country":"United States",
    "city":"Winter Park",
    "address":"4949 Mary Lane"
}
print(student)

# 4. Get the length of the student dictionary
print("Length of student dictionary: ", len(student))

# 5. Get the value of skills and check the data type, it should be a list
skills = student.get("skills")
print("skills data type:", type(skills))

# 6. Modify the skills values by adding one or two skills
student["skills"].append("Running")
print(student)

# 7. Get the dictionary keys as a list
keys_list = student.keys()
print(keys_list)

# 8. Get the dictionary values as a list
values_list = student.values()
print(values_list)

# 9. Change the dictionary to a list of tuples using items() method
print("\n\n", student.items())

# 10. Delete one of the items in the dictionary
del student["address"]

# 11. Delete one of the dictionaries
del student