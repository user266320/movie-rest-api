from django.urls import path
from .views import MovieInsert,MoviesUpdateAndDelete
urlpatterns=[
    path('movies/',MovieInsert.as_view()),
    path('movies/<int:pk>/',MoviesUpdateAndDelete.as_view())
]