from django.urls import path 
from testapp.views import DetailView,Details_View1
from rest_framework.authtoken import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[
    path('data',DetailView.as_view()),
    path('data/<int:pk>',Details_View1.as_view()),
    path('get_token',ObtainAuthToken.as_view())
]