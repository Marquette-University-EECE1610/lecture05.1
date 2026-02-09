"""
Sum 1 to 5 (for loop)

GitHub Copilot Instructions:
- Write a short Python program that computes the sum of the integers from 1 to 5.
- Print ONLY the final total (no extra text).
- Add brief inline comments explaining what each section does.
- Add an assert with a failure output at the end of the program that verifies the output is 15.
"""

# Initialize total to 0
total = 0

# Loop through numbers 1 to 5 and add each to total
for i in range(1, 6):
    total += i

# Print the final sum
print(total)

# Assert that the sum equals 15 with a failure message
assert total == 15, f"Expected sum to be 15, but got {total}"

print(list(range(1, 6)))
