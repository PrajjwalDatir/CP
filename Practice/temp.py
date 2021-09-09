# create list display display

def append_to_list(mylist, new_item):
    myList.append(new_item)

def insert_in_list(mylist, new_item, index):
    myList.insert(index, new_item)

def len_list(mylist):
    return len(myList)

def remove_from_list(mylist, item):
    myList.remove(item)

def del_from_list(mylist, index):
    del myList[index]


myList = []
while(True):
    print('''Choose from the following options :\n
    Press 1 to append to the list\n
    Press 2 to insert to list\n
    Press 3 to get length of list\n
    Press 4 to remove from the list\n
    Press 5 to del from list\n\n''')
    new_item = input("Enter your choice: ")
    if new_item == 'q':
        break
    elif new_item == '1':
        new_item = input("Enter new item: ")
        append_to_list(myList, new_item)
        print(myList)
    elif new_item == '2':
        new_item = input("Enter new item: ")
        index = int(input("Enter index: "))
        insert_in_list(myList, new_item, index)
        print(myList)
    elif new_item == '3':
        print(len_list(myList))
    elif new_item == '4':
        item = input("Enter item to remove: ")
        remove_from_list(myList, item)
        print(myList)
    elif new_item == '5':
        index = int(input("Enter index: "))
        del_from_list(myList, index)
        print(myList)
    else:
        print("Invalid option")
    
    
