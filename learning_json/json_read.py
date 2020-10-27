import json
import phone_nos as pn
import location_Maharashtra as lm
import nam_starting_with_A as ns
import two_work_nos as tw
import firstName_with_no_address as noadd
import search_by_name as s
import details as d


def home():
    f = open("C:/Users/Vaishak/learning_apicalls_and_json/output.json", )
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    pn.phone_nos(data)
    lm.location_Maharashtra(data)
    ns.name_starting_with_A(data)
    tw.two_work_nos(data)
    d.details(data)
    noadd.firstName_with_no_address(data)
    s.search_by_name(data)
home()
