from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class users(models.Model):
    class Meta:
        db_table = 'user'
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(_('password'), max_length=128)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]
    

