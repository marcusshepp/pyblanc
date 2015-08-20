"""
This document gets its name from a character in the game named Leblanc.
When I play her I feel it's a battle of me vs all nine other players in the game.
Much like when I program. Marcus vs Problem.
"""
import json
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

    def __init__(self, summoner):
        """ Initialize obj with debug = False """
        self.api_key = API_KEY
        self.summoner = summoner

    def __unicode__(self):
        """ Useful for displaying `LeagueStats` as on obj. """
        return u"PyBlanc object instance. Summoner: {}".format(self.summoner)

    def get_data(self):
        """ 
        Makes a request to League servers and returns parsed JSON data.
        If called within same hour, retrieves data from memory cache.
        """
        url = MATCH_HISTORY + "{0}".format(
            summoner_id(self.summoner))
        url += "?api_key={0}".format(API_KEY)
        request = requests.get(url)
        parsed = request.json()
        return parsed
