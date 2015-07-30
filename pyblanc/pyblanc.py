import os
import json
import math
import urllib2 as urll
from datetime import date

import numpy as np

import util as util_ez


class BackEnd(object):
    """
    Do NOT instantiate this class itself.
    Only instantiate League's subclasses.
    """

    api_key = ""
    summoner = 0

    def __init__(self, api_key, summoner):
        """ Initialize obj with debug = False """
        self.api_key = api_key
        self.summoner = summoner
        self.request_data = self.match_history_request()

    def __unicode__(self):
        """ Useful for displaying `LeagueStats` as on obj. """
        return u"PyBlanc object instance. Summoner: {}".format(self.summoner)

    def get_request(self, url):
        url += "?api_key={0}".format(self.api_key)
        request = urll.urlopen(url)
        parsed = json.loads(request.read())
        return parsed

    def match_history_request(self):
        """ Makes a request to League servers and returns parsed JSON data."""
        url = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/{0}".format(self.summoner)
        return self.get_request(url)

    def champion_list(self):
        url = "https://na.api.pvp.net/api/lol/na/v1.2/champion"
        return self.get_request(url)
    

class League(BackEnd):
    """ Security layer. """

    def __init__(self, *args, **kwargs):
        super(League, self).__init__(*args, **kwargs)
        self.SETTINGS = {}
        self.SETTINGS['champs'] = util_ez.champ_strings()
        self.SETTINGS['champ_ids'] = util_ez.champ_string_int()


class LeagueFile(League):
    """
    Class for reading/writing League stats to/from files.

    parameters:
    path_to_data -> type: str, description: absolute path containing JSON
    """

    def __init__(self, path_to_data):
        super(League, self).__init__()
        self.path_to_data = str(path_to_data)
    
    def stats_from_file(self):
        """ Returns dict of data from a file. """
        path = r'{}'.format(self.path_to_data)  
        for dir_entry in os.listdir(path):
            dir_entry_path = os.path.join(path, dir_entry)
            if os.path.isfile(dir_entry_path):
                with open(dir_entry_path) as my_file:
                    data = json.load(my_file)
        if data:
            return data['matches'] # rid myself of this layer
        return None
    
    def stats_to_file(self, relative_path, file_name):
        """ Writes match history to a file in a given location. """
        parsed, file_name = self.match_history_request(), date.today()
        complete_path = os.path.abspath("{0}{1}.json".format(relative_path, file_name))
        if os.path.isfile(complete_path):
            file_name = "{}-duplicate".format(date.today())
            complete_path = os.path.abspath("{0}{1}.json".format(relative_path, file_name))
        with open(complete_path, "w") as f:
            f.write(json.dumps(parsed))
            f.close()
        return str(complete_path)
    

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
        parsed = self.match_history_request()
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
        parsed = self.match_history_request()
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
        parsed = self.request_data
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
        [False, True,...]
        """
        x = [self.get_stat(i, "goldEarned") for i in xrange(10)]
        return x
        
    def longest_killing_spree(self):
        """
        :returns:
        []
        """
        x = [self.get_stat(i, "largestKillingSpree") for i in xrange(10)]
        return x

    def largest_multikill(self):
        """
        :returns:
        []
        """
        x = [self.get_stat(i, "largestMultiKill") for i in xrange(10)]
        return x
    
    def wards_placed(self):
        """
        :returns:
        []
        """
        x = [self.get_stat(i, "wardsPlaced") for i in xrange(10)]
        return x
    
    def items(self):
        """
        :returns:
        []
        """
        x = [self.get_stat(i, "wardsPlaced") for i in xrange(10)]
        return x

    def teamkills(self):
        """
        :returns:
        []
        """
        x = [self.get_stat(i, "wardsPlaced") for i in xrange(10)]
        return x


class LeagueTimelineFile(LeagueFile):
    """
    * READS FROM FILE ONLY *
    Handles the `timeline` dict.
    Available methods:
        timeline_request
        timeline_file
        timeline_lanes
        timeline_cspermin
        timeline_cspermin_bytime
        timeline_xppermin
    """

    def timeline_request(self, game_number, stat_name, *args, **kwargs):
        """ Returns the `timeline` data, type: dict. """
        parsed = self.match_history_request()
        return parsed['matches'][game_number]['participants'][0]['timeline'][stat_name]    

    def timeline_file(self, stat_name, *args, **kwargs):
        """ Returns the `timeline` data for a given stat, type: dict. """
        matches = self.stats_from_file("{}".format(self.path_to_data))
        timeline = {}
        for n in range(len(matches)):
            timeline[n] = matches[n]['participants'][0]['timeline'][stat_name]
        return timeline
    
    def timeline_lanes(self):
        """ Returns game lane value for `game_number`.  """
        lanes = self.timeline_file("lane")
        for g, l in lanes.iteritems():
            lanes[g] = str(l) # from unicode to str
        return lanes # {game_num: 'lane'}
      
    def timeline_cspermin(self, time_value=None):
        """ 
        cspermin from zero to ten min. 
        `time_value` can be: 
        zeroToTen
        tenToTwenty
        twentyToThirty
        """
        a, pika = self.timeline_file("creepsPerMinDeltas"), {}
        if time_value:
            for i, j in a.iteritems():
                for num in range(len(i)):
                    pika[i] = a[i][time_value]
                    return pika # {game_num: cs}
        return a

    def timeline_xppermin(self):
        dict_of_values = self.timeline_file("xpPerMinDeltas")
        return dict_of_values


class LeagueStatFile(LeagueFile):

    def __unicode__(self):
        return "Stats file reader/writter."

