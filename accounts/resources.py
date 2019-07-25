from tastypie.resources import ModelResource
from accounts.models import open_account 
class openaccount(ModelResource):
    class Meta:
        queryset = open_account.objects.all()
        resource_name = 'new'