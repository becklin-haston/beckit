import praw
import os

reddit = praw.Reddit(client_id="SsZW8NMLOD5qvg", client_secret="Pm4_MfJ_DMugRRDiEryG48CJbak", user_agent="Beckit: Beck's personal Reddit client")



g = "go"

i = str(input("Input:"))



while i == "go":

    for submission in reddit.subreddit('learnpython').hot(limit=10):
        print(submission.title)

    i = str(input("Next?"))

    if i == "go":
        os.system("clear")








