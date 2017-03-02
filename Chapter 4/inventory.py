#display a dictionary appropriately

def displayInventory(dictionary):
    print("Inventory:")
    counter = 0
    for k, v in dictionary.items():
        print(str(v) + " " + str(k))
        counter += v

    print("Total number of items: " + str(counter))

def addToInventory(inventory, addedItems):

    for i in range(len(addedItems)):
        if inventory.get(addedItems[i], 0) == 0:
            inventory[addedItems[i]] = 1
        else:
            inventory[addedItems[i]] += 1


##Test Section Start
stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow':12
    }
testStuff = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(stuff)
addToInventory(stuff, testStuff)
displayInventory(stuff)

###Test Section End

