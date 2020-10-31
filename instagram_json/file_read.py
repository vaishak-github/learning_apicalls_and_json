import json
def home():
    f=open("H:/insta_data/_vaishak07_20201023_part_1/likes.json")
    data=json.load(f)

    for like in data['media_likes']:

        if like[0]=="2020-10-21T21:33:23+00:00":
            print(like)


home()