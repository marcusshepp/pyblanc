## API Wrapper for League of Legends
#### Get the data you want, quickly.

######Example usage
```python

>>> from pyblanc import LeagueStat
>>> ls = LeagueStat(summoner='foo')
>>> average_cs = ls.average_cs()
>>> averge_cs
35.5 
>>> ls.kills()
[12, 5, 7, 15, 9, 9, 13, 0, 11, 3]
>>> from pyblanc import LeagueTimelineFile
>>> lf = LeagueTimelineFile(summoner='bar')
>>> lf.stats_to_file() # files are named "datetime.date.today().json"
>>> lf.timeline_cspermin() 
{"zeroToTen": 12, "tenToTwenty": 20, "twentyToThirty", 30}
```
