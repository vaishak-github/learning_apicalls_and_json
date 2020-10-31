'''def details(data):
    print(" the firstname of employees with state Maharashtra and postal code:421202")
    for user in data['users']:
        for add in user['address'].values():

             if user['address']['state'] == "Maharashtra" and user['address']['postalCode']== '421202':
                print("FirstName", user['firstName'])
             break
             '''


def details(data):
    print(" the firstname of employees with state Maharashtra and postal code:421202")
    for user in data['users']:
        add_details = user['address']
        for det in add_details:
            if user['address']['state'] == "Maharashtra" and user['address']['postalCode'] == '421202':
                print("FirstName", user['firstName'])
            break
