from django.urls import path
from companypublic import views
urlpatterns = [
    path('',views.companypublicApi),
    path('<int:id>/',views.companypublic_detailApi),
]