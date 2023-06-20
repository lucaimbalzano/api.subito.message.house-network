from dataclasses import fields
from rest_framework import serializers
from .models import Messages, House, TrackProcess, MachineProcess

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('__all__')


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('__all__')


class TrackProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackProcess
        fields = ('__all__')


class StateMachineProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineProcess
        fields = ('__all__')


