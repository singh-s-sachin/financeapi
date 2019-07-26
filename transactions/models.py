from django.db import models

# Create your models here.
class transaction(models.Model):
    tid=models.CharField(max_length=150)
    kind=models.CharField(max_length=150)
    account=models.CharField(max_length=150)
    amount=models.IntegerField()