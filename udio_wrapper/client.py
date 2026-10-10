import requests

class UdioWrapper:
    def __init__(self, auth_token=None):
        self.auth_token = auth_token
        self.base_url = "https://www.udio.com/api"
        self.headers = {
            "Authorization": f"Bearer {self.auth_token}" if self.auth_token else "",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }

    def generate(self, prompt, **kwargs):
        url = f"{self.base_url}/generate"
        payload = {"prompt": prompt, **kwargs}
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            if response.status_code == 500:
                # Handle hCaptcha or backend 500 error gracefully
                raise Exception("500 Server Error: Possible hCaptcha challenge triggered or upstream backend failure.")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(f"API Request Failed: {e}")
