from django.urls import path
from . import views


urlpatterns = [
	path('', views.QuizAll.as_view()),
    ]