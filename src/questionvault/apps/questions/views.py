import pdb

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django import forms

from models import Question, Answer
from forms import QuestionForm, AnswerFormSet

# view handling groked from http://stackoverflow.com/questions/18755909/django-multiple-modelforms-with-the-same-model-and-foreignkeys
def edit_question(request):
    AnswerFormset = forms.models.inlineformset_factory(
         Question, Answer, formset=AnswerFormSet, extra=4, max_num=4)
#    question = Question()
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        answer_formset = AnswerFormset(request.POST)
        
        # Check these separately to avoid short-circuiting
        question_valid = question_form.is_valid()
        answer_valid = answer_formset.is_valid()
        
        if question_valid and answer_valid:
            question_form.save()
            # No need to add new question as it was already set as the instance above
            answer_formset.save()
            return HttpResponse(status=200) # TODO redirect to something worthwhile

    elif request.method == 'GET':
        answer_formset = AnswerFormset()
        question_form = QuestionForm()
    elif request.method:
        return HttpResponse(status=405)

    return render_to_response("question_edit.html", {"formset": answer_formset, "question_form": question_form}, context_instance=RequestContext(request))



