dict= {"users":[
        { "address": {
            "streetAddress": "126",
            "city": "San Jone",
            "state": "CA",
            "postalCode": "394221"
         },
         "phoneNumbers": [
            {
               "type": "home",
               "number": "7383627627"
            },
{
               "type": "home",
               "number": "7383627627"
            }

                 ]}]}

for user in dict['users']:
    for pn in user['phoneNumbers']:#pn is dictionary itself
      print(pn['type']) #so we can access it using variable

for user in dict['users']:
    for add in user['address']:#add is key
      #print(add['state']) #so u cant use a key to access a key
      print(user['address']['state'])
      break