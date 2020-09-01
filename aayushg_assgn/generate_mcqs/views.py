from django.shortcuts import render
import random, operator, requests, json
from fractions import Fraction
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.views import APIView


# Generating Unique Questions, their Answers & Suggested Options
class qnGenerate(APIView):

	def post(self, request):
		count = request.data
		count = count["count"]

		# This will make sure that qns do not repeat
		qnsapi = requests.get(url = "http://aayushgadia.pythonanywhere.com/qns/")
		qnsapi = qnsapi.text
		qnsapi = json.loads(qnsapi)
		qns = list(qnsapi["data"].keys())
		#print (qns)

		qns_dict = {}
		operators = {"+" : operator.add, "-" : operator.sub, "/" : operator.truediv, "*" : operator.mul}

		for i in range(1,int(count)+1):
			while True:
				op = random.choice(list(operators.keys()))
				if op == "*":
					num1 = random.randint(1,99)
					num2 = random.randint(1,99)

				else:
					num1 = random.randint(1,999)
					num2 = random.randint(1,999)

				question = "What is "+str(num1)+str(op)+str(num2)+" ?"

				if question not in qns:
					qns.append(question)
					ans_op = random.choice(["op1","op2","op3","op4"])
					if op =="/":
						correct_ans = str(Fraction(num1,num2))

					else:
						correct_ans = operators[op](num1,num2)

					qns_dict[i] = {"qn" : question, ans_op : correct_ans, "correct" : correct_ans}
					for each in ["op1","op2","op3","op4"]:
						if each != ans_op:
							if op == "/" :
								qns_dict[i][each] = str(random.randint(1,9999))+"/"+str(random.randint(1,9999))
							elif op == "-":
								qns_dict[i][each] = operators[op](random.randint(1,999),random.randint(1,999))
							else:
								qns_dict[i][each] = random.randint(1,9999)

					break

				else:
					#print ("Non-Unique")
					continue

		#print (qns_dict)
		send = json.dumps(qns_dict)
		headers = {'Content-type': 'application/json'}
		response = requests.post(url = "http://aayushgadia.pythonanywhere.com/qns/", data = send, headers = headers)
		return JsonResponse(json.loads(response.text))