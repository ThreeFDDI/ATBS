#!/usr/local/bin/python3

catNames = [ "Zophie", "Pooka", "Simon", "Lady Macbeth", "Fat-tail", "Miss Cleo" ]

#catNames = []

#while True:
#    print("\nEnter the name of cat #" + str(len(catNames) + 1) + " ( Or enter nothing to quit): ")
#    name = input()
#    if name == "":
#        break
#    catNames = catNames + [name] # list concatenation

print("The cat names are:")
for name in catNames:
    print("   {}".format(name))

print("\n" + "~"*30 + "\n")

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print("\n" + "~"*30 + "\n")

name = "Sismons"

if name not in catNames:
    print("Pet \"{}\" not found".format(name))
else:
    print("{} is my pet.".format(name))

print("\n" + "~"*30 + "\n")

