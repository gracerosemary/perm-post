from django.urls import path
from .views import TrackerList, TrackerDetail

urlpatterns = [
    path('', TrackerList.as_view(), name='tracker_list'),
    path('<int:pk>', TrackerDetail.as_view(), name='tracker_detail'),
] 