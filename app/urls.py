from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getProject),
    path('post/', views.postProject),
    path('put/<int:id>/', views.putProject),
    path('delete/<int:id>/', views.delProject),
]
