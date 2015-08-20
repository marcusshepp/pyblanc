## API Wrapper for League of Legends
#### Get the data you want, quickly.

######

######Example usage
```python

>>> from pyblanc import LeagueStat
>>> cls = LeagueStat(summoner='foo', api_key='bar')
>>> average_cs = cls.average_cs()
>>> print averge_cs
35.5 

>>> from pyblanc import LeagueTimelineFile
>>> cls = LeagueTimelineFile(summoner='bar', api_key='foo', path_to_data="path_str")
>>> cls.stats_to_file() # files are named "datetime.date.today().json"
>>> cls.timeline_cspermin() 
{"zeroToTen": 12, "tenToTwenty": 20, "twentyToThirty", 30}
```