from django.urls import path
from users import views
urlpatterns = [
    # path('',views.userApi),
    # path('<int:id>/',views.user_detailApi),
    path('register/',views.register.as_view(), name='register')
]