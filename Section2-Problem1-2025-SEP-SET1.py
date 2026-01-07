
def remove_duplicates(s: str) -> str:
    """Removes duplicate characters, keeping the first occurrence."""
    
    
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
    

# Remove Duplicate Characters from String
# Write a function remove_duplicates(s) that returns a new string with duplicate characters removed, preserving the original order of first appearance.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> s = "banana"
# >>> remove_duplicates(s)
# 'ban'
# >>> s = "hello"
# >>> remove_duplicates(s)
# 'helo'
# >>> s = "abc"
# >>> remove_duplicates(s)
# 'abc'
