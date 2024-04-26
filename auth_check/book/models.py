from django.db import models
from author.models import authors
from genre.models import genres
from companypublic.models import companypublics

class books(models.Model):
    class Meta:
        db_table = 'book'
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(authors,on_delete=models.CASCADE)
    genre = models.ForeignKey(genres,on_delete=models.CASCADE)
    company = models.ForeignKey(companypublics,on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    release = models.DateField("date published")
    def __str__(self):
        return self.book_name
    

