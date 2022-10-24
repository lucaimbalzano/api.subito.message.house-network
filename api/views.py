from email import message
from rest_framework import generics
from .models import Messages, House
from .serializers import MessagesSerializer, HouseSerializer

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
