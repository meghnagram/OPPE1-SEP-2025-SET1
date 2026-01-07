

import re
line = input()

result = ""
for char in line:
  if char.isalpha() or char.isdigit():
    result += char.lower()
  else:
    result+='-'


parts = [word for word in result.strip('-').split('-') if word]
print('-'.join(parts))

# Create Slug from String
# Given a string, generate its slug version.

# A slug is created by:

# Replacing every character that is not an English alphabet letter (a-z, A-Z) nor a digit (0-9) with a hyphen -.
# Collapsing consecutive hyphens into a single hyphen.
# Removing any leading or trailing hyphens.
# Converting to lowercase.
# Print the resulting slug.

# NOTE: This is an I/O type problem. You must read from standard input and write to standard output.

# Input Format
# A single line containing the original string S. S may contain spaces, punctuation, symbols, etc.

# Output Format
# A single line containing the slug of S after applying the four rules above.
# If the resulting slug is empty, output an empty line.

# Example
# Input

# Hello, World! (2023)
# Output

# hello-world-2023
# Explanation

# Non-alphanumeric characters (space, comma,!, and '()') become - -> "Hello--World---2023-"
# The sequence -- is collapsed to a single - -> "Hello-World-2023-"
# Removed Trailing hyphen -> "Hello-World-2023"
# Lowercased -> "hello-world-2023"
