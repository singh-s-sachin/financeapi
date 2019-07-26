from django.db import models
# Create your models here.
class open_account(models.Model):
	name=models.CharField(max_length=150)
	current_address=models.CharField(max_length=150)
	aadhar=models.CharField(max_length=150)
	pan=models.CharField(max_length=150)
	relative=models.CharField(max_length=150)
	mobile=models.CharField(max_length=10,primary_key=True)
	amount=models.CharField(max_length=6)
class create_fd(models.Model):
	mobile=models.CharField(max_length=10,primary_key=True)
	amount=models.CharField(max_length=10)
	time=models.CharField(max_length=5)
	maturity=models.CharField(max_length=10)
class create_loan(models.Model):
	mobile=models.CharField(max_length=10,primary_key=True)
	amount=models.CharField(max_length=10)
	duration=models.CharField(max_length=10)
	time=models.CharField(max_length=50)
	repay=models.CharField(max_length=10)
	approved=models.CharField(max_length=10)
def __str__(self):
        return '%s %s' % (self.name, self.amount)