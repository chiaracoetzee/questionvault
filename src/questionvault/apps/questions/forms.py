import pdb

from django import forms

from models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'solution']

class AnswerFormSet(forms.models.BaseInlineFormSet):
    def clean(self):
        correct_count = sum([form.cleaned_data.has_key('is_correct') and form.cleaned_data['is_correct'] for form in self.forms])
        if correct_count != 1:
            raise forms.ValidationError('Exactly one answer must be marked as correct')
