from django.urls import path
from .views import MessagesList, MessagesDetail, HouseList, HouseDetail, HouseCheckByNumber, HouseCheckByNumberAndAvertising, TrackProcessList, TrackProcessDetail, StateMachineProcessList, StateMachineProcessDetail, TimeManagerList, TimeManagerDetail, FlowInputScraperConfigDetail, FlowInputScraperConfigList
from api import views


urlpatterns = [

    path('scraper/config', FlowInputScraperConfigList.as_view()),
    path('scraper/config/<int:pk>', FlowInputScraperConfigDetail.as_view()),

    path('timemanager/', TimeManagerList.as_view()),
    path('timemanager/<int:pk>', TimeManagerDetail.as_view()),
    path('timemanager/last/', views.latest_time_manager),

    path('track/', TrackProcessList.as_view()),
    path('track/<int:pk>', TrackProcessDetail.as_view()),
    path('track/last/', views.latest_track_process),
    # path('track/<identifier_process>', views.get_by_identifier_proc),

    path('state/', StateMachineProcessList.as_view()),
    path('state/<int:pk>', StateMachineProcessDetail.as_view()),
    path('state/last/', views.latest_state_machine),

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
