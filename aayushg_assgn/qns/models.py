from django.db import models

# Create your models here.

class Qns(models.Model):
	qn_id = models.IntegerField(primary_key=True)
	qn = models.CharField(max_length=255)
	option1 = models.CharField(max_length=255)
	option2 = models.CharField(max_length=255)
	option3 = models.CharField(max_length=255)
	option4 = models.CharField(max_length=255)
	correct = models.CharField(max_length=255)

	class Meta:
		managed = True
		db_table = 'qns'