import requests


GITHUB_TOKEN = "ghp_pDaZCGLK6aFf5PuHMJEKPwuPeRcB1roiSkLH"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

response = requests.get("https://api.github.com/user", headers=headers)

if response.status_code == 200:
    print("Authenticated as:", response.json().get("login"))
else:
    print("Request failed:", response.status_code, response.text)
