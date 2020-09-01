from django.db import models

# Create your models here.

class Quiz(models.Model):
	quiz_id = models.IntegerField(primary_key=True)
	student_id = models.IntegerField()
	score = models.IntegerField()

	class Meta:
		managed = True
		db_table = 'quiz'


class Students(models.Model):
	student_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	std = models.CharField(max_length=255)
	school = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	country = models.CharField(max_length=255)

	class Meta:
		managed = False
		db_table = 'students'