# Importing Libraries
import requests, json


# Student Details Enter before Quiz Starts
name = str(input("Please enter your Name- "))
std = str(input("Enter your Class- "))
school = str(input("Enter your School- "))
city = str(input("Enter your City- "))
country = str(input("Enter your Country- "))

student_data = {"name" : name, "class" : std, "school" : school, "city" : city, "country" : country}


# API call for saving student details
send = json.dumps(student_data)
headers = {'Content-type': 'application/json'}
response = requests.post(url = "http://aayushgadia.pythonanywhere.com/students-data/", data = send, headers = headers)
print (response.text)


# API call returning student id
response = requests.get(url = "http://aayushgadia.pythonanywhere.com/students-data/")
response = response.text
response = json.loads(response)
studentId = response["data"]["id"]
print (studentId)


# Quiz Starts
score = 0
qnsapi = requests.get(url = "http://aayushgadia.pythonanywhere.com/qns/")
qnsapi = qnsapi.text
qnsapi = json.loads(qnsapi)
qns = qnsapi["data"]
i = 1

for qn in qns:
    print("\n","Question"+str(i)+" - "+qn)
    print ("1. "+qns[qn]["1"]+"  2. "+qns[qn]["2"]+"  3. "+qns[qn]["3"]+"  4. "+qns[qn]["4"],"\n")
    ans = str(input("Enter the Correct Option in terms of 1,2,3 or 4 \n"))
    
    while True:
        if ans not in ["1","2","3","4"]:
            ans = str(input("Enter the Correct Option in terms of 1,2,3 or 4 \n"))
        else:
            break
    
    if qns[qn][ans] == qns[qn]["correct"]:
        print ("Correct")
        score += 1
        
    i += 1
        
print (score)


# API call for saving student's quiz score
quiz_data = {"id" : studentId, "score" : score}
send = json.dumps(quiz_data)
headers = {'Content-type': 'application/json'}
response = requests.post(url = "http://aayushgadia.pythonanywhere.com/quiz-data/", data = send, headers = headers)
print (response.text)
       

# API call for viewing the Top 10 Scorers
response = requests.get(url = "http://aayushgadia.pythonanywhere.com/quiz-data/")
response = response.text
response = json.loads(response)
print (response["data"])


# by AAYUSH GADIA
