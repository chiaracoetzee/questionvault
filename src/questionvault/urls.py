from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_template.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
            url(r'^$', TemplateView.as_view(template_name="landing.html")),
            url(r'^q/', include('questionvault.apps.questions.urls', namespace='questions')),
            url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
