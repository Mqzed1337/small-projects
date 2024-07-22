user = input("Enter your email: ")
password = input("Enter your password: ")
from mojang import Client

client = Client(user, password, retry_on_ratelimit=True, ratelimit_sleep_time=60)
print("Bearer Token:")
print(client.bearer_token)
with open("token.env", "w") as file:
    file.write(str(client.bearer_token))
print("Bearer token written to token.env")
