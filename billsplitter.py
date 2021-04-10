import random

friends_num = int(input("Enter the number of friends joining (including you):\n"))
print("Enter the name of every friend (including you), each on a new line:")
friends = {input(): 0 for _ in range(friends_num)}
amt = int(input("Enter the total bill value:\n"))
choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
if choice == "Yes":
    name = random.choice(list(friends.keys()))
    print(f"{name} is the lucky one!")
    if amt > 0 and friends_num > 0:
        bill = round(amt / (friends_num - 1), 2)
        friends = {friend: bill for friend in friends}
        friends[name] = 0
if choice == "No":
    print("No one is going to be lucky")
    if amt > 0 and friends_num > 0:
        bill = round(amt / friends_num, 2)
        friends = {friend: bill for friend in friends}
print(friends)
