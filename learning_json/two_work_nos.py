def two_work_nos(Data):
    print("Employees with atleast 2  nos")
    for user in Data['users']:
        has_mobile_number = False
        has_work_number = False
        has_home_number=False
        type=""
        for phonenumber in user['phoneNumbers']:

            if phonenumber['type'] == 'work':
                has_work_number = True
                type=type+phonenumber['type']+","
            if phonenumber['type'] == 'mobile':
                has_mobile_number = True
                type = type + phonenumber['type']+","
            if phonenumber['type'] == 'home':
                has_home_number = True
                type = type + phonenumber['type']+","

        if has_work_number and has_mobile_number or has_mobile_number and has_home_number or has_home_number and has_work_number:
            print('Firstname', user['firstName'], 'Phone number', phonenumber['number'],"Type",type)

    print(" ")
