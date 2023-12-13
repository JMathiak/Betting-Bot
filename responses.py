import random
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
def handle_response(message) -> str:
    p_message = message.lower();

    if p_message == 'hello':
        return 'HI'
    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message == 'help':
        return "`This is a help message that you can modify`"

    if p_message[0:8] == '!mastery':
        riot_token = os.getenv('RIOT_TOKEN')
        user_message = p_message[9:]
        user = user_message.split('#')
        url_parts = [user[0], user[1], "?api_key=", riot_token]

        # uid_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id".format("/".join(url_parts))
        uid_url = ""
        print(uid_url)
        response = requests.get(uid_url).json()
        return str(response)


def get_mastery(message, riot_token) -> str:
    user = message.split('#')
    url_parts=[user[0], user[1], "?api_key=", riot_token]

    uid_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id".format("/".join(url_parts))
    response = requests.get(uid_url)

    #wait for uid
    #get uid and put it into vvv url

    mastery_url = ""
    master_url = mastery_url.format(riot_token)

    return str(response)
