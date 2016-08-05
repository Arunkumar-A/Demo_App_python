from django.conf.urls import include, url
from .views import Facebook_view
from .views import facebook
urlpatterns = [
                  url('webhook', Facebook_view.as_view()),
                  url('',facebook.as_view()) 
               ]