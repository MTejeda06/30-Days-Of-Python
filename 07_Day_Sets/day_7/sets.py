# 30 days of python day 7 - Sets

# Exercises: Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(it_companies)

# 1. Find the length of the set it_companies
print(f"The length of it_companies is {len(it_companies)}")

# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["Meta", "NVIDIA", "AMD"])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.discard("IBM")
print(it_companies)

# 5. What is the difference between remove and discard
# Remove raises an error if the item is not in the set, discard does not

# Exercises: Level 2

# 1. Join A and B
C = A.union(B)
print(C)

# 2. Find A intersection B
intersection = A.intersection(B)
print(intersection)

# 3. Is A subset of B
print(f"Is A subset of B? {A.issubset(B)}")

# 4. Are A and B disjoint sets
print(f"Are A and B disjoint sets? {A.isdisjoint(B)}")

# 5. Join A with B and B with A
A_B = A.union(B)
B_A = B.union(A)
print(A_B, B_A)

# 6. What is the symmetric difference between A and B
print(f"What is the symmetric difference between A and B? {A.symmetric_difference(B)}")

# 7. Delete the sets completely
del A, B, C, it_companies, age, intersection, A_B, B_A

# Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
len_list = len(age)
len_set = len(age_set)
print(f"Length of list: {len_list}\nLength of set: {len_set}\nThe list is bigger.")

# 2. Explain the difference between the following data types: string, list, tuple and set
# Strings and tuples are immutable, lists and sets are mutable
# Strings, lists, and tuples are ordered, sets are not
# Sets do not allow duplicates, and are indexed, while the other 3 are indexed, and allow duplicates
# Strings only allow 1 data type, while the other 3 can store multiple

# 3. How many unique words have been used in this sentence?
sentence = "I am a teacher and I love to inspire and teach people."
sentence_set = set(sentence[:-1].split())
print(sentence)
print(f"There are {len(sentence_set)} unique words in the sentence")