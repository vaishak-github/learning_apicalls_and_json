def phone_nos(Data):
    '''print("Emp with worknos")
    for user in Data['users']:
        has_mobile_number = False
        has_work_number = False
        has_home_number = False
        for pno in user['phoneNumbers']:
            if (pno['type'] == "work"):
                has_work_number = True

            elif pno['type'] == "mobile":
                has_mobile_number = True
            else:
                has_home_number = True
        if has_work_number:
            print("Name", user['firstName'], "work number", pno['number'])
        elif not has_work_number and has_mobile_number:
            print("Name", user['firstName'], "mobile number", pno['number'])
        elif not has_mobile_number  and has_home_number:
            print("Name", user['firstName'], "home number", pno['number'])'''
    print("Employees with work nos:")
    for user in Data['users']:
        has_mobile_number = False
        has_work_number = False
        has_home_number = False

        for pno in user['phoneNumbers']:
            if pno['type']=="work":
                has_work_number = True
        if has_work_number:
            print("Name", user['firstName'], "work number", pno['number'])
    print("")
    print("Employees with no work no but have mobile no:")
    for user in Data['users']:
        has_mobile_number = False
        has_work_number = False
        has_home_number = False


        for pno in user['phoneNumbers']:
            if pno['type'] == "work":
                has_work_number = True
            elif pno['type'] == "mobile":
                has_mobile_number=True
        if has_mobile_number and not has_work_number:
            print("Name", user['firstName'], "mobile number", pno['number'])
    print("")
    print("Employess with no mobileno and work no:")
    for user in Data['users']:
        has_mobile_number = False
        has_work_number = False
        has_home_number = False

        for pno in user['phoneNumbers']:
            if pno['type'] == "work":
                has_work_number = True
            elif pno['type'] == "mobile":
                has_mobile_number=True
            else:
                has_home_number = True

        if has_home_number and not has_mobile_number and not has_work_number:
            print("Name", user['firstName'], "home number", pno['number'])
