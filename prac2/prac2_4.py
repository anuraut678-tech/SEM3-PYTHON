# Create a tuple
subject = ("Java ", 101)

# Try to modify an element in the tuple
try:
    subject[1] = 999  # Attempt to change the subject code
except TypeError as e:
    print("Tuple is immutable! Error:", e)
