# A palindrome reads the same backwards as forwards (ignoring capitalization).
# E.g. civic, madam.
# Write a Python script to ask for a word. 
# Print True if the word is a palindrom.
# Otherwise, False should be printed.
# E.g.
# Enter a word: Civic
# True
# Enter a string: Python
# False

word = input("Enter a word: ").lower()  # receive a string and convert to lowercase

print(word == word[::-1])