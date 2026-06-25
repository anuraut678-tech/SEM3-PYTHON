# a. Create a tuple with 5 different elements and print it
subjects = ("TOC", "DBMS", "ML", "AI", "Scala")
print("Original Tuple:", subjects)

# b. Access the first and last elements using indexing
print("\nFirst Element:", subjects[0])
print("Last Element:", subjects[-1])

# c. Slice the tuple and print the middle 3 elements
print("\nMiddle 3 Elements:", subjects[1:4])

# d. Concatenate two tuples and print the result
extra_subjects = ("OS", "Python")
concatenated_tuple = subjects + extra_subjects
print("\nConcatenated Tuple:", concatenated_tuple)

# e. Reverse a tuple using slicing
reversed_tuple = subjects[::-1]
print("\nReversed Tuple:", reversed_tuple)

# f. Count how many times an element appears in a tuple
sample_tuple = ("AI", "DBMS", "AI", "ML", "AI")
print("\nCount of 'AI':", sample_tuple.count("AI"))

# g. Find the index of a specific element in a tuple
print("Index of 'ML':", subjects.index("ML"))

# h. Check if an element exists in a tuple
element = "Scala"
if element in subjects:
    print(f"'{element}' exists in the tuple.")
else:
    print(f"'{element}' does not exist in the tuple.")

# i. Convert a list to a tuple
subject_list = ["Java", "Python", "Scala"]
tuple_from_list = tuple(subject_list)
print("\nTuple from List:", tuple_from_list)

# j. Sort a tuple of numbers in ascending order
numbers = (45, 12, 78, 23, 9)
sorted_numbers = tuple(sorted(numbers))
print("\nSorted Tuple:", sorted_numbers)

# k. Repeat a tuple 3 times using the * operator
repeated_tuple = ("AI", "DBMS") * 3
print("\nRepeated Tuple:", repeated_tuple)

# l. Check tuple immutability by trying to modify an element
try:
    subjects[0] = "Python"
except TypeError as e:
    print("\nTuple Immutability Test: Error ->", e)
