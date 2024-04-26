from django.db import models
from users.models import users
class borrows(models.Model):
    class Meta:
        db_table = 'borrow'
    ORDER_STATUSES=(
        ('PENDING','Vẫn còn'),
        ('BORROW','Đã mượn'),
        ('DUEDAY','Quá hạn')
    )
    id = models.AutoField(primary_key=True)
    dayborrow = models.DateField(auto_now_add=True)
    dueborrow = models.DateField(auto_now_add=True)
    user = models.ForeignKey(users, blank=True, on_delete= models.CASCADE)
    borrow_status=models.CharField(max_length=25,choices=ORDER_STATUSES,default=ORDER_STATUSES[0][0])
