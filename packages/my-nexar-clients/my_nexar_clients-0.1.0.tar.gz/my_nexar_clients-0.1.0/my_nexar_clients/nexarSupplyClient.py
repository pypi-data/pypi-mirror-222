"""Resources for making Nexar requests."""
import requests
import base64
import json
import time
import os
from typing import Dict

NEXAR_URL = "https://api.nexar.com/graphql"
PROD_TOKEN_URL = "https://identity.nexar.com/connect/token"


def cache_token(token):
    with open("token.json", "w") as token_file:
        token_file.write(json.dumps(token, indent=4))


def get_token(client_id, client_secret):
    """Return the Nexar token from the client_id and client_secret provided."""

    if not client_id or not client_secret:
        raise Exception("client_id and/or client_secret are empty")

    token = {}
    try:
        token = requests.post(
            url=PROD_TOKEN_URL,
            data={
                "grant_type": "client_credentials",
                "client_id": client_id,
                "client_secret": client_secret,
            },
            allow_redirects=False,
        ).json()

    except Exception:
        raise

    cache_token(token)
    return token


def decodeJWT(token):
    return json.loads(
        (base64.urlsafe_b64decode(token.split(".")[1] + "==")).decode("utf-8")
    )


class NexarSupplyClient:
    def __init__(self, id, secret) -> None:
        self.id = id
        self.secret = secret
        self.s = requests.session()
        self.s.keep_alive = False

        if not os.path.exists("token.json"):
            self.token = get_token(id, secret)

        else:
            with open("token.json", "r") as token_file:
                self.token = json.load(token_file)

        self.token = get_token(id, secret)
        self.s.headers.update({"token": self.token.get('access_token')})
        self.exp = decodeJWT(self.token.get('access_token')).get('exp')

    def check_exp(self):
        if (self.exp < time.time() + 300):
            self.token = get_token(self.id, self.secret)
            self.s.headers.update({"token": self.token.get('access_token')})
            self.exp = decodeJWT(self.token.get('access_token')).get('exp')

    def get_query(self, query: str, variables: Dict) -> dict:
        """Return Nexar response for the query."""
        try:
            self.check_exp()
            r = self.s.post(
                NEXAR_URL,
                json={"query": query, "variables": variables},
            )

        except Exception as e:
            print(e)
            raise Exception("Error while getting Nexar response")

        response = r.json()
        if ("errors" in response):
            for error in response["errors"]:
                print(error["message"])
            raise SystemExit

        return response["data"]
