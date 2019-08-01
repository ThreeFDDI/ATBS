#!/usr/local/bin/python3

from collections import Counter

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: {}\n".format(item_total))

displayInventory(stuff)

def addToInventory(inventory, new_items):
    print("*** New lootz!! ***\n")
    for i in new_items:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
        

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(stuff, dragonLoot)

displayInventory(stuff)



