from django.db import models

# Create your models here.

class Students(models.Model):
	student_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	std = models.CharField(max_length=255)
	school = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	country = models.CharField(max_length=255)

	class Meta:
		managed = True
		db_table = 'students'