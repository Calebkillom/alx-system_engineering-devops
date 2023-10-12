#!usr/bin/python3
""" function that queries the Reddit API and returns a list """
import requests


def recurse(subreddit, hot_list=None, after=None):
    """ function that queries the Reddit API and returns a list """
    if hot_list is None:
        hot_list = []

    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "UniqueRedditScraper/1.0"
    headers = {'User-Agent': user_agent}
    params = {'limit': 100, 'after': after}

    response = requests.get(base_url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        articles = data.get('children', [])

        for article in articles:
            hot_list.append(article['data']['title'])

        after = data.get('after')

        if not articles:
            if not hot_list:
                return None
            else:
                return hot_list

        return recurse(subreddit, hot_list, after)
    elif response.status_code == 404:
        return None
    else:
        return None
