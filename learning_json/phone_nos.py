def phone_nos(Data):
    print("Emp with worknos")
    for x, y in Data.items():

        for i in range(0, len(y)):
            flag_work = False
            for b in y[i]['phoneNumbers']:
                if b['type'] == "work":
                    flag_work = True
            if flag_work:
                print("emp_name", y[i]['firstName'], "work no", b['number'])

    print("")
    print("Emp with mobile nos")

    for x, y in Data.items():

        for i in range(0, len(y)):
            flag_mobile = False
            for b in y[i]['phoneNumbers']:
                if b['type'] == "mobile":
                    flag_mobile = True
            if flag_mobile:
                print("emp_name", y[i]['firstName'], "mobile no", b['number'])

    print("")

    print("Emp with home nos")
    for x, y in Data.items():
        for i in range(0, len(y)):
            flag_home = False
            for b in y[i]['phoneNumbers']:
                if b['type'] == "home":
                    flag_home = True
            if flag_home:
                print("emp_name", y[i]['firstName'], "mobile no", b['number'])

    print("")