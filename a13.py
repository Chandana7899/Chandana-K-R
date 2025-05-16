word = input("Enter a word: ")

# Reverse the word
reversed_word = word[::-1]

# Check if it's a palindrome
if word == reversed_word:
    print(word, "is a palindrome!")
else:
    print(word, "is not a palindrome.")
