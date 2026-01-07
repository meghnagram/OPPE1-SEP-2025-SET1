
def compare_last_digits(num1:int, num2:int) -> str:
    '''
    Given two integers, check whether their last digits are the same.

    Args:
        num1 (int): First number
        num2 (int): Second number

    Returns:
        str: "same" if last digits match else "different"
    '''
    
    return "same" if num1 % 10 == num2 % 10 else "different"

# Compare Last Digits
# Write a function compare_last_digits(num1, num2) that takes two integers as input and checks whether they have the same last digit.
# Return "same" if the last digits match, otherwise return "different".

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# compare_last_digits(123, 43) -> "same" # Last digit of both is 3
# compare_last_digits(56, 78) -> "different" # Last digits are 6 and 8
# compare_last_digits(90, 0) -> "same" # Last digit of both is 0
