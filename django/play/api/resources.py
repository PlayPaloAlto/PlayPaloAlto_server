from tastypie.resources import ModelResource
from play.models import *


class CustomUserResource(ModelResource):
    class Meta:
        queryset = CustomUser.objects.all()
        allowed_methods = ['get','post']