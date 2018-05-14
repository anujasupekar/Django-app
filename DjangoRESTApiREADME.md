# Django REST Framework 

### This is the REST Api implementation for the Django App using Django REST Framework

**Models** [models.py](https://github.com/anujasupekar/Django-app/blob/master/askit/models.py)
  + There are 2 models, Question model and Answer model
  + Answer model has question as the foreign key
  
**Serializers** [serializers.py](https://github.com/anujasupekar/Django-app-and-Django-REST/blob/master/askitREST/serializers.py)
  + Implemented QuestionSerializer and AnswerSerializer for the Question and Answer model respectively.
  
**Views** [views.py](https://github.com/anujasupekar/Django-app-and-Django-REST/blob/master/askitREST/views.py)
  Implemented GenericViews 
  + ListCreateApiView for listing questions or creating new question
  + RetrieveUpdateDestroyApiView to retrieve details of a specific question or update or destroy a question
  + ListCreateApiView for listing answers or creating new answer for a specific question
  + RetrieveUpdateDestroyApiView to retrieve details of a specific answer or update or destroy a answer
  
**URL Conf** [urls.py](https://github.com/anujasupekar/Django-app-and-Django-REST/blob/master/askitREST/urls.py)
  + Specified url and the corresponding view in askitREST/urls.py.
  
Screenshots of the application:
1. ListCreateApiView for listing/creating question
![alt text](https://github.com/anujasupekar/Django-app-and-Django-REST/blob/master/screenshots/list%20of%20questions.png)
![alt text](https://github.com/anujasupekar/Django-app-and-Django-REST/blob/master/screenshots/create%20new%20question.png)

2. RetrieveUpdateDestroyApiView for specific question
![alt text](https://github.com/anujasupekar/Django-app-and-Django-REST/blob/master/screenshots/retrieve:update:delete%20specific%20question.png)

3. ListCreateApiView for listing/creating answer for a question
![alt text](https://github.com/anujasupekar/Django-app-and-Django-REST/blob/master/screenshots/list%20answers:create%20new%20answer.png)

4. RetrieveUpdateDestroyApiView for specific answer
![alt text](https://github.com/anujasupekar/Django-app-and-Django-REST/blob/master/screenshots/retrieve:update:delete%20specific%20answer.png)
