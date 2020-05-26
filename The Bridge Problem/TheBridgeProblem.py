"""
Eyyup Demirkiran
In the code below, I wrote the algorithm of the problem in the Ted-Ed Youtube link.
Problem Youtube Link: https://www.youtube.com/watch?v=7yDmGnA8Hw0

dict1: refers to the names and speeds of those to the left of the bridge.
dict2: refers to the names and speeds of those to the right of the bridge.
def list1_random(): is the function to choose two people from the dictionary
def list2_random(): is the function to choose one people from the dictionary for returnning
def going(): is the function that determines the going speed of the chosen ones.
If you run the code on the command line,
the only desired situation in the problem will be printed on the screen.
"""
import random
import os

def list1_random(dict1,dict2):
    list1_selected1=random.choice(list1_keys)
    list1_keys.remove(list1_selected1)
    list2_keys.append(list1_selected1)
    list1_values.remove(dict1[list1_selected1])
    list2_values.append(dict1[list1_selected1])
    list1_selected2 = random.choice(list1_keys)
    list1_keys.remove(list1_selected2)
    list2_keys.append(list1_selected2)
    list1_values.remove(dict1[list1_selected2])
    list2_values.append(dict1[list1_selected2])
    dict2[list1_selected1] = (dict1[list1_selected1])
    dict2[list1_selected2] = (dict1[list1_selected2])
    print("Selected 1st person: %s"  %(dict1[list1_selected1]))
    print("Selected 2nd person: %s"  %(dict1[list1_selected2]))
    def going(list1_selected1, list1_selected2):
        if list1_selected1 > list1_selected2:
            return list1_selected1
        else:
            return list1_selected2
    print("Minute for going:", going(list1_selected1, list1_selected2))
    print("New list 1:", list1_values)
    print("New list 2:", list2_values)
    return going(list1_selected1, list1_selected2)

def list2_random(sozluk2):
    list2_selected = random.choice(list2_keys)
    list2_keys.remove(list2_selected)
    list1_keys.append(list2_selected)
    list2_values.remove(sozluk2[list2_selected])
    list1_values.append(sozluk2[list2_selected])
    print("Selected person for returning: %s" %(sozluk2[list2_selected]))
    print("Minute for returning:", list2_selected)
    print("New list 1:", list1_values)
    print("New list 2:", list2_values)
    return list2_selected

for i in range(1,301):
    os.system('cls')
    print("\n\n******** %d. Combinations. Found it! ********" % (i))
    dict1= {1: "Me" , 2: "Assistant" , 5: "Janitor" , 10: "Professor"}
    dict2= {}
    list1_keys   = list(dict1.keys())
    list1_values = list(dict1.values())
    list2_keys   = list(dict2.keys())
    list2_values = list(dict2.values())
    total = 0
    for j in range(1,3):
        print("%d.Tour------------------------------" %(j))
        Going_return1 = list1_random(dict1, dict2)
        Returning_return1 = list2_random(dict2)
        total = total+Going_return1+Returning_return1
    print("3.Tour-----------------------------------")
    Going_return3 = list1_random(dict1, dict2)
    total +=Going_return3
    print("\nTotal Minutes:", total)
    if total <=17:
        break




