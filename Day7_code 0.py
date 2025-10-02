# ---------------- Day 1 – Star Patterns ----------------

# 1. Left-aligned triangle
for i in range(1, 6):
    print("*" * i)

# 2. Inverted triangle
for i in range(5, 0, -1):
    print("*" * i)

# 3. Right-aligned triangle
for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

# 4. Pyramid pattern
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))

# 5. Inverted pyramid
for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))


# ---------------- Day 2 – Number Patterns ----------------

# 6. 1 to 5 in each row
for i in range(5):
    print("12345")

# 7. Increasing triangle of numbers
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 8. Reverse numbers in each row
for i in range(3):
    print("54321")

# 9. Row-wise increasing numbers
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 10. Centered number pyramid
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()


# ---------------- Day 3 – Alphabet Patterns ----------------

# 11. A to E in each row
for i in range(5):
    print("ABCDE")

# 12. Increasing triangle of alphabets
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

# 13. Row-wise increasing alphabets
ch = 65
for i in range(1, 5):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

# 14. Alphabet pyramid
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()

# 15. Right-aligned alphabets
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(i):
        print(chr(65 + j), end="")
    print()


# ---------------- Day 4 – Logical Loops ----------------

# 16. Even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# 17. Odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# 18. Sum of 1 to n
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)

# 19. Factorial of a number
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

# 20. Table of a number
n = 7
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# ---------------- Day 5 – While Loop Practice ----------------

# 21. Print 1 to 10
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

# 22. Sum of digits
n = 1234
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n //= 10
print("Sum of digits:", sum_digits)

# 23. Reverse a number
n = 1234
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed:", rev)

# 24. Palindrome number
n = 121
original = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
if rev == original:
    print("Palindrome")
else:
    print("Not Palindrome")

# 25. Armstrong number (3-digit)
n = 153
original = n
sum = 0
while n > 0:
    digit = n % 10
    sum += digit ** 3
    n //= 10
if sum == original:
    print("Armstrong")
else:
    print("Not Armstrong")


# ---------------- Day 6 – Nested Loops ----------------
# 26. Solid Square
for i in range(5):
    print("* " * 5)

# 27. Rectangle (3x6)
for i in range(3):
    print("* " * 6)

# 28. Hollow Square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 29. Hollow Right Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 30. Floyd’s Triangle
num = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()
# 31. Diamond Pattern
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 32. Pascal’s Triangle
from math import comb
n = 5
for i in range(n):
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(comb(i, j), end=" ")
    print()

# 33. Checkerboard Pattern (X-O)
for i in range(5):
    for j in range(5):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()

# 34. Hourglass Pattern
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 35. Binary Triangle Pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()
