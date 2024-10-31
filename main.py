cat_attributes = {
    "intelligence": 2,
    "energy": 30,
    "weight": 5,
}

print("Welcome to my cat game!")

name = input("Enter name of your new cat:")
colour = input("Enter colour of your new cat: )

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats")

    if option == '1':
        cat_attributes[energy] -= 1 
        pass
    elif option == '2':
        cat_attributes[intelligence] += 1
        pass
    
    elif option == '3':
        print("Your stats: ")
        for x in cat_attributes:
            print(f"Your cat's {x} in {cat_attributes[x]}")

    else:
    
        pass

    # finish off the if statements below
    if cat_attributes['energy'] < 0:
        print("Oh no! You just killed your cat")
        pass
    # elif ...
    
