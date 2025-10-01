# Take input
num = int(input("Enter a number: "))

original = num
reverse = 0

# Reverse the number using a loop
while num > 0:
    digit = num % 10          # get last digit
    reverse = reverse * 10 + digit  # build reversed number
    num //= 10                # remove last digit

# Check palindrome
if original == reverse:
    print(original, "is a Palindrome")
else:
    print(original, "is NOT a Palindrome")
