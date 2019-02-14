from django.urls import path
from . import views
app_name = 'test1'
urlpatterns =[
    path('<int:num>/',views.show_mul,name = 'showmul'  ),
    path('',views.input,name = 'input'),
    path('result/',views.showresult,name = 'showresult'),
]
