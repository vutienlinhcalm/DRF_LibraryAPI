from django.urls import path
from author import views
urlpatterns = [
    path('',views.authorApi),
    path('<int:id>/',views.authors_detailApi),
]