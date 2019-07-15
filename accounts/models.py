from django.db import models

# Create your models here.
class open_account(models.Model):
	name=models.CharField(max_length=150)
	current_address=models.CharField(max_length=150)
	aadhar=models.CharField(max_length=150)
	pan=models.CharField(max_length=150)
	relative=models.CharField(max_length=150)
 #	relation=models.Charfield(max_length=150)
