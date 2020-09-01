from django.urls import path
from . import views


urlpatterns = [
	path('', views.qnGenerate.as_view()),
    ]