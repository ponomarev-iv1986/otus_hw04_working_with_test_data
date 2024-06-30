import csv
import json
import os

BASE_DIR = os.path.dirname(__file__)
FILE_WITH_USERS = os.path.join(BASE_DIR, "users.json")
FILE_WITH_BOOKS = os.path.join(BASE_DIR, "books.csv")


def get_users_list(file):
    users = []
    with open(file, newline="") as f:
        user_list_full = json.loads(f.read())
    for user in user_list_full:
        new_user = dict(
            name=user["name"],
            gender=user["gender"],
            address=user["address"],
            age=user["age"],
            books=[],
        )
        users.append(new_user)
    return users


def get_books_list(file):
    books = []
    with open(file, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            book = dict(
                title=row["Title"],
                author=row["Author"],
                pages=row["Pages"],
                genre=row["Genre"],
            )
            books.append(book)
    return books


def distribute_books(users, books):
    counter = 0
    while True:
        if books:
            book = books.pop()
            users[counter]["books"].append(book)
            if counter < len(users) - 1:
                counter += 1
            else:
                counter = 0
        else:
            break
    return users


if __name__ == "__main__":
    users_list = get_users_list(FILE_WITH_USERS)
    books_list = get_books_list(FILE_WITH_BOOKS)
    books_list = books_list[::-1]
    result = distribute_books(users_list, books_list)
    with open("result.json", "w") as file:
        file.write(json.dumps(result, indent=4))
