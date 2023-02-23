'''
Homework 3-3
Name: Zachary Pace
Date: 2/22/2023
Description: Make inventory functions
'''


# Function Definitions
def printInventory(inventory):
    print("# | Item")
    for k in inventory.keys():
        print(str(inventory[k]) + " | " + str(k))


def addItem(inventory, item):
    if item not in inventory:
        inventory[item] = 1
    else:
        inventory[item] += 1


def delItem(inventory, item):
    if item in inventory:
        inventory[item] -= 1
    if inventory[item] == 0:
        del inventory[item]


# Instantiate inventory
store = {'Hand sanitizer': 10, 'Soap': 6, 'Kleenex': 22, 'Lotion': 16, 'Razors': 12}

# test addItem
for i in range(10):
    addItem(store, "Mask")

# test delItem
for i in range(4):
    delItem(store, "Kleenex")

# test printInventory
printInventory(store)
