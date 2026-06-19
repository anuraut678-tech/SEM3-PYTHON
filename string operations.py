#String operations

sentence = input("Enter a sentence: ")

words = len(sentence.split())
characters = len(sentence)

print("Word Count =", words)
print("Character Count =", characters)

print("Lowercase =", sentence.lower())
print("Uppercase =", sentence.upper())

print("With Underscores =", sentence.replace(" ", "_"))
