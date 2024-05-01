import requests # type: ignore

class FacebookClient:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_user_info(self):
        url = f"https://graph.facebook.com/me?access_token={self.access_token}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def post_status(self, message):
        url = f"https://graph.facebook.com/me/feed?access_token={self.access_token}"
        data = {"message": message}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return True
        else:
            return False