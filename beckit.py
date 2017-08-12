import praw
import os

reddit = praw.Reddit(client_id="SsZW8NMLOD5qvg", client_secret="Pm4_MfJ_DMugRRDiEryG48CJbak", user_agent="Beckit: Beck's personal Reddit client")

learnpython = "learnpython"


subreddit_name = input("Which subreddit would you like to go to?")

subreddit_limit = input("How many links do you want to display?")

subreddit = reddit.subreddit(subreddit_name)

subreddit_top_10_posts = subreddit.hot(limit=subreddit_limit)

for submission in subreddit_top_10_posts:
    print(submission.title)





'''
g = "go"

i = str(input("Input:"))

while i == "go":

    for submission in reddit.subreddit('learnpython').hot(limit=10):
        print(submission.title)

    i = str(input("Next?"))

    if i == "go":
        os.system("clear")
'''







