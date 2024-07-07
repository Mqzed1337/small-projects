import string
from mojang import API
from time import sleep

api = API()


start_index = 600
usernames = []
available_usernames = []
characters = string.ascii_lowercase + string.digits + "_"
character_list = list(characters)
for i in character_list:
    for j in character_list:
        for k in character_list:
            usernames.append(i + j + k)
# uuid = api.get_uuids(
#    ["aqg", "aqh'", "aqi", "aqj", "aqk", "aql", "aqm", "aqn", "aqo", "aqp"]
# )
# print(uuid)
# print(len(uuid))

while start_index < len(usernames):
    try:
        check = api.get_uuids(usernames[start_index : start_index + 10])
        if len(check) != 10:
            for username in usernames[start_index : start_index + 10]:
                if username not in check.keys().lower():
                    available_usernames.append(username)
                    print(f"Available: {username}")
                    with open("available.txt", "a") as file:
                        file.write(username + "\n")
        start_index += 10
        print(start_index)
    except:
        print("Rate limited, waiting 10 seconds...")
        sleep(10)
