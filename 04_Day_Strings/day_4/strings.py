# 30 days of python day 4 - Strings

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1 = "Thirty"
str2 = "Days"
str3 = "Of"
str4 = "Python"
result = str1 + str2 + str3 + str4

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str5 = "Coding"
str6 = "For"
str7 = "All"
result2 = str5 + str6 + str7

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
print(company.split()[0])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding" in company)

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
str12 = "Python for Everyone"
print(str12.replace("Everyone", "All"))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
str14 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str14.split(","))

# 15. What is the character at index 0 in the string Coding For All.
# "C"
str15 = "Coding For All."
print(company[0])

# 16. What is the last index of the string Coding For All.
# 14
print(len(str15)-1)

# 17. What character is at index 10 in "Coding For All" string.
# " "
print(str15[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
letters = []
for word in str12.split():
    letters.append(word[0].upper())
print("".join(letters))

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
letters2 = []
for word in company.split():
    letters2.append(word[0].upper())
print("".join(letters2))

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(str15.index("C"))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(str15.index("F"))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People.".rfind("l"))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".find("because"))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".rindex("because"))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
because_str = "You cannot end a sentence with because because because is a conjunction"
print(because_str[because_str.find("because"):because_str.rfind("because") + len("because")])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(because_str.find("because"))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(because_str[because_str.find("because"):because_str.rfind("because") + len("because")])

# 28. Does ''Coding For All' start with a substring Coding?
# Yes
print("Coding For All".startswith("Coding"))

# 29. Does 'Coding For All' end with a substring coding?
# No
print("Coding For All".endswith("coding"))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())

# 31. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
# The 2nd one
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print( "#" + " #".join(libraries))

# 33. Use the new line escape sequence to separate the following sentences: I am enjoying this challenge. I just wonder what is next.
enjoy_str = "I am enjoying this challenge. I just wonder what is next."
print(enjoy_str.replace(". ", "\n"))

# 34. Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki")

# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
print(f"The area of a circle with radius {radius} is {int(area)} meters square")

# 36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
print(f"8 + 6 = {8+6}")
print("8 - 6 = {}".format(8-6))
print(f"8 * 6 = {8*6}")
print("8 / 6 = %.2lf" %(1.33))
print("8 % 6 = {}".format(8%6))
print(f"8 // 6 = {8//6}")
print("8 ** 6 = %d" %(8**6))