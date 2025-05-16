a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Find the maximum of the two
max_num = max(a, b)

# Find the least common multiple (LCM)
while True:
    if max_num % a == 0 and max_num % b == 0:
        print("The next common multiple of", a, "and", b, "is", max_num)
        break
    max_num += 1
