#List operations

numbers = [12, 45, 67, 23, 89, 34, 56, 78, 90, 11]

print("List =", numbers)

print("Maximum =", max(numbers))
print("Minimum =", min(numbers))
print("Average =", sum(numbers) / len(numbers))

print("Ascending =", sorted(numbers))
print("Descending =", sorted(numbers, reverse=True))

new_num = int(input("Enter a new number: "))
numbers.append(new_num)

numbers.pop(0)

print("Updated List =", numbers)
