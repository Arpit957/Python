# Take input
num = int(input("Enter a number: "))

# Convert number to string to count digits
digits = str(num)
power = len(digits)

# Calculate sum of digits raised to power
armstrong_sum = sum(int(d)**power for d in digits)

# Check condition
if num == armstrong_sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
