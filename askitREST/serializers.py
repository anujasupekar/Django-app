from rest_framework import serializers
from askit.models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ('id', 'answer', 'written_by', 'question')
		read_only_fields = ['question']

class QuestionSerializer(serializers.ModelSerializer):
	#answers = AnswerSerializer(read_only=True, many=True)
	class Meta:
		model = Question
		fields = ('id', 'title', 'posted_by')






