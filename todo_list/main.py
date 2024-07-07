import json

with open("list.json", "r", encoding="uft-8") as file:
    todo_list = file.read()


def update_json(updated_list):
    with open("list.json", "w", encoding="uft-8") as file:
        file.write(updated_list)
    pass


todo_list = ["a"]
update_json(todo_list)
