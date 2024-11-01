cat_attributes = {
    "intelligence": 2,
    "energy": 10,
    "weight": 5,
}

print("Welcome to my cat game!")

name = input("Enter name of your new cat:")
colour = input("Enter colour of your new cat: ")


while True:
    
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Show stats 4. Feed your cat 5. Put to sleep > ")

    if option == '1':
        cat_attributes['energy'] -= 3 
        pass
    elif option == '2':
        cat_attributes['intelligence'] += 2 
        cat_attributes['energy'] -= 1
        pass
    
    elif option == '3':
        print("Your stats: ")
        for x in cat_attributes:
            print(f"Your cat's {x} is {cat_attributes[x]}")
    
    elif option == '4':
        cat_attributes['weight'] += 1
        cat_attributes['energy'] += 2
        pass

    elif option == '5':
        cat_attributes['energy'] += 5

    else:
    
        pass

    if cat_attributes['energy'] < 5: 
        print("You are abusing your cat, please increase its energy before it drops dead.")

    if cat_attributes['energy'] < 0:
        print("Oh no! You just killed your cat")
        quit()
     
    elif cat_attributes['energy'] > 0:
        print("Keep going! Give your cat more energy")

   
    if cat_attributes['weight'] > 10:
        print("Your cat is too obsese. You cannot feed your cat. ")

    if option == 4:
        print("You cannot feed your cat anymore. It's too obese.")
        quit()

    


    
