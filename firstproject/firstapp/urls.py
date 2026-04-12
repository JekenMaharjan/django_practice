from django.urls import path
from . import views

urlpatterns = [
    path('hello_world', views.hello_world),
    path('HelloEthiopia', views.HelloEthiopia.as_view()),
    path('my_first', views.my_first),
    path('members', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
