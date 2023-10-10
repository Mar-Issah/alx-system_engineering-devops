#!/usr/bin/python3
"""queries Reddit API, returns the titles of first 10 hot posts listed  """
import requests

URL = 'https://www.reddit.com/r/{}/hot.json'


def top_ten(subreddit):
    """Get top_ten hot post listed"""
    header = {'user-agent': 'marsiya-app1'}

    req = requests.get(URL.format(subreddit), headers=header)
    if req.status_code != 200:
        print("None")
        return
    children = req.json().get('data', {}).get('children', [])
    if not children:
        print("None")
        return
    for item in children[0:10]:
        print(item.get('data', {}).get('title', ''))
