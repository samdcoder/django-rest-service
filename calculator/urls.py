from django.urls import path
from .views import addition, subtraction, multiplication, division

urlpatterns = [
    path('addition/', addition, name='addition'),
    path('subtraction/', subtraction, name='subtraction'),
    path('multiplication/', multiplication, name='multiplication'),
    path('division/', division, name='division')
]