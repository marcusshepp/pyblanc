import math
from datetime import date

import numpy as np

from lbonevnine.lbonevnine import BackEnd
import util as util_ez


class League(BackEnd):
    """ Base League Object. """

    class Meta:
        abstract = True


class LeagueStat(League):
    """ 
    Handles the `Stat` data field. 
    Available methods:
        get_stat
        all_minions_killed
        average_cs
        winoverlose
        get_champion_id
        all_champion_ids
        cs_per_min
        xp_per_min
    """

    def __unicode__(self):
        return u"pyblanc.LeagueStat object instance. Summoner: {summ}".format(
            summ=self.summoner)
     
    def get_stat(self, game_number, stat_name):
        """ Returns a `stat`. """
        parsed = self.get_data()
        return parsed['matches'][game_number]['participants'][0]['stats'][stat_name]
        
    def all_minions_killed(self):
        """ Returns an array of minionsKilled. """
        scores = []
        for i in range(0, 10):
            scores.append(self.get_stat(int(i), "minionsKilled"))
        return scores

    def average_cs(self):
        """ Returns the average creep score for the last ten games. """
        total = []
        total_creep_count = 0
        for i in range(0, 10):
            total.append(self.get_stat(int(i), "minionsKilled"))
        for j in range(0, len(total)):
            total_creep_count+=total[j]
        return total_creep_count/10

    def winsandloses(self):
        """ Returns wins and loses. """ 
        wl = [self.get_stat(x, "winner") for x in xrange(10)]
        return wl

    def winoverlose(self):
        """ Returns the win/lose ratio. """ 
        counter, num_of_wins, num_of_lose = 0, 0, 0
        for i in range(0, 10):
            if self.get_stat(int(i), "winner") == True:
                num_of_wins += 1
            else:
                num_of_lose += 1
        return math.ceil(num_of_lose/num_of_wins)
    
    def get_champion_id(self, game_number):
        parsed = self.get_data()
        return parsed['matches'][game_number]['participants'][0]['championId']
    
    def all_champions(self):
        container = []
        for game_number in range(10):
            container.append(self.get_champion_id(game_number))
        for i in xrange(10):
            container[i] = util_ez.champion_id_to_str(container[i])
        return container

    def get_timeline(self, game_number, stat_name):
        """ Returns a `timeline`. """
        parsed = self.get_data()
        return parsed['matches'][game_number]['participants'][0]['timeline'][stat_name]
    
    def cs_per_min(self):
        """
        :returns:
        [{u'zeroToTen': 6.81, u'tenToTwenty': 5.9},...]
        """
        x = [self.get_timeline(i, "creepsPerMinDeltas") for i in xrange(10)]
        return x

    def xp_per_min(self):
        """
        :returns:
        [{u'zeroToTen': 6.81, u'tenToTwenty': 5.9},...]
        """
        x = [self.get_timeline(i, "xpPerMinDeltas") for i in xrange(10)]
        return x
    
    def damage_dealt_to_champions(self):
        """
        :returns:
        [21520, 35665, 28709,...]
        """
        x = [self.get_stat(i, "totalDamageDealtToChampions") for i in xrange(10)]
        return x
    
    def first_blood(self):
        """
        :returns:
        [False, True,...]
        """
        x = [self.get_stat(i, "firstBloodKill") for i in xrange(10)]
        return x
    
    def gold_earned(self):
        """
        :returns:
        [10906, 12795,...]
        """
        x = [self.get_stat(i, "goldEarned") for i in xrange(10)]
        return x
        
    def longest_killing_spree(self):
        """
        :returns:
        [6, 2, 3...]
        """
        x = [self.get_stat(i, "largestKillingSpree") for i in xrange(10)]
        return x

    def largest_multikill(self):
        """
        :returns:
        [2, 2,...]
        """
        x = [self.get_stat(i, "largestMultiKill") for i in xrange(10)]
        return x
    
    def wards_placed(self):
        """
        :returns:
        [10, 18,...]
        """
        x = [self.get_stat(i, "wardsPlaced") for i in xrange(10)]
        return x
    
    def kills(self):
        """
        :returns:
        [10, 18,...]
        """
        x = [self.get_stat(i, "kills") for i in xrange(10)]
        return x
    
    def deaths(self):
        """
        :returns:
        [10, 18,...]
        """
        x = [self.get_stat(i, "deaths") for i in xrange(10)]
        return x   
    
    def assists(self):
        """
        :returns:
        [10, 18,...]
        """
        x = [self.get_stat(i, "assists") for i in xrange(10)]
        return x 
    
    def towers_killed(self):
        """
        :returns:
        [10, 18,...]
        """
        x = [self.get_stat(i, "towerKills") for i in xrange(10)]
        return x 
    def items(self):
        pass

    def teamkills(self):
        pass