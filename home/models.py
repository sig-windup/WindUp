from django.db import models

class Matches(models.Model):
    id = models.TextField(db_column='_id', primary_key=True)
    date = models.CharField(db_column='date', max_length=50)  # Field name made lowercase.
    state_game = models.CharField(db_column='state_game', max_length=50)  # Field name made lowercase.
    home = models.CharField(db_column='home', max_length=50)  # Field name made lowercase.
    home_score = models.CharField(db_column='home_score', max_length=50)  # Field name made lowercase.
    home_result = models.CharField(db_column='home_result', max_length=50)  # Field name made lowercase.
    home_time = models.CharField(db_column='home_time', max_length=50)  # Field name made lowercase.
    away = models.CharField(db_column='away', max_length=50)  # Field name made lowercase.
    away_score = models.CharField(db_column='away_score', max_length=50)  # Field name made lowercase.
    away_result = models.CharField(db_column='away_result', max_length=50)  # Field name made lowercase.
    away_time = models.CharField(db_column='away_time', max_length=50)  # Field name made lowercase.
    stadium = models.CharField(db_column='stadium', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'matches'

class Teams(models.Model):
    id = models.TextField(db_column='_id', primary_key=True)
    team_id = models.CharField(db_column='team_id', max_length=50)  # Field name made lowercase.
    team_name = models.CharField(db_column='team_name', max_length=50)  # Field name made lowercase.
    team_code = models.CharField(db_column='team_code', max_length=50)  # Field name made lowercase.
    team_img = models.CharField(db_column='team_img', max_length=50)  # Field name made lowercase.
    team_stadium = models.CharField(db_column='team_stadium', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teams'