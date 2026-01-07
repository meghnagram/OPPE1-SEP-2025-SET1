
def move_even_indices_to_end_reversed(t):
    '''
    Given a tuple `t`, move all elements at even indices to the end
    in reversed order, while keeping odd-indexed elements as they are.

    Example:
    >>> t = (10, 20, 30, 40, 50)
    >>> move_even_indices_to_end_reversed(t)
    (20, 40, 50, 30, 10)

    Args:
        t (tuple): The input tuple.

    Returns:
        tuple: A new tuple with odd-indexed elements followed by reversed even-indexed elements.
    '''
    
    return t[1::2] + t[::2][::-1]

# Move Even Indices to End (Reversed)
# Given a tuple t, write a function move_even_indices_to_end_reversed to move all elements at even indices to the end of the tuple in reversed order, while keeping the odd-indexed elements in their original order.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> t = (10, 20, 30, 40, 50)
# >>> move_even_indices_to_end_reversed(t)
# (20, 40, 50, 30, 10)
# Explanation

# even-indexed elements = (10, 30, 50)
# reversed evens = (50, 30, 10)
# odd-indexed elements = (20, 40)
Final output = (20, 40, 50, 30, 10)
