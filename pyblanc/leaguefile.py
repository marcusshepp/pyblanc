import os
import json

from .pyblanc import League


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
        parsed, file_name = self.get_data(), date.today()
        complete_path = os.path.abspath("{0}{1}.json".format(relative_path, file_name))
        if os.path.isfile(complete_path):
            file_name = "{}-duplicate".format(date.today())
            complete_path = os.path.abspath("{0}{1}.json".format(relative_path, file_name))
        with open(complete_path, "w") as f:
            f.write(json.dumps(parsed))
            f.close()
        return str(complete_path)


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