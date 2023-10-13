#!/usr/bin/python3
"""  recursive function that queries the Reddit API and returns a list """
import requests


def recurse(subreddit, after=None):
    """
    function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
    """
    if after is None:
        after_param = ""
    else:
        after_param = "?after=" + after

    url = "https://www.reddit.com/r/{}/hot.json{}"\
        .format(subreddit, after_param)
    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        hot_list = [child['data']['title'] for child in children]

        after = data.get('after')
        if after:
            hot_list += recurse(subreddit, after)

        return hot_list

    elif response.status_code == 404:
        return None
    else:
        return None
