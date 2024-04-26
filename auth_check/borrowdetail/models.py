from django.db import models
from book.models import books
from borrow.models import borrows
class borrowdetails(models.Model):
    class Meta:
        db_table = 'borrowdetail'
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    borrow = models.ForeignKey(borrows, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=True)
