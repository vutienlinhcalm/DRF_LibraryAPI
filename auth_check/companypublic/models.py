from django.db import models

class companypublics(models.Model):
    class Meta:
        db_table = 'companypublic'
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    info_company = models.CharField(max_length=200)
    def __str__(self):
        return self.company_name
