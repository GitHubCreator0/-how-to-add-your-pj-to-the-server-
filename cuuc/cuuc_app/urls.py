from django.urls import path
from . import views

urlpatterns = [
    path('p1/', views.page_1),
    path('', views.page_2)
]
