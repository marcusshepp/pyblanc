import os

from pyblanc import LeagueStat


marcusshep = 42008349
api_key = "8a9d2c2d-f00d-406b-87b1-810c2312a1ae"
path_to_data = "../data"

pb = LeagueStat(from_file=True, path_to_data=path_to_data)
print pb.__unicode__()
print pb.masteries()
