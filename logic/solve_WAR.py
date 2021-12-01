# 리그 평균 상수값
LEAGUE_AVG_wOBA = 0.344
LEAGUE_AVG_wOBAScale = 1.224

# 계산 상수값
BASE_ON_BALLS = 0.691
HIT_BY_PITCH = 0.722
ONE_BASE_HIT = 0.884
TWO_BASE_HIT = 1.257
THREE_BASE_HIT = 1.593
HOMERUN = 2.058
RUN_STEALING_BASE = 0.200
RUN_CAUGHT_STEALING = -0.438


class Hitter:
    def __init__(self, name, team, oppositeTeam, game, pa, ab, h, oneb, twob, threeb, hr, r, bb, ibb, hbp, k, sf, sh, gidp, sb, cs, avg):
        self.name = name
        self.team = team
        self.oppositeTeam = oppositeTeam
        self.game = float(game)
        self.pa = float(pa)
        self.ab = float(ab)
        self.h = float(h)
        self.oneb = float(oneb)
        self.twob = float(twob)
        self.threeb = float(threeb)
        self.hr = float(hr)
        self.r = float(r)
        self.bb = float(bb)
        self.ibb = float(ibb)
        self.hbp = float(hbp)
        self.k = float(k)
        self.sf = float(sf)
        self.sh = float(sh)
        self.gidp = float(gidp)
        self.sb = float(sb)
        self.cs = float(cs)
        self.avg = avg

    def WAR(self):
        return self.wRAA() + self.wSB()

    def wRAA(self):
        return (self.wOBA() - LEAGUE_AVG_wOBA) / LEAGUE_AVG_wOBAScale * self.pa

    def wOBA(self):
        if (self.pa + self.bb - self.ibb + self.sf + self.hbp) == 0:
            return 0
        else:
            return (BASE_ON_BALLS * (self.bb-self.ibb) + HIT_BY_PITCH * self.hbp + ONE_BASE_HIT * self.oneb + TWO_BASE_HIT * self.twob + THREE_BASE_HIT * self.threeb + HOMERUN * self.hr) / \
               (self.pa + self.bb - self.ibb + self.sf + self.hbp)

    def wSB(self):
        return RUN_STEALING_BASE * self.sb + RUN_CAUGHT_STEALING * self.cs
