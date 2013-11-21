from django.db import models


class Question(models.Model):
    """
    Basic text-based question model
    """

    # TODO we will eventually want richer question formats
    text = models.TextField(verbose_name="question text")
    title = models.CharField(max_length=1000, verbose_name="question title")

    def __unicode__(self):
        return self.text + ": " + self.solution


class Answer(models.Model):
    """
    Basic text-based answer option for multiple choice questions
    """    
    question = models.ForeignKey(Question)
    text = models.TextField(max_length=1000, verbose_name="displayed answer")
    explanation = models.TextField(verbose_name="Explanation")
    is_correct = models.BooleanField(default=False)

    def __unicode__(self):
        ret_txt = ""
        if self.correct:
            ret_txt += "[correct]   :"
        else:
            ret_txt += "[incorrect] :"
        return ret_txt + self.text + "(explanation: " + self.explanation + ")\n For question: " + question.text + "\n"
    
