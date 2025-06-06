"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
Questions:

When will a ValueError occur?
- When the value the user inputs is not an integer
When will a ZeroDivisionError occur?
- When the denominator the user inputs is 0
Could you change the code to avoid the possibility of a ZeroDivisionError?
If you could figure out the answer to question 3, then make this change now.
"""