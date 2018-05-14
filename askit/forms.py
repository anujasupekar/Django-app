'''from django.forms import ModelForm
from .models import Question
from django.forms import ModelChoiceField



# Create the form class.
class QuestionForm(ModelForm):
	class Meta:
		model = Question
		fields = ['title','post_date', 'posted_by']
		answer = ModelChoiceField(queryset=Question.answer_set, empty_label=None)'''