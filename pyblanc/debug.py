import pyblanc


marcusshep = 42008349
api_key = "8a9d2c2d-f00d-406b-87b1-810c2312a1ae"

pb = pyblanc.LeagueStat(api_key, marcusshep)
print pb.__unicode__()
print pb.all_minions_killed()