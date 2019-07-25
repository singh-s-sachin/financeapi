from django.db import models
# Create your models here.
class open_account(models.Model):
	name=models.CharField(max_length=150)
	current_address=models.CharField(max_length=150)
	aadhar=models.CharField(max_length=150)
	pan=models.CharField(max_length=150)
	relative=models.CharField(max_length=150)
	mobile=models.CharField(max_length=10)
	amount=models.CharField(max_length=6)
def __str__(self):
        return '%s %s' % (self.name, self.amount)