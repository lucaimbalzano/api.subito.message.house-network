from django.urls import path
from .views import MessagesList, MessagesDetail, HouseList, HouseDetail, HouseCheckByNumber, HouseCheckByNumberAndAvertising
from api import views


urlpatterns = [
    path('messages/', MessagesList.as_view()),
    path('messages/<int:pk>/', MessagesDetail.as_view()),
    path('house/', HouseList.as_view()),
    path('house/<int:pk>/', HouseDetail.as_view()),
    path('house/check/<number_house>/', views.HouseCheckByNumber),
    path('house/check/vetrina/<number_house>/<vetrina_house>', views.HouseCheckByNumberAndVetrina),
    path('house/check/vetrina/<vetrina_house>', views.HouseCheckByVetrina),
    path('house/check/advertising/<advertising_house>', views.HouseCheckByAdvertising),
    path('house/check/advertising/<number_house>/<advertising_house>', views.HouseCheckByNumberAndAvertising),
    # path('house/check/price/<price_house>/rooms/<rooms_house>', views.HouseCheckPriceAndRooms),
   
]
