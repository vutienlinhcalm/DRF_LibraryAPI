from django.urls import path
from borrowdetail import views
urlpatterns = [
    path('',views.borrowdetailApi),
    path('<int:id>/',views.borrowdetail_detailApi),
]