import os
import json
import math
import requests
import requests_cache


requests_cache.install_cache(
    'stat_cache', backend="memory", expire_after=3600) #one hour


class BackEnd(object):
    """
    Do NOT instantiate this class itself.
    Only instantiate League's subclasses.
    """

    def __init__(self, api_key=None, summoner=None, from_file=False, path_to_data="Undefined"):
        self.api_key = api_key
        self.summoner = summoner
        self.from_file = from_file
        self.path_to_data = path_to_data

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
        url = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/{0}".format(self.summoner)
        url += "?api_key={0}".format(self.api_key)
        request = requests.get(url)
        parsed = request.json()
        return parsed
