from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm


def question_list(request):
	question_list = Question.objects.all().order_by('-post_date')
	return render(request, 'askit/index.html', {'question_list':question_list})

def question_detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'askit/detail.html', {'question':question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	votes = request.POST.get("votes")
	if votes:
		if votes == 'upvote':
			question.upvotes += 1
		elif votes == 'downvote':
			question.downvotes += 1
	question.save()
	return HttpResponse(request)

def add_question_page(request):
	return render(request, 'askit/add_question.html')

def add_new_question(request):
	title = request.POST.get("question")
	writer = request.POST.get("writer")
	question = Question.objects.create(title=title,
									posted_by = writer,
									post_date = timezone.now()
									)
	question.save()
	return HttpResponseRedirect(reverse('askit:list'))

def add_answer_page(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'askit/answer_detail.html', {'question':question})

def add_new_answer(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	new_answer = request.POST.get("answer")
	writer = request.POST.get("writer")
	if new_answer:
		new_answer = Answer(answer=new_answer, written_by=writer, post_date=timezone.now(), question=question)
		new_answer.save()
	question.save()
	return HttpResponseRedirect(reverse('askit:detail', args=(question.id,)))