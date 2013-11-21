from django.conf.urls import patterns, url

from views import edit_question

urlpatterns = patterns('',
                       url('new', edit_question, name="new")
                )
