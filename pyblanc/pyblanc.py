from __future__ import division

import os
import math
import operator
from datetime import date

import numpy as np

from lbonevnine.lbonevnine import BackEnd
import util as util_ez


class League(BackEnd):
    """ Security layer. """

    def __init__(self, *args, **kwargs):
        super(League, self).__init__(*args, **kwargs)
        self.SETTINGS = {}
        self.champs = util_ez.champ_strings()
        self.champ_ids = util_ez.champ_string_int()
    

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
        scores = [self.get_stat(int(i), "minionsKilled") for i in xrange(10)]
        return scores

    def average_cs(self):
        """ Returns the average creep score for the last ten games. """
        total_creep_count = 0
        total = [self.get_stat(int(i), "minionsKilled") for i in xrange(10)]
        for j in xrange(10):
            total_creep_count += total[j]
        return total_creep_count / 10

    def winsandloses(self):
        """ Returns wins and loses. """ 
        wl = [self.get_stat(x, "winner") for x in xrange(10)]
        return wl

    def winoverten(self):
        """ Returns the win/lose ratio. """
        num_of_wins = sum(self.winsandloses())
        return num_of_wins/10
    
    def get_champion_id(self, game_number):
        parsed = self.get_data()
        return parsed['matches'][game_number]['participants'][0]['championId']
    
    def all_champions(self):
        """
        :returns:
        ['Annie', 'Nidalee', ...]
        """
        container = [self.get_champion_id(i) for i in xrange(10)]
        container = [util_ez.champion_id_to_str(container[i]) for i in xrange(10)]
        return container

    def get_masteries(self, game_number):
        """ Returns masteries. """
        parsed = self.get_data()
        return parsed['matches'][game_number]['participants'][0]["masteries"]

    def masteries(self):
        print len(self.get_masteries(0))
        x = [[(self.get_masteries(i))] for i in xrange(10)]
        return x

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
