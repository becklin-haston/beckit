import SubmissionDisplay

class dummySubmission:
    
    def __init__(self):
        self.title = "This is the title of the post"


dummy = dummySubmission()

sd = SubmissionDisplay.SubmissionDisplay(dummy)

sd.showSubmissionDisplay()
