from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('subjects', views.subjects, name="subjects"),
    path('subjects/<int:id>', views.subject, name="subject"),
    path('subjects/level/<str:level>', views.subject_level, name="level"),
    path('search', views.search, name="search"),
]