from django.urls import path
from . import views


urlpatterns = [
	path('', views.StudentsAll.as_view()),
    ]