# 30 days of python day 6 - Tuples

# Exercises: Level 1

# 1. Create an empty tuple
tup = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Alex", "Jacob", "Mason")
sisters = ("Samantha", "Emily", "Lily")
print(brothers, sisters)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# 4. How many siblings do you have?
print(f"I have {len(siblings)} siblings.")

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Rick", "Maria")
print(family_members)

# Exercises: Level 2

# 1. Unpack siblings and parents from family_members
brother1, brother2, brother3, sister1, sister2, sister3, dad, mom = family_members

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Apple", "Banana", "Pineapple")
vegetables = ("Lettuce", "Potato", "Carrot")
animal_products = ("Cheese", "Milk", "Butter")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid = len(food_stuff_tp) // 2
middle_food = food_stuff_tp[mid:mid+1]
print(middle_food)

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"Is Estonia a nordic country? {'Estonia' in nordic_countries}")
print(f"Is Iceland a nordic country? {'Iceland' in nordic_countries}")