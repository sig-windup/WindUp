from django.db import models

# Create your models here.
class Starting_lineup(models.Model) :
    lineup_id = models.TextField(db_column='_id', primary_key=True)
    date = models.CharField(db_column='date', max_length=20, null=True)
    name = models.CharField(db_column='name', max_length=20)
    team = models.CharField(db_column='team', max_length=20)
    position = models.CharField(db_column='position', max_length=20)
    order = models.IntegerField(db_column='order', default=0)

    class Meta:
        managed = False
        db_table = 'starting_lineup'

class Player(models.Model) :
    player_id = models.TextField(db_column='_id', primary_key=True)
    team = models.CharField(db_column='team', max_length=20)
    name = models.CharField(db_column='name', max_length=20)
    backNum = models.CharField(db_column='backNum', max_length=20)
    birth = models.CharField(db_column='birth', max_length=20)
    position = models.CharField(db_column='position', max_length=30)

    class Meta:
        managed = False
        db_table = 'players'

class Pitcher_stats(models.Model):
    stat_id = models.TextField(db_column='_id', primary_key=True)
    name = models.CharField(db_column='name', max_length=20)
    team = models.CharField(db_column='team', max_length=20)
    opposite_team = models.CharField(db_column='oppositeTeam', max_length=20)
    w = models.CharField(db_column='w', max_length=20)
    l = models.CharField(db_column='l', max_length=20)
    save = models.CharField(db_column='save', max_length=20)
    hld = models.CharField(db_column='hld', max_length=20)
    blown = models.CharField(db_column='blown', max_length=20)
    game = models.CharField(db_column='game', max_length=20)
    gs = models.CharField(db_column='gs', max_length=20)
    ip = models.CharField(db_column='ip', max_length=20)
    k = models.CharField(db_column='k', max_length=20)
    bb = models.CharField(db_column='bb', max_length=20)
    hr = models.CharField(db_column='hr', max_length=20)
    babip = models.CharField(db_column='babip', max_length=20)
    lob = models.CharField(db_column='lob', max_length=20)
    era = models.CharField(db_column='era', max_length=20)
    ra = models.CharField(db_column='ra', max_length=20)
    fip = models.CharField(db_column='fip', max_length=20)
    kfip = models.CharField(db_column='kfip', max_length=20)
    war = models.CharField(db_column='war', max_length=20)


    class Meta:
        managed = False
        db_table = 'pitcher_stats'


class Hitter_stats(models.Model):
    stat_id = models.TextField(db_column='_id', primary_key=True)
    name = models.CharField(db_column='name', max_length=20)
    team = models.CharField(db_column='team', max_length=20)
    opposite_team = models.CharField(db_column='oppositeTeam', max_length=20)
    game = models.CharField(db_column='game', max_length=20)
    pa = models.CharField(db_column='pa', max_length=20)
    ab = models.CharField(db_column='ab', max_length=20)
    h = models.CharField(db_column='h', max_length=20)
    oneb = models.CharField(db_column='1b', max_length=20)
    twob = models.CharField(db_column='2b', max_length=20)
    threeb = models.CharField(db_column='3b', max_length=20)
    hr = models.CharField(db_column='hr', max_length=20)
    r = models.CharField(db_column='r', max_length=20)
    rbi = models.CharField(db_column='rbi', max_length=20)
    bb = models.CharField(db_column='bb', max_length=20)
    ibb = models.CharField(db_column='ibb', max_length=20)
    hbp = models.CharField(db_column='hbp', max_length=20)
    k = models.CharField(db_column='k', max_length=20)
    sf = models.CharField(db_column='sf', max_length=20)
    sh = models.CharField(db_column='sh', max_length=20)
    gidp = models.CharField(db_column='gidp', max_length=20)
    sb = models.CharField(db_column='sb', max_length=20)
    cs = models.CharField(db_column='cs', max_length=20)
    avg = models.CharField(db_column='avg', max_length=20)

    class Meta:
        managed = False
        db_table = 'hitter_stats'

