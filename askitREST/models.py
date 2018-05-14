'''from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=20)
	posted_by = models.CharField(max_length=20)
	post_date = models.DateTimeField()
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Answer(models.Model):
	answer = models.TextField()
	written_by = models.CharField(max_length=20)
	post_date = models.DateTimeField()
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.answer'''
