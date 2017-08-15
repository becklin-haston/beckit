import praw
import os
import time
askreddit = "askreddit"
def show_splash_screen():
    splash_screen = '''                              
______________________________  ____  __.______________
\______   \_   _____/\_   ___ \|    |/ _|   \__    ___/
 |    |  _/|    __)_ /    \  \/|      < |   | |    |   
 |    |   \|        \\     \___|    |  \|   | |    |   
 |______  /_______  / \______  /____|__ \___| |____|   
        \/        \/         \/        \/                                        
'''
    print(splash_screen)
    time.sleep(1)            

def clear_screen():
    os.system("clear")

def truncate(text, limit):
    if len(text) >= limit:
        return text[0:limit - 1] + "..."
    else:
        return text

def truncate_comment_body(body):
    return truncate(body, 200)

def truncate_submission_title(title):
    return truncate(title, 200)

reddit = praw.Reddit(client_id="SsZW8NMLOD5qvg", client_secret="Pm4_MfJ_DMugRRDiEryG48CJbak", user_agent="Beckit: Beck's personal Reddit client")

clear_screen()

show_splash_screen()


while True:

    clear_screen()
    
    subreddit_name = input("Which subreddit would you like to go to?")

    subreddit_limit = int(input("How many of the top links do you want to see?"))

    subreddit = reddit.subreddit(subreddit_name)

    subreddit_top_posts = subreddit.hot(limit=subreddit_limit)

    submissions = []

    for submission in subreddit_top_posts:
        submissions.append(submission)

    clear_screen()

    print("Subreddit: " + subreddit_name)

    for index, submission in enumerate(submissions):
        print(str(index) + " ------- " + str(truncate_submission_title(submission.title)))

    i = int(input("Which thread would you like to see?"))
   
    clear_screen()
 
    print("\nTopic: " + submissions[i].title + "\n\n") 
    
    comments = submissions[i].comments
    
    clear_screen()

    print("There are " + str(len(comments)) + " comments in this thread.\n\n")
    
    index = 0
    
    while index < len(comments) - 2:
        
        print("Subreddit: " + subreddit_name)
        
        print("\nTopic: " + submissions[i].title + "\n\n")
        
        for comment in comments[index:index + 2]:

            print("Comment by " + comment.author.name + ":\n")            

            print(truncate_comment_body(comment.body))
            
            print("\nEND_COMMENT\n")

        n = "n"
        p = "p"
        r = "r"
        user_input = input(">>")
        
        if user_input == n:    
            index = index + 2
        elif user_input == p:
            index = index - 2
        else:
            break
        
        os.system("clear")
    
    

    
 






