from django.urls import path
from .views import HomePageView,BmiView

urlpatterns = [
path('calculators',BmiView.as_view(),name='bmi'),
path('', HomePageView.as_view(), name='home')
]