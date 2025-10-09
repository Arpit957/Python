friends = ["arpit", 2, "ankush","Om","Ankit"] 
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:4])
friends[1] = "Rohan"
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends.extend(lucky_numbers)
friends.append("Bata")
friends.insert(1, "Jay")
friends.remove("Om")
print(friends.index("Rohan"))
print(friends.count("Ankit"))
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)
friends.reverse()
print(friends)
friends2 = friends.copy()
print(friends2)