import requests

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
        response = requests.post(url, json=data, headers=self.headers)
        return self._handle_response(response)

    def signin_verify(self, token):
        url = "https://v4.passwordless.dev/signin/verify"
        data = {"token": token}
        response = requests.post(url, json=data, headers=self.headers)
        return self._handle_response(response)

    def alias(self, user_id, aliases, hashing=True):
        url = "https://v4.passwordless.dev/alias"
        data = {"userId": user_id, "aliases": aliases, "hashing": hashing}
        response = requests.post(url, json=data, headers=self.headers)
        return self._handle_response(response)

    def credentials_list(self, user_id):
        url = f"https://v4.passwordless.dev/credentials/list?userId={user_id}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def credentials_delete(self, credential_id):
        url = "https://v4.passwordless.dev/credentials/delete"
        data = {"credentialId": credential_id}
        response = requests.post(url, json=data, headers=self.headers)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code in [200, 201]:
            return response.json()
        else:
            response.raise_for_status()