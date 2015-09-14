from datetime import datetime

from lbonevnine.settings import ACCOUNTS
from leaguefile import LeagueFile

def pull_data():
    for acc in ACCOUNTS:
        l = LeagueFile(summoner=acc)
        file_name = "{0}-{1}".format(acc, datetime.now())
        l.stats_to_file(relative_path="../data", file_name=file_name)
    return