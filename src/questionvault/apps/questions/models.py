from django.db import models


class Question(models.Model):
    """
    Basic text-based question model
    """

    # TODO we will eventually want richer question formats
    text = models.TextField()
    solution = models.TextField()

    def __unicode__(self):
        return self.text + ": " + self.solution

class Answer(models.Model):
    """
    Basic text-based answer option for multiple choice questions
    """    
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=1000)
    explanation = models.TextField()
    is_correct = models.BooleanField(default=False)


    def __unicode__(self):
        ret_txt = ""
        if self.correct:
            ret_txt += "[correct]   :"
        else:
            ret_txt += "[incorrect] :"
        return ret_txt + self.text + "(explanation: " + self.explanation + ")\n For question: " + question.text + "\n"
    
