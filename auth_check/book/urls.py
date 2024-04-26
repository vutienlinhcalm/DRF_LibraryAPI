from django.urls import path
from book import views
urlpatterns = [
    path('',views.bookApi),
    path('<int:id>/',views.book_detailApi),
]