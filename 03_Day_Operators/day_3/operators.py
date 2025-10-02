# Day 2: 30 days of python programming

import math

# Declare data types
age = 19
height = 68.0
comp = 1 + 1j

# Calculate area of a triangle
base = int(input("Enter base: "))
height = int(input("Enter height: "))
print("The area of the triangle is", 0.5 * base * height)

# Calculate perimeter of a triangle
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
print("The perimeter of the triangle is", side_a+side_b+side_c)

# Calculate area & perimeter of a rectangle
rect_length = int(input("Enter rectangle length: "))
rect_width = int(input("Enter rectangle width: "))
print("The area of the rectangle is", rect_length*rect_width, "and the perimeter is", 2*(rect_length+rect_width))

# Calculate area & circumference of a circle
rad = int(input("Enter the radius of the circle: "))
print("The area of the circle is", math.pi*(rad**2), "and the circumference is", 2*math.pi*rad)

# Slope, x-intercept, and y-intercept of y = 2x-2
slope1 = 2
print("The slope of y = 2x-2 is " + str(slope1), "the y-intercept is -2, and the x-intercept is 1")

# Slope & Euclidean distance between (2,2) and (6,10)
slope2 = (10-2)/(6-2)
euc_dist = math.sqrt((2-6)**2 + (2-10)**2)
print("The slope between (2,2) and (6,10) is", slope2, ". The Euclidean distance is" , euc_dist)

# Which is bigger?
print("Is the 1st slope larger? ", slope1 > slope2)

# y = x^2 + 6x + 9
def what_is_y(x):
    return x**2 + 6*x + 9

print("Different values of y = x^2 + 6x + 9\nx=0: ", what_is_y(0), "\nx=5: ", what_is_y(5), "\nx=25", what_is_y(25))

# "python" vs "dragon"
print("Is \"python\" longer than \"dragon\"? ", len("python") > len("dragon"))

# Is there jargon in this course?
check_jargon = "I hope this course is not full of jargon"
print(f"is \"jargon\" in \"{check_jargon}\"? {'jargon' in check_jargon}")

# "python" and "dragon"... again!
print(f"is there no \"on\" in both \"dragon\" and \"python\"? {('on' not in 'python') and ('on' not in 'dragon')}")

# convert length to float and string
python_length = len("python")
length_float = float(python_length)
length_string = str(length_float)

# How do you check if a number is even or not using python?
# You can use mod operator, or the bitwise operator for some extra speed
num = 3
is_even = num%2 == 0
is_even = (num & 1) == 0

# floor division equality
print(f"is the floor division of 7 by 3 is equal to the int converted value of 2.7? {7//3 == int(2.7)}")

# compare data types. note: int(9.8) is invalid, so must convert to float first
print(f"is the data type of \"10\" equal to the data type of 10? {type('10') == type(10)}")
print(f"is the data type of int(\"9.8\") equal to the data type of 10? {type(int(float('9.8'))) == type(10)}")

# calculate pay rate
hours = int(input("Enter hours: "))
pay = int(input("Enter rate per hour: "))
print(f"Your weekly earning is {hours*pay}")

# years to seconds
years = int(input("Enter number of years you have lived: "))
print(f"You have lived for {years*60*60*24*365} seconds")

# print a table of numbers
print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")

