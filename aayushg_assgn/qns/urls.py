from django.urls import path
from . import views


urlpatterns = [
	path('', views.AllQns.as_view()),
    ]