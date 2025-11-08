# 30 days of python day 9 - Conditionals

# 1. Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age = int(input("Enter your age: "))

print("You are old enough to drive.") if age >= 18 else print(f"You need {18-age} more years to learn to drive.")

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
if age > 19:
    print(f"You are {age-19} years older than me.")
elif age < 19:
    print(f"You are {19-age} years younger than me.")
else:
    print("You are the same age as me")

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number:"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num1} is equal to {num2}")

# Exercises: Level 2

# 1. Write a code which gives grade to students according to theirs scores: 80-100: A. 70-89: B. 60-69: C. 50-59: D 0-49: F.
grade = int(input("Enter your grade: "))
if grade >= 80:
    print("A")
elif grade >= 70:
    print("B")
elif grade >= 60:
    print("C")
elif grade >= 50:
    print("D")
else:
    print("F")

# 2. Check if the season is Autumn, Winter, Spring or Summer.
season = input("Enter a month: ").lower()

months = {
    "december":"winter",
    "january":"winter",
    "february":"winter",
    "march":"spring",
    "april":"spring",
    "may":"spring",
    "june":"summer",
    "july":"summer",
    "august":"summer",
    "september":"fall",
    "october":"fall",
    "november":"fall"
    }

print(f"{season.capitalize()} is in {months.get(season)}.")

# 3. If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ")
if new_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(new_fruit)
    print(fruits)

# Exercises: Level 3

# 1. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if "skills" in person:
    mid_length = len(person["skills"]) // 2
    middle_skill = person["skills"][mid_length:mid_length + 1]
    print(f"Middle Skill: {middle_skill}")

    if "Python" in person["skills"]:
        print("The person has Python skills.")
    else:
        print("The person does not have Python skills.")

    front_end = ["Javascript", "React"]
    back_end = ["Node", "Python", "MongoDB"]
    full_stack = ["React", "Node", "MongoDB"]
    
    set_skills = set(person["skills"])
    if set_skills == set(front_end):
        print("This person is a front end developer")
    elif set(back_end).issubset(set_skills):
        print("This person is a back end developer")
    elif set(full_stack).issubset(set_skills):
        print("This person is a full stack developer")
    else:
        print("Unknown Title")

    if person["is_marred"] == True and person["country"] == "Finland":
        print(f"{person["first_name"]} {person["last_name"]} lives in Finland. He is married")