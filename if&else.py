is_male = True
is_Tall = False  

if is_male and is_Tall:
    print("You are a tall male")
elif is_male and not(is_Tall):
    print("You are a short male")
elif not(is_male) and is_Tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and not tall")