from rest_framework import serializers
from app.models import Train


class TrainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Train
        fields = '__all__'
