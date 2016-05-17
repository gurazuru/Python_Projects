#Automate the Boring Stuff Chapter 5
#inventory.py
#updates inventory with new loot from after killing the dragon
stuff = {'gold coin': 42, 'rope': 1}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

def newLoot(addedLoot):
    for item in addedLoot:
        if item in stuff:
            stuff[item] = stuff[item] + 1
        else:
            stuff[item] = 1

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print(dragonLoot)
newLoot(dragonLoot)
displayInventory(stuff)
