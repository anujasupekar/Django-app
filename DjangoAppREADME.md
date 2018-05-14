# Django-app

### This is a Django application which is a QnA(Question and Answer) site. 
Overview:

**Models** [models.py](https://github.com/anujasupekar/Django-app/blob/master/askit/models.py)
  + There are 2 models, Question model and Answer model
  + Answer model has question as the foreign key
  
**Views** [views.py](https://github.com/anujasupekar/Django-app/blob/master/askit/views.py)
  There are views for following features,
  + GET list of questions
  + GET details of a specific question
  + POST a new question
  + Upvote or Downvote a question
  + POST a new answer for a specific question
  
**URL Conf** [urls.py](https://github.com/anujasupekar/Django-app/blob/master/askit/urls.py)
  + Specified url path and the corresponding view in askit/urls.py.
  
**Templates** [templates](https://github.com/anujasupekar/Django-app/tree/master/askit/templates/askit)
  + Created template files in askit/templates/askit/template_file.html
  + There are different html template files for all the views
  
**Static Files** [static files](https://github.com/anujasupekar/Django-app/tree/master/askit/static/askit)
  + Created CSS file for styling and Javascript file for making AJAX api calls
  + The path for static files is askit/static/askit/static_file
  
 The default SQLite database is used.

Screenshots of the application:
1. GET list of questions
![alt text](https://github.com/anujasupekar/Django-app/blob/master/screenshots/GET%20list%20of%20questions%20(homepage).png)

2. GET details of a specific question
![alt text](https://github.com/anujasupekar/Django-app/blob/master/screenshots/GET%20question%20detail.png)

3. POST a new answer for a specific question
![alt text](https://github.com/anujasupekar/Django-app/blob/master/screenshots/POST%20new%20answer.png)

4. POST a new question
![alt text](https://github.com/anujasupekar/Django-app/blob/master/screenshots/POST%20new%20question.png)
