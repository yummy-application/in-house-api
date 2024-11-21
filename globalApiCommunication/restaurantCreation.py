import json
import requests

with open(r"globalApiCommunication\config.json", "r") as f:
    global_api_adress = json.load(f)["address"]


def create_restaurant(name, image,password,backend_address):
    requests.post(global_api_adress + "/restaurant/create", headers={"name": name, "image": image, "password": password, "backendAddress":backend_address})
