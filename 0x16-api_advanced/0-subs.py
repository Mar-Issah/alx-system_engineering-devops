#!/usr/bin/python3
"""that queries the Reddit API and returns the num of subscribers """
import requests


URL = 'https://www.reddit.com/r/{}/about.json'


def number_of_subscribers(subreddit):
    """Get num of subscribers"""
    header = {'user-agent': 'marsiya-app'}
    req = requests.get(URL.format(subreddit), headers=header)

    if req.status_code != 200:
        return 0
    return req.json().get("data", {}).get("subscribers", 0)
