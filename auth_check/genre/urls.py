from django.urls import path
from genre import views
urlpatterns = [
    path('',views.genreApi),
    path('<int:id>/',views.genre_detailApi),
]