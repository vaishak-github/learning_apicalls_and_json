def two_work_nos(Data):
    print("Employees with 2 work nos")
    for user in Data['users']:
        has_mobile_number = False
        has_work_number = False

        for phonenumber in user['phoneNumbers']:

            if phonenumber['type'] == 'work':
                has_work_number = True
            if phonenumber['type'] == 'mobile':
                has_mobile_number = True

        if has_work_number and has_mobile_number:
            print('Firstname', user['firstName'], 'Phone number', phonenumber['number'])

    print(" ")
