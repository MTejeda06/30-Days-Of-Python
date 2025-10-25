# 30 days of python day 5 - Lists

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
list_5 = [1,2,3,4,5,6]

# 3. Find the length of your list
print(f"Length of list: {len(list_5)}")

# 4. Get the first item, the middle item and the last item of the list
first_item = list_5[0]
middle_item = list_5[len(list_5) // 2]
last_item = list_5[-1]
print(f"first item: {first_item}\nmiddle item: {middle_item}\nlast item: {last_item}")
 
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Marc", 19, 68, "Single", "3700 Libra Dr"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(f"number of companies: {len(it_companies)}")

# 9. Print the first, middle and last company
print(f"first company: {it_companies[0]}")
print(f"middle company: {it_companies[len(it_companies) // 2]}")
print(f"last company: {it_companies[-1]}")

# 10. Print the list after modifying one of the companies
it_companies[4] = "NVIDIA"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("AMD")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Discord")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
str_join = "#; ".join(it_companies)
print(str_join)

# 15. Check if a certain company exists in the it_companies list.
print(f"is Amazon in companies list? {"Amazon" in it_companies}")

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(f"first 3 companies: {it_companies[:3]}")

# 19. Slice out the last 3 companies from the list
print(f"last 3 companies: {it_companies[-3:]}")

# 20. Slice out the middle IT company or companies from the list
mid_index = len(it_companies) // 2
print(f"middle company: {it_companies[mid_index:mid_index+1]}")

# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
del it_companies[3:5]
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_back = front_end + back_end
print(front_back)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_back.copy()
full_stack.insert(full_stack.index("Redux")+1, "Python")
full_stack.insert(full_stack.index("Python")+1, "SQL")
print(full_stack)

# Exercises: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max ages
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(f"min age: {min_age} max age: {max_age}")

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

# Find the median age (one middle item or two middle items divided by two)
print(ages)
mid_ages = ages[len(ages) // 2 - 1:len(ages) // 2 + 1]
median = (mid_ages[0] + mid_ages[1])/2
print(f"median age: {median}")

# Find the average age (sum of all items divided by their number )
average = sum(ages) / len(ages)
print(f"average: {average}")

# Find the range of the ages (max minus min)
min_age = min(ages)
max_age = max(ages)
print(f"range: {max_age - min_age}")

# Compare the value of (min - average) and (max - average), use abs() method
abs_min = abs(min_age - average)
abs_max = abs(max_age - average)
print(f"min - average: {abs_min}\nmax - average: {abs_max}")
print(f"3.25 > 3.75? {abs_max > abs_min}")

# Countries
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

# Find the middle country(ies) in the countries list
# length is odd, so 1 lies in the middle
middle_country = countries[len(countries) // 2]
print(middle_country)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
left_half = countries[:len(countries) // 2 + 1]
right_half = countries[len(countries) // 2 + 1:]
print(left_half)
print(right_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
China, Russia, US, *scandic = countries_2
print(China, Russia, US, scandic)