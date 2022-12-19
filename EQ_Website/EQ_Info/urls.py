from django.urls import path
from . import views
from EQ_Info.views import EQ_page

# URLConf
urlpatterns = [
    path('', EQ_page),
]