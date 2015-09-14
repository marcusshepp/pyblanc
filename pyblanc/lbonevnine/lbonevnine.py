"""
This document gets its name from a character in the game named Leblanc.
When I play her I feel it's a battle of me vs all nine other players in the game.
Much like when I program. Marcus vs Problem.
"""
import json
import math
import requests
import requests_cache

from settings import ( 
    API_KEY,
    SUMMONER_INFO_BY_NAME,
    MATCH_HISTORY,
)


requests_cache.install_cache(
    'stat_cache', backend="memory", expire_after=3600) #one hour

def summoner_id(name):
    """ Doesn't need instance of class. """
    url = SUMMONER_INFO_BY_NAME + "{0}?api_key={1}".format(name, API_KEY)
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()[name][u"id"]


class BackEnd(object):
    """
    Do NOT instantiate this class itself.
    Only instantiate it's subclasses.
    """

    def __init__(self, api_key=None, summoner=None, from_file=False, path_to_data="Undefined"):
        """ Initialize obj with debug = False """
        self.api_key = api_key
        self.from_file = from_file
        self.path_to_data = path_to_data
        if summoner:
            self.summoner = summoner_id(summoner)

    def __unicode__(self):
        """ Useful for displaying `LeagueStats` as on obj. """
        return u"PyBlanc object instance. Summoner: {}".format(self.summoner)

    def get_data(self):
        """ 
        Makes a request to League servers and returns parsed JSON data.
        If called within same hour, retrieves data from memory cache.
        """
        if self.from_file:
            """ Returns dict of data from a file. """
            path = r'{}'.format(self.path_to_data)  
            for dir_entry in os.listdir(path):
                dir_entry_path = os.path.join(path, dir_entry)
                if os.path.isfile(dir_entry_path):
                    with open(dir_entry_path) as my_file:
                        data = json.load(my_file)
            if data:
                return data
            raise Exception
        url = "{0}{1}".format(MATCH_HISTORY, self.summoner)
        url += "?api_key={0}".format(API_KEY)
        request = requests.get(url)
        parsed = request.json()
        return parsed
