from django.shortcuts import render
from askit.models import Question, Answer
from rest_framework import generics
from . import serializers

# Create your views here.

class list_create_questions(generics.ListCreateAPIView):
	queryset = Question.objects.all()
	serializer_class = serializers.QuestionSerializer


class retrieve_update_del_question(generics.RetrieveUpdateDestroyAPIView):
	queryset = Question.objects.all()
	serializer_class = serializers.QuestionSerializer

class list_create_answers(generics.ListCreateAPIView):
	serializer_class = serializers.AnswerSerializer

	def get_queryset(self):
		question_id = self.kwargs['question_id']
		return Answer.objects.filter(question=question_id)

	def perform_create(self, serializer):
		serializer.save(question_id = self.kwargs['question_id'])

class retrieve_update_del_answer(generics.RetrieveUpdateDestroyAPIView):
	queryset = Answer.objects.all()
	serializer_class = serializers.AnswerSerializer