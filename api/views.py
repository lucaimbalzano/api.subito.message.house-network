from email import message
from functools import reduce
import json
from textwrap import indent
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import operator
from requests import Response
from rest_framework import generics

from api.dto.res_api_house import HouseRequestDTOEncoder, HouseResponseDTO
from .models import Messages, House
from .serializers import MessagesSerializer, HouseSerializer
from api import serializers


def render(data,message,status_code, accepted_media_type=None, renderer_context=None):
        our_response_dict = {
            'version': '1.0',
            'data': {},
            'message': '',
        }
        
        our_response_dict['data'] = data
        our_response_dict['statusCode'] = status_code
        our_response_dict['message'] = message
        data = our_response_dict

        return json.dumps(data)

class MessagesList(generics.ListCreateAPIView):
    serializer_class = MessagesSerializer

    def get_queryset(self):
        queryset = Messages.objects.all()
        house = self.request.query_params.get('house')
        if house is not None:
            queryset = queryset.filter(numberSent=house)
        return queryset


class MessagesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessagesSerializer
    queryset = Messages.objects.all()
    




class HouseList(generics.ListCreateAPIView):
    serializer_class = HouseSerializer
    queryset = House.objects.all()

class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HouseSerializer
    queryset = House.objects.all()


def HouseCheckByNumber(request, number_house):
    serializer_class = HouseSerializer
    respone = 0
    queryset = House.objects.filter(number=number_house).values()
    return HttpResponse(queryset)


def HouseCheckByNumberAndAvertising(request, number_house, advertising_house):
    serializer_class = HouseSerializer
    respone = 0
    q_list = [Q(number=number_house), Q(advertising=advertising_house)]
    queryset = House.objects.filter(reduce(operator.and_, q_list)).values()
    
    return HttpResponse(queryset)
    
    