from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),
    path('polls/',views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('polls/<int:pk>/',  views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),

    path('',views.homepage),
    path('data/',views.personal_data,name = 'personal_data'),

    path('polls/<int:question_id>/delete/', views.delete, name='del'),

    path('polls/delete', views.delete_question, name='del_question'),

]
