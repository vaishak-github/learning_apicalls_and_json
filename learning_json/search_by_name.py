def search_by_name(data):
    name = input(str("Enter a name"))
    for user in data['users']:
        if user['firstName'].lower().startswith(name.lower()):
            print("Firstname", user['firstName'], "Lastname:", user['lastName'], "Age:", user['age'],
                  "Gender:", user['gender']
                  , "\nAddress: State", user['address'], "Phonenumbers:\n", user['phoneNumbers'])
            print("****************************************************************************")