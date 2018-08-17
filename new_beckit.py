import os
import time
import praw

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
    os.system("cls")

def truncate(text, limit):
    if len(text) >= limit:
        return text[0:limit - 1] + "..."
    else:
        return text

def truncate_comment_body(body):
    return truncate(body, 200)

def truncate_submission_title(title):
    return truncate(title, 200)

def show_submissions(submissions):
    print("Subreddit: " + subreddit_name)
    for index, submission in enumerate(submissions):
        print(f"{str(index)} ------- {str(truncate_submission_title(submission.title))}")


def parse_command(user_command):

    split_command = user_command.split(",")

    for command in split_command:
        # s:stevenuniverse 25
        command = command.split(":")
        operator = command[0]
        operands = command[1]
        operands_list = operands.split(" ")


def get_input():
    command = input(">>>")
    return command

def execute_command(command):
    pass

reddit = praw.Reddit(client_id="SsZW8NMLOD5qvg", client_secret="Pm4_MfJ_DMugRRDiEryG48CJbak", user_agent="Beckit: Beck's personal Reddit client")

clear_screen()

show_splash_screen()

take_input = True
while take_input:

    user_commmand = get_input()

    parsed_command = parse_command(user_command)

    command_result = execute_command(parsed_command)
