import requests
from pprint import pprint
subscription_key = ""
assert subscription_key
text_analytics_base_url = "https://canadacentral.api.cognitive.microsoft.com/text/analytics/v2.0/"
language_api_url = text_analytics_base_url + "sentiment"
print(language_api_url)


# check sentiment
def checkSentiment(title, selfText):
    documents = { 'documents': [
    { 'id': '1', 'text': title },
    { 'id': '2', 'text': selfText }
    ]}
    headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
    response  = requests.post(language_api_url, headers=headers, json=documents)
    languages = response.json()
    pprint(languages)
    return


# reddit bot praw magic
import praw
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("learnpython")
for submission in subreddit.hot(limit=5):
#    print("Title: ", submission.title)
#    print("Text: ", submission.selftext)
#    print("Score: ", submission.score)
#    print("---------------------------------\n")
    checkSentiment(submission.title, submission.selftext)

