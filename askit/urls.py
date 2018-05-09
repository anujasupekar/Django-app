from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'askit'

urlpatterns = [
	path('', views.question_list, name='list'),
	path('add', views.add_question_page, name='add_question'),
	path('add/new', views.add_new_question, name='save_question'),
	path('<int:question_id>/', views.question_detail, name='detail'),
	path('<int:question_id>/vote', views.vote, name='vote'),
	path('<int:question_id>/add_answer_page', views.add_answer_page, name='add_answer'),
	path('<int:question_id>/add_new_answer', views.add_new_answer, name='save_answer')
]

urlpatterns += staticfiles_urlpatterns()
