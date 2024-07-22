import string
import datetime
from mojang import API
from mojang import Client
from time import sleep
from datetime import date

api = API()


start_index = 50660
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
                if username not in {k.lower(): check[k] for k in check.keys()}:
                    available_usernames.append(username)
                    print(f"Available: {username}")
                    with open("available.txt", "a") as file:
                        file.write(username + "\n")
        start_index += 10
        print(start_index)
        sleep(5)
    except Exception as e:
        print(e)
        print("Rate limited, waiting 10 seconds..." + str(start_index))
        sleep(10)

# Code to print the contents of available.txt
with open("available.txt", "r", encoding="utf-8") as file:
    available_list = file.read().splitlines()
    print(len(available_list) + " names which are not currently taken")
with open("token.env", "r", encoding="utf-8") as file:
    user_token = file.read().strip()
client = Client(
    bearer_token=user_token,
    retry_on_ratelimit=True,
    ratelimit_sleep_time=60,
)
print("got api access")
check = available_list
final = []
for i in check:
    if client.is_username_available(i):
        print(f'"{i}" is available')
        final.append(i)
    else:
        print(f'"{i}" is not available')
print("avaiable three letter names are: \n")
for i in final:
    print(i)
