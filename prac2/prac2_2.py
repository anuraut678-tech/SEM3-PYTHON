# Original nested tuple of subjects
nested_tuple = (
    ("Java", 101),
    ("Database Management System", 102),
    ("Machine Learning", 103)
)

# Sorting the nested tuple by subject code (index 1)
sorted_subjects = sorted(nested_tuple, key=lambda x: x[1])

# Display the sorted result
print("Sorted Subjects (by subject code):", sorted_subjects)
