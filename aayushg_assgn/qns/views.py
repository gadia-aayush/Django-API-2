from django.http import JsonResponse
from .models import Qns
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.views import APIView
import requests, json


class AllQns(APIView):

	#for saving the mcq's generated into the database
	def post(self, request):
		ip = request.data
		for i in range(1,len(ip)+1):
			i = str(i)
			model_use = Qns()
			model_use.qn = str(ip[i]['qn'])
			model_use.option1 = str(ip[i]['op1'])
			model_use.option2 = str(ip[i]['op2'])
			model_use.option3 = str(ip[i]['op3'])
			model_use.option4 = str(ip[i]['op4'])
			model_use.correct = str(ip[i]['correct'])
			model_use.save()
		
			#qn = Qns.objects.create(qn = str(ip[i]['qn']), option1 = str(ip[i]['op1']), option2 = str(ip[i]['op2']), option3 = str(ip[i]['op3']), option4 = str(ip[i]['op4']), correct = str(ip[i]['correct']))
			#qn.save()

		data = {"code" : 201, "status" : "Created", "message" : "Qns Generated & Saved"}
		return JsonResponse(data)


	#for getting qns for the quiz, currently simply fetching first 20 qns
	def get(self, request):
		obj = Qns.objects.all()[:20]
		if len(obj) != 20:
			count = 20-len(obj)
			ip = {"count" : count}
			send = json.dumps(ip)
			headers = {'Content-type': 'application/json'}
			response = requests.post(url = "http://aayushgadia.pythonanywhere.com/generate-qns/", data = send, headers = headers)
			print (response.text)

		obj = Qns.objects.all()[:20]
		op = {}
		for every in obj:
			op[str(every.qn)] = {"1" : str(every.option1), "2" : str(every.option2), "3" : str(every.option3),
							"4" : str(every.option4), "correct" : str(every.correct)}

		data = {"code" : 200, "status" : "OK", "message" : "Data Fetched Successfully", "data" : op}
		return JsonResponse(data)
