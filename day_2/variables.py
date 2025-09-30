# Day 2: 30 days of python programming

import math

# Declare Variables
first_name = "Marc"
last_name = "Tejeda"
full_name = "Marc Tejeda"
country = "United States"
city = "Orlando"
age = 19
year = 2025
is_married = False
is_true = True
is_light_on = False
var1, var2, var3, var4 = 1, "Hello", 2.34, [1,2,3]

# Print the type of each variable
all_variables = [first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on, var1, var2, var3, var4]

for var in all_variables:
    print(type(var), "\n")

# Length of first name
print("My first name is", len(first_name), "Characters long!")

# Compare length of first & last"
print("My first name is", len(first_name), "Characters long, and my last name is", len(last_name), "Characters long, which means my last name is longer!")

# Arithmetic
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one = num_two
remainder = num_two%num_one
exp = num_one ** num_two
floor_divison = num_one//num_two

# Area of a circle with radius 30
radius = 30
area_of_circle = math.pi * (radius ** 2)
circum_of_cricle = (2*math.pi) * radius

# With radius as user input
input_radius = int(input("What is the radius of the circle? \n"))
input_area = math.pi * (input_radius ** 2)
print("The area of the circle is", input_area)

# Gather info about the user
user_fname = input("What is your first name?\n")
user_lname = input("What is your last name?\n")
user_country = input("What country do you live in?\n")
user_age = input("How old are you?\n")

# Reserved keywords
help("keywords")

