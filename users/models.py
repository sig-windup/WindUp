from django.db import models
# Create your models here.
from django.db import models

class User(models.Model) :
    user_id = models.CharField(max_length=20, primary_key=True)
    team_id = models.TextField()
    password = models.CharField(max_length=16)

    def create_user(self, id, pwd, team):
        self.user_id = id
        self.password = pwd
        self.team_id = team