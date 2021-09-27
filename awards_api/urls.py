from django.urls import path
from . import views

urlpatterns = [
    path('awards/', views.snippet_list),
    path('awards/<int:pk>/', views.snippet_detail),
]