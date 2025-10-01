#1.
# for i in range(1, 11):
#     if (i&1):
#         print(i * 2)
#     else:
#         print(i)

#2.
# Take input from the user
# Take 3 numbers as input
for i in range(3):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

