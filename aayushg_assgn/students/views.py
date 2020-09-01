from django.http import JsonResponse
from .models import Students
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.views import APIView
import requests, json


class StudentsAll(APIView):

	#for saving the students details
	def post(self, request):
		ip = request.data
		model_use = Students()
		model_use.name = ip["name"]
		model_use.std = ip["class"]
		model_use.school = ip["school"]
		model_use.city = ip["city"]
		model_use.country = ip["country"]
		model_use.save()

		data = {"code" : 201, "status" : "Created", "message" : "Data Saved"}
		return JsonResponse(data)


	#for getting the student id
	def get(self, request):
		obj = Students.objects.all()
		student_id = obj[len(obj)-1].student_id

		op = {"id" : student_id}
		data = {"code" : 200, "status" : "OK", "message" : "Data Fetched Successfully", "data" : op}
		return JsonResponse(data)

