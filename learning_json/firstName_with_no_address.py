def firstName_with_no_address(data):
    print(" ")
    print("Employees with no address")
    for user in data['users']:
        if not user['address']:
            print("Firstname:", user['firstName'])