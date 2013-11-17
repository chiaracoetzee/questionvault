from django.conf.urls import patterns, url

from views import edit_question

urlpatterns = patterns('edit',
                       url('', edit_question, name="edit")
                )
