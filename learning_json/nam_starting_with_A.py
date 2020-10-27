def name_starting_with_A(Data):
    test = 'A'
    print("Employees whose name start with A")
    for i in Data['users']:
        for add in i['address']:
            if i['firstName'].startswith(test):
                print("Firstname", i['firstName'], "State", i['address']['state'])
            break
    print(" ")
