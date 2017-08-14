import praw
import os

go = "go"
reddit = praw.Reddit(client_id="SsZW8NMLOD5qvg", client_secret="Pm4_MfJ_DMugRRDiEryG48CJbak", user_agent="Beckit: Beck's personal Reddit client")

learnpython = "learnpython"


#subreddit_name = input("Which subreddit would you like to go to?")

#subreddit_limit = input("How many links do you want to display?")

subreddit_name = "askreddit"

subreddit_limit = 10

subreddit = reddit.subreddit(subreddit_name)

subreddit_top_10_posts = subreddit.hot(limit=subreddit_limit)

submissions = []

for submission in subreddit_top_10_posts:
    submissions.append(submission)

while True:
    for index, submission in enumerate(submissions):
        print(str(index) + " ------- " + str(submission.title))

    comments = submissions[1].comments

    print("The length of the comments list is:" + str(len(comments)) + "\n\n")
    
    y = "y"
    index = 0
    while index < len(comments) - 2:
        for comment in comments[index:index + 2]:
            print(comment.body)
            print("\nEND_COMMENT\n")

        i = input("Next page?")
        if i == y:
            index = index + 2
            os.system("clear")
    
    

    
 






