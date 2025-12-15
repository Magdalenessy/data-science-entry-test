def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return -1

    if divisor == 0:
        return False

    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:

result1 = check_divisibility(10, 2)
print(result1)   # Output: True

result2 = check_divisibility(7, 3)
print(result2)   # Output: False
def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return -1

    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
result1 = string_reverse("Hello World")
print(result1)   # Output: "dlroW olleH"

result2 = string_reverse("Python")
print(result2)   # Output: "nohtyP"
