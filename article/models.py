from django.db import models

# Create your models here.
class Articles(models.Model):
    id = models.TextField(db_column='_id', primary_key=True)
    url = models.CharField(db_column='url', max_length=500)  # Field name made lowercase.
    team = models.CharField(db_column='team', max_length=10)  # Field name made lowercase.
    date = models.CharField(db_column='date', max_length=10)  # Field name made lowercase.
    time = models.CharField(db_column='time', max_length=50)  # Field name made lowercase.
    publisher = models.CharField(db_column='publisher', max_length=50)  # Field name made lowercase.
    journalist = models.CharField(db_column='journalist', max_length=50)  # Field name made lowercase.
    title = models.CharField(db_column='title', max_length=200)  # Field name made lowercase.
    content = models.CharField(db_column='content', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'articles'
