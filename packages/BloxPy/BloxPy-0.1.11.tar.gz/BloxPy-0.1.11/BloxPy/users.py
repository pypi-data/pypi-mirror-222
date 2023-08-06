import requests

def get_user(user_id: int):
    response = requests.get(f'https://users.roblox.com/v1/users/{user_id}')

    if response.status_code == 200:
        return response.json()

    elif response.status_code == 404:
        return print("The user id is invalid.")

    else:
        return "An unexpected error occured"