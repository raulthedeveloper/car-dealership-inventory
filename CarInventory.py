# Car inventory Dictionary
import sys, json
inventory = {}

# Add List to Dictionary properties to add more models to brands

def addToDatabase():
    print(f"Current inventory {inventory}")
    print('Enter car Make')
    brand = str(input()).lower()
    brand.lower()

    print('Please enter model name')
    model = str(input()).lower()

    if brand in inventory:

        if model in inventory[brand]:
            print(f"{brand} {model} is in stock")
        else:
            # check for duplicates

            if model in inventory[brand]:
                print('Model already exist \n')
                print(" ")
            else:
                print('Model doesnt exist \n')
                print(" ")
                inventory[brand].append(model)
                print('Database updated \n')

    else:
        # Creates initial data
        print('Model doesnt exist')
        inventory[brand] = []
        inventory[brand].append(model)
        print('Database updated')




def saveFile():
    json_object = json.dumps(inventory, indent=4)

    with open('output.json', 'w') as outfile:
        jsonString = json.dumps(json_object)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

    print(json_object)


def removeData():
    print('What would you like to look into')
    print(inventory)
    brand = input()
    print('What model do you want to remove')
    print(inventory[brand])
    model = input()
    inventory[brand].remove(model)

    if inventory[brand] == []:
        del inventory[brand]


while True:
    print("What would you like to do? [add, remove, print, exit, view]")

    choice = input()

    if choice == 'add':
        addToDatabase()
    elif choice == 'save':
        saveFile()
    elif choice == 'exit':
        sys.exit()
    elif choice == 'view':
        print(inventory)
    elif choice == 'remove':
        removeData()
    else:
        print('Please enter valid command')



