from django.urls import path
from .views import HomePageView,BmiView

urlpatterns = [
path('calculator',BmiView.as_view()),
path('', HomePageView.as_view(), name='home')
]