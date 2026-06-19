#Python code to swap two numbers.

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

swap(numbers, 1, 3)

print("Updated List:", numbers)
