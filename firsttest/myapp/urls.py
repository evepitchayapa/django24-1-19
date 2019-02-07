from django.urls import path
from . import views
app_name = 'template'
urlpatterns = [
    path('m/9',views.multiplication,name= 'mul'),

]
