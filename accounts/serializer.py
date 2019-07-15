from rest_framework import serializers
from .models import open_account

class accountserializer(serializers.ModelSerializer)
	class Meta :
		modal = Lamguage
		fields ={"id","name"}
