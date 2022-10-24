from django.urls import path
from .views import MessagesList, MessagesDetail, HouseList, HouseDetail


urlpatterns = [
    path('messages/', MessagesList.as_view()),
    path('messages/<int:pk>/', MessagesDetail.as_view()),
    path('house/', HouseList.as_view()),
    path('house/<int:pk>/', HouseDetail.as_view()),
]
