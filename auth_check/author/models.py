from django.db import models

class authors(models.Model):
    class Meta:
        db_table = 'authors'
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100)
    award = models.CharField(max_length= 100)
    def __str__(self):
        return self.author_name

    
