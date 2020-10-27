def location_Maharashtra(Data):
    print("")
    print("Employees whose location is Maharashtra")
    for user in Data['users']:
        for add in user['address']:
            if user['address']['state'] == "Maharashtra":
                print("Firstname:", user['firstName'], "Lastname:", user['lastName'],
                      "PostalCode:", user['address']['postalCode'])
                break
    print(" ")