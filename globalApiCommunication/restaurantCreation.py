import json
import requests

with open(r"globalApiCommunication\config.json", "r") as f:
    backend_address_api = json.load(f)["address"]


def create_restaurant(name, image,password,backend_address):
    requests.post(backend_address_api + "/restaurant/create", headers={"name": name, "image": image, "password": password,"backendAddress":backend_address})
