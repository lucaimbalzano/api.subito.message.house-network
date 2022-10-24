from dataclasses import fields
from rest_framework import serializers
from .models import Messages, House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('__all__')


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('__all__')