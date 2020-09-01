from django.http import JsonResponse
from .models import Quiz, Students
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.views import APIView
import requests, json


class QuizAll(APIView):

	#for saving the quiz score
	def post(self, request):
		ip = request.data
		model_use = Quiz()
		model_use.student_id = ip["id"]
		model_use.score = ip["score"]
		model_use.save()

		data = {"code" : 201, "status" : "Created", "message" : "Data Saved"}
		return JsonResponse(data)


	#for returning the Top 10 scorer
	def get(self, request):
		obj = Quiz.objects.order_by('-score')[:10]
		i = 1
		op = {}
		for every in obj:
			obj2 = Students.objects.get(student_id = int(every.student_id))
			name = str(obj2.name)
			std = str(obj2.std)
			school = str(obj2.school)
			city = str(obj2.city)
			country = str(obj2.country)
			everyScore = int(every.score)

			op[str(i)] = {"Name" : name, "Quiz Score" : everyScore, "Class" : std, "School" : school, "City" : city, "Country" : country}
			
			i += 1

		data = {"code" : 200, "status" : "OK", "message" : "Data Fetched Successfully", "data" : op}
		return JsonResponse(data)
		