word = input("Enter a word: ")

# Convert to lowercase for easier checking
word = word.lower()

# Define vowels
vowels = "aeiou"

# Count vowels
count = 0
for letter in word:
    if letter in vowels:
        count += 1

# Print the result
print("Number of vowels in", word, "is", count)
