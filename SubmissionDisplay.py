class SubmissionDisplay:

    def __init__(self, submission):
        self.submission = submission
    
    def showSubmissionDisplay(self):
        print("+-------------------------------------------------------------------+")
        print("+" + self.submission.title[:10] + "---------------------------------------------------------+")
        print("+-------------------------------------------------------------------+")




