from django.urls import path

from . import views

app_name = 'P'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:pk>/', views.detail_view, name='detail'),
]
