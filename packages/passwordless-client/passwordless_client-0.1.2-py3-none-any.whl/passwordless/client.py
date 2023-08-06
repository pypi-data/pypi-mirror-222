import requests
from requests.exceptions import RequestException

class PasswordlessClient:
    def __init__(self, api_secret):
        self.api_secret = api_secret
        self.headers = {
            "ApiSecret": api_secret,
            "Content-Type": "application/json"
        }

    def register_token(self, user_id, username, displayname, **kwargs):
        url = "https://v4.passwordless.dev/register/token"
        data = {
            "userId": user_id,
            "username": username,
            "displayname": displayname,
            **kwargs
        }
        try:
            response = requests.post(url, json=data, headers=self.headers)
            return self._handle_response(response)
        except RequestException as e:
            return f"An error occurred while registering the token: {str(e)}"

    def signin_verify(self, token):
        url = "https://v4.passwordless.dev/signin/verify"
        data = {"token": token}
        try:
            response = requests.post(url, json=data, headers=self.headers)
            return self._handle_response(response)
        except RequestException as e:
            return f"An error occurred while verifying the sign-in: {str(e)}"

    def alias(self, user_id, aliases, hashing=True):
        url = "https://v4.passwordless.dev/alias"
        data = {"userId": user_id, "aliases": aliases, "hashing": hashing}
        try:
            response = requests.post(url, json=data, headers=self.headers)
            return self._handle_response(response)
        except RequestException as e:
            return f"An error occurred while adding aliases: {str(e)}"

    def credentials_list(self, user_id):
        url = f"https://v4.passwordless.dev/credentials/list?userId={user_id}"
        try:
            response = requests.get(url, headers=self.headers)
            return self._handle_response(response)
        except RequestException as e:
            return f"An error occurred while listing credentials: {str(e)}"

    def credentials_delete(self, credential_id):
        url = "https://v4.passwordless.dev/credentials/delete"
        data = {"credentialId": credential_id}
        try:
            response = requests.post(url, json=data, headers=self.headers)
            return self._handle_response(response)
        except RequestException as e:
            return f"An error occurred while deleting the credential: {str(e)}"

    def _handle_response(self, response):
        try:
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 201:
                return "Everything is OK but empty."
            elif response.status_code == 400:
                return "Bad request. Please check your parameters."
            elif response.status_code == 401:
                return "You did not identify yourself. Please check your API secret."
            elif response.status_code == 409:
                return "Conflict (alias is already in use)."
            elif response.status_code == 500:
                return "Something went very wrong on the server side."
            else:
                response.raise_for_status()
        except RequestException as e:
            return f"An error occurred while processing the request: {str(e)}"