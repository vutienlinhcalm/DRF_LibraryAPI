from django.db import models

class genres(models.Model):
    class Meta:
        db_table = 'genres'
    id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=100)
    def __str__(self):
        return self.genre_name