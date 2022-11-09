from email import message
from functools import reduce
import json
from textwrap import indent
from django.http import HttpResponse, JsonResponse
from django.db.models import Q, When, Case, BooleanField, Value
import operator
from requests import Response
from rest_framework import generics

from api.dto.res_api_house import HouseRequestDTOEncoder, HouseResponseDTO
from .models import Messages, House, TrackProcess, StateMachineProcess
from .serializers import MessagesSerializer, HouseSerializer, TrackProcessSerializer, StateMachineProcessSerializer
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


class TrackProcessList(generics.ListCreateAPIView):
    serializer_class = TrackProcessSerializer
    queryset = TrackProcess.objects.all()

class TrackProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrackProcessSerializer
    queryset = TrackProcess.objects.all()






class StateMachineProcessList(generics.ListCreateAPIView):
    serializer_class = StateMachineProcessSerializer

    def get_queryset(self):
        queryset = Messages.objects.all()
        trackProcess = self.request.query_params.get('trackprocess')
        if trackProcess is not None:
            queryset = queryset.filter(processId=trackProcess)
        return queryset
class StateMachineProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StateMachineProcessSerializer
    queryset = TrackProcess.objects.all()







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




# HOUSE CUSTOM API


def HouseCheckByNumber(request, number_house):
    serializer_class = HouseSerializer
    respone = 0
    queryset = House.objects.filter(number=number_house).values()
    return HttpResponse(queryset)





def HouseCheckByAdvertising(request,advertising_house):
    serializer_class = HouseSerializer
    respone = 0
    queryset = House.objects.filter(advertising=advertising_house).values()
    
    return HttpResponse(queryset)

def HouseCheckByNumberAndAvertising(request, number_house, advertising_house):
    serializer_class = HouseSerializer
    respone = 0
    q_list = [Q(number=number_house), Q(advertising=advertising_house)]
    queryset = House.objects.filter(reduce(operator.and_, q_list)).values()
    
    return HttpResponse(queryset)


# def HouseCheckPriceAndRooms(request, price_house,rooms_house):
#     queryset =   House.objects.filter(price=price_house, age=rooms_house).annotate(
#                     house_price_rooms=Case(
#                         When(price=price_house, then=)),
#                         default=Value(False),
#                         output_field=BooleanField(),
#                     ),
#                 )
#     return HttpResponse(queryset)



def HouseCheckByVetrina(request,vetrina_house):
    serializer_class = HouseSerializer
    respone = 0
    queryset = House.objects.filter(vetrina=vetrina_house).values()
    
    return HttpResponse(queryset)

def HouseCheckByNumberAndVetrina(request, number_house, vetrina_house):
    serializer_class = HouseSerializer
    respone = 0
    q_list = [Q(number=number_house), Q(vetrina=vetrina_house)]
    queryset = House.objects.filter(reduce(operator.and_, q_list)).values()
    
    return HttpResponse(queryset)
    