"""
Buggy Loop for Debugging (INTENTIONAL BUGS)

GitHub Copilot Instructions:
- Write a Python program that asks the user to enter integers.
- The program should stop when the user enters 0.
- The program should compute the sum of all negative numbers entered.
- At the end, print the sum.

IMPORTANT:
- Intentionally include THREE logic bugs related to looping.
- The program should still run without syntax errors.
- Do NOT comment where the bugs are.
- The bugs should require step-through tracing to discover.

Suggested bug types (choose at least one):
- Off-by-one error in counting or summing
- Incorrect loop condition that causes one extra iteration
- Updating the sum in the wrong place
- Failing to update the loop control variable correctly
- Reading input at the wrong time (before vs. inside the loop)

Requirements:
- Use a while-loop.
- Use variables named `num` and `total`.
- Use the prompt: "Enter an integer (0 to stop): "
- Print only the final sum (no extra text).
"""

total = -1
num = int(input("Enter an integer (0 to stop): "))

while num != 0:
    if num < 0:
        total = total + num
    total = total + num
    num = int(input("Enter an integer (0 to stop): "))

total = total + num
print(total)
