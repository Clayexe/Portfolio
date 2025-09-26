# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 17:59:31 2025

@author: Clay Smith
"""

#Adventure Game, Clay Smith
print("Last night, you went to sleep in your own bed.")
print("Now, you wake up in a locked room in a castle.")
print("Could there be a key hidden somewhere?")

#The Menu Function:
def menu(list,question):
    for item in list:
        print(1+list.index(item), item)
    return int(input(question))

#This is a list of items in the room
items=["book","vase","picture","desk", "chest"]
import random
keylocation=random.randint(1,5)

#the key is not found
keyfound="No"
loop=1

#Display the menu until the key is found:
while loop == 1:
    choice = menu(items,"What do you want to inspect?")
    print("")
    if choice < 6:     
        if choice == keylocation:
            print("You found a small key in the", items[choice -1])
            keyfound = "Yes"
            break
        else:
            print("You found nothing in the", items[choice -1])
    elif choice == 0:
        if keyfound == "Yes" :
            loop=0
            print("You insert the key in the keyhole and turn it.")
        else:
            print("The door is locked. You need to find a key.")
    else:
        print("Choose a number less than 5.")
print("You open the door to your freedom.")
        