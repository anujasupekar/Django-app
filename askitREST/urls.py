from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^questions/$', views.list_create_questions.as_view()),
	url(r'^questions/(?P<pk>[0-9]+)/$', views.retrieve_update_del_question.as_view()),
	url(r'^questions/(?P<question_id>[0-9]+)/answers/$', views.list_create_answers.as_view()),
	url(r'^questions/(?P<question_id>[0-9]+)/answers/(?P<pk>[0-9]+)/$', views.retrieve_update_del_answer.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)