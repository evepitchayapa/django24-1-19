from django.urls import path
from . import views

urlpatterns =[
    path('<int:num>/',views.show_mul , ),
]
