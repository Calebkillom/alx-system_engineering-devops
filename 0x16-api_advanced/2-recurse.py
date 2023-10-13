#!/usr/bin/python3
""" function that queries the Reddit API and returns a list of titles. """
import requests


def recurse(subreddit, after=None, hot_list=None):
    """
    Recursively fetches hot article titles from Reddit.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Unique User Agent 2.0'}

    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        hot_list += [child['data']['title'] for child in children]

        after = data.get('after')
        if after:
            # Recursively fetch the next page
            hot_list = recurse(subreddit, after, hot_list)

        return hot_list

    elif response.status_code == 404:
        return None
    else:
        return None
