import praw
import os

def truncate_comment_body(body):
    if len(body) >= 80:
        return body[0:79] + "..."
    else:
        return body

def truncate_submission_title(title):
    if len(title) >= 80:
        return title[0:79] + "..."
    else:
        return title


reddit = praw.Reddit(client_id="SsZW8NMLOD5qvg", client_secret="Pm4_MfJ_DMugRRDiEryG48CJbak", user_agent="Beckit: Beck's personal Reddit client")

subreddit_name = input("Which subreddit would you like to go to?")

subreddit_limit = 10

subreddit = reddit.subreddit(subreddit_name)

subreddit_top_10_posts = subreddit.hot(limit=subreddit_limit)

submissions = []

for submission in subreddit_top_10_posts:
    submissions.append(submission)

os.system("clear")
while True:
    for index, submission in enumerate(submissions):
        print(str(index) + " ------- " + str(truncate_submission_title(submission.title)))

    i = int(input("Which thread would you like to see?"))
    print("Topic: " + submissions[i].title + "\n\n")
    if submissions[i].selftext_html:
        print(submissions[i].selftext.html) 
    comments = submissions[i].comments
    print("There are " + str(len(comments)) + " comments in this thread.\n\n")
    
    y = "y"
    index = 0
    while index < len(comments) - 2:
        print("Topic: " + submissions[i].title + "\n\n")
        for comment in comments[index:index + 2]:
            #print(type(comment))
            #print(comment.__dict__)
            print("Comment by " + comment.author.name + ":\n")            
            print(truncate_comment_body(comment.body))
            print("\nEND_COMMENT\n")

        n = "n"
        p = "p"

        user_input = input(">>")
        
        if user_input == n:
            index = index + 2
        elif user_input == p:
            index = index - 2
        
        os.system("clear")
    
    

    
 






