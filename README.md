#### README- Assignment Submission :: Aayush Gadia

-----

##### API Name, Description, it's EndPoints, ScreenShots-
1. **qns**

- *API EndPoints-*
	- *Posting Qns URL- http://aayushgadia.pythonanywhere.com/qns/ (POST API)*
	- *Getting Qns URL- http://aayushgadia.pythonanywhere.com/qns/ (GET API)*


- *Description-*
	- *The URL of both the API's are same, only the difference happens based on the **type of request that is made.**. So, if a **GET** request is made on the same url, then **it fetches the first 20 qns from the the database as a QUIZ question** (We can also, shuffle them up, but currently it is simply fetching the first 20 questions.**Also, let's say that if the database doesn't contains 20 questions, then it also generates the no. of questions needed to make it 20, and finally returns those questions).***<br><br>
	- *Similarly, if the **POST** request is made on the same url, then **the questions which are generated are sent and using the API it is saved.** Currently, the script- **script_generate-mcqs.py**, is generating the questions randomly (detail about the script is written below.)*


- *Screenshots-*
	- ![1](https://github.com/gadia-aayush/rough/blob/master/1.png)
	- ![2](https://github.com/gadia-aayush/rough/blob/master/2.png)


2. **students**

- *API EndPoints-*
	- *Posting Students Data URL- http://aayushgadia.pythonanywhere.com/students-data/ (POST API)*
	- *Getting Student ID URL- http://aayushgadia.pythonanywhere.com/students-data/ (GET API)*


- *Description-*
	- *The URL of both the API's are same, only the difference happens based on the **type of request that is made.**. So, basically this **API is used when a student is attempting a QUIZ. So, before attempting the QUIZ, the student fills up the data which is asked by the script- "script_student-quiz.py"** (details explained ahead) and **that data is actually entered into the database using the POST API.*** <br><br>
	- *The GET API, is used to **fetch the ID of the student whose details was entered last. This is useful for the script- "script_student-quiz.py"***


- *Screenshots-*
	- ![3](https://github.com/gadia-aayush/rough/blob/master/3.png)
	- ![4](https://github.com/gadia-aayush/rough/blob/master/4.png)


3. **quiz**

- *API EndPoints-*
	- *Posting Quiz Score URL- http://aayushgadia.pythonanywhere.com/quiz-data/ (POST API)*
	- *Getting the Quiz LeaderBoard URL- http://aayushgadia.pythonanywhere.com/quiz-data/ (GET API)*


- *Description-*
	- *The URL of both the API's are same, only the difference happens based on the **type of request that is made.**.So, basically here the script- **"script_student-quiz.py"** (details explained ahead) when executed would later ask a few quiz qns and a student would be evaluated. So the **POST API enters the quiz score of the student who had attempted the quiz and saves it score in the database*** <br><br>
	- *Similarly, the **GET API is used to fetch the Top 10 students in the QUIZ LeaderBoard.***


- *Screenshots-*
	- ![5](https://github.com/gadia-aayush/rough/blob/master/5.png)
	- ![6](https://github.com/gadia-aayush/rough/blob/master/6.png)


-----

##### Scripts-

1. **script_generate-mcqs.py**-
	- *Here, the script is **generating unique qns, along with their options and correct answer.***
	- ***Also, it is made sure that the script generates unique qns and none of the questions are repeating.***
	- ***Currently, the script generates math problems, where questions on adding the numbers, subtracting the numbers, multiplying them, dividing them are asked.***
	- ***Also, for multiplication, 2 digits multiplication questions are asked & for addition, subtraction & division, 3 digits questions are asked.***
	- ***Also, it has been made sure that for division, the options displayed are in Fractions not in Decimal Values.***
	- *Once the script is executed, automatically at the end it makes a **POST Request Call at the Url-** **"http://aayushgadia.pythonanywhere.com/qns/"**, which saves the questions which are generated into the database.*
	- ***Snap of the Output of the Script-***<br>
		- ![10](https://github.com/gadia-aayush/rough/blob/master/10.png)<br><br>


2. **script_student-quiz.py**-
	- *Here, the script purpose is to **let the users participate in the quiz.**. So, this script first **asks the user to enter the details like name, class, school, city, country** & these details are saved by making a **POST Request Call at the URL- http://aayushgadia.pythonanywhere.com/students-data/**. <br>After that a **GET Request Call at the same URL, returns the ID of the Student whose details were saved in the database. The ID was generated in the database.***<br><br>*Now the Quiz Questions are displayed to the user. **20 Quiz Questions are fetched by the GET Request Call at the URL- "http://aayushgadia.pythonanywhere.com/qns/" , and the user just has to type the option like 1,2,3,4 and the script will keep calculating the score. Once all the 20 questions are answered, the score would be saved in the database along with the student id by making a POST Request Call at the URL- http://aayushgadia.pythonanywhere.com/quiz-data/***<br><br>*Finally, a **GET Request Call is made at the URL- http://aayushgadia.pythonanywhere.com/quiz-data/, which fetches the Top 10 Scorers of the QUIZ.<br><br>***
	- ***Snap of the Output of the Script-***<br>
		- ![11](https://github.com/gadia-aayush/rough/blob/master/11.png)<br><br>
		- ![12](https://github.com/gadia-aayush/rough/blob/master/12.png)<br><br>
		- ![13](https://github.com/gadia-aayush/rough/blob/master/13.png)<br><br>
	
-----

##### DATABASE-

- *Here, **the default SQLite Database is used for the Django Application.***
- *Models that were created were are- **Students, Quiz, Qns***
- *To, know more please visit the **db.sqlite3.***

- *Screenshots-*
	- ![7](https://github.com/gadia-aayush/rough/blob/master/7.png)
	- ![8](https://github.com/gadia-aayush/rough/blob/master/8.png)
	- ![9](https://github.com/gadia-aayush/rough/blob/master/9.png)
	
-----

##### Requirements-

- Django==2.1.5
- djangorestframework==3.9.1
- requests==2.24.0
- json5==0.8.5
- random, operator, fractions (Optional, as generally it comes installed)

-----

##### Author-
- **AAYUSH GADIA**
- **Phone- +91- 8334827095  |  Email- gadia.aayush@gmail.com**
- **[Wesbite](https://gadia-aayush.github.io/) | [GitHub](https://github.com/gadia-aayush)  |  [LinkedIn](https://www.linkedin.com/in/gadia-aayush/)**

------
