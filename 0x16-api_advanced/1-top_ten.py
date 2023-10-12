#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """ queries the Reddit API and prints the titles of the first 10 """
    if not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            if not posts:
                print(None)
            for post in posts:
                print(post['data']['title'])

        else:
            print("none")

    except Exception as e:
        print("An error occurred:", str(e))
