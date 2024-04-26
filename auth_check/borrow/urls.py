from django.urls import path
from borrow import views
urlpatterns = [
    path('',views.borrowApi),
    path('<int:id>/',views.borrow_detailApi),
]