#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:2]
word_last_2 = word[-2:]
first_word, *middle_word, last_word = word.split()
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
