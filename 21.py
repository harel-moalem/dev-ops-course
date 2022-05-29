import requests

response = requests.get("https://api.github.com/users/avielb/repos")
repo_list = response.json()

for repo in repo_list:
    print(repo["name"])