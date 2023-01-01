from rest_framework import serializers
from .models import *
class PassengerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerModel
        fields = ['id','first_name','last_name','reward_points']