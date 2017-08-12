import praw
import os

go = "go"
reddit = praw.Reddit(client_id="SsZW8NMLOD5qvg", client_secret="Pm4_MfJ_DMugRRDiEryG48CJbak", user_agent="Beckit: Beck's personal Reddit client")

learnpython = "learnpython"


subreddit_name = input("Which subreddit would you like to go to?")

subreddit_limit = input("How many links do you want to display?")

subreddit = reddit.subreddit(subreddit_name)

subreddit_top_10_posts = subreddit.hot(limit=subreddit_limit)

submissions = []

for submission in subreddit_top_10_posts:
    submissions.append(submission)



g = "go"

i = str(input("Input:"))

while i == "go":
    for index, submission in enumerate(submissions):
        print(str(index) + " ------- " + str(submission.title))

    i = input("Which submission would you like to read?")
    for comment in submissions[i].comments:
        print(comment.body)
        print("\n\nEND_COMMENT\n\n")

    i = input("go?")
    os.system("clear") 






