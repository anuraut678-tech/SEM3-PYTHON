# a, b, c, d - Create a list and display it
numbers = [10, 20, 30, 20, 40]

print("Original List:", numbers)

# a. Find the largest number
print("Largest Number:", max(numbers))

# b. Remove duplicates
unique_numbers = list(set(numbers))
print("List without Duplicates:", unique_numbers)

# c. Count even numbers
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("Count of Even Numbers:", even_count)

# d. Display the list
print("Stored List:", numbers)

# e. Function to calculate average
def average(lst):
    return sum(lst) / len(lst)

print("Average of List:", average(numbers))

# f. Convert a string into a list of characters
text = "Python"
char_list = list(text)
print("List of Characters:", char_list)

# g. Join list elements into a single string
words = ["Python", "is", "easy"]
joined_string = " ".join(words)
print("Joined String:", joined_string)
