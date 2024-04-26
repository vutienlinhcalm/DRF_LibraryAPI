
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/',include('author.urls')),
    path('companypublic/', include('companypublic.urls')),
    path('genre/',include('genre.urls')),
    path('book/',include('book.urls')),
    path('user/',include('users.urls')),
    path('borrow/',include('borrow.urls')),
    path('borrowdetail/',include('borrowdetail.urls')),

]
