num = int(input("Enter a number: "))

factorial = 1

# Calculate factorial using a for loop
for i in range(1, num + 1):
    factorial *= i

# Print the result
print("The factorial of", num, "is", factorial)
