import requests
from globalApiCommunication.restaurantCreation import global_api_adress


def validate_jwt(jwt):
    """
    Checks if jwt is valid
    :param jwt:
    :return:
    """
    response = requests.post(f"{global_api_adress}/acc/login/check", data={"jwt":jwt})
    return response.status_code in [200,499]
