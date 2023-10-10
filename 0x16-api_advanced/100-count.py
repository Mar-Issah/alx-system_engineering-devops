#!/usr/bin/python3
''' list containing the titles of all hot articles '''
import pprint
import re
import requests

url = 'http://reddit.com/r/{}/hot.json'


def count_words(subreddit, word_list, hot_list=[], next_page=None):
    ''' Get hot posts '''
    header = {'User-agent': 'marsiya-app3'}
    params = {'limit': 100}
    if isinstance(next_page, str):
        if next_page != "DONE":
            params['after'] = next_page
        else:
            return _print(word_list, hot_list)

    response = requests.get(url.format(subreddit),
                            headers=header, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    next_page = data.get('after', 'DONE')
    if not next_page:
        next_page = "DONE"
    hot_list = hot_list + [item.get('data', {}).get('title')
                           for item in data.get('children', [])]
    return count_words(subreddit, word_list, hot_list, next_page)


def _print(word_list, hot_list):
    ''' print '''
    count = {}
    for word in word_list:
        count[word] = 0
    for title in hot_list:
        for word in word_list:
            count[word] = count[word] +\
             len(re.findall(r'(?:^| ){}(?:$| )'.format(word), title, re.I))

    count = {k: v for k, v in count.items() if v > 0}
    words = sorted(list(count.keys()))
    for word in sorted(words,
                       reverse=True, key=lambda k: count[k]):
        print("{}: {}".format(word, count[word]))
