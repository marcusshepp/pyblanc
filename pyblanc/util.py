""" champion_names + ids """


def champ_strings():
	# returns: ['Aatrox', ...]
	return [x for x in CHAMPION_STRINGS]

def champ_string_int():
	# returns: {"Aatrox": 266, ...}
	return dict((name, eval(name)) for name in CHAMPION_STRINGS)

def champion_id_to_str(given_id):
	for name, value in champ_string_int().iteritems():
		if value == given_id:
			return name

Aatrox = 266
Ahri = 103
Akali = 84
Alistar = 12
Amumu = 32
Anivia = 34
Annie = 1
Ashe = 22
Azir = 268
Bard = 432
Blitzcrank = 53
Brand = 63
Braum = 201
Caitlyn = 51
Cassiopeia = 69
ChoGath = 31
Corki = 42
Darius = 122
Diana = 131
DrMundo = 36
Draven = 119
Ekko = 245
Elise = 60
Evelynn = 28
Ezreal = 81
Fiddlesticks = 9
Fiora = 114
Fizz = 105
Galio = 3
Gangplank = 41
Garen = 86
Gnar = 150
Gragas = 79
Graves = 104
Hecarim = 120
Heimerdinger = 74
Irelia = 39
Janna = 40
JarvanIV = 59
Jax = 24
Jayce = 126
Jinx = 222
Kalista = 429
Karma = 43
Karthus = 30
Kassadin = 38
Katarina = 55
Kayle = 10
Kennen = 85
KhaZix = 121
KogMaw = 96
LeBlanc = 7
LeeSin = 64
Leona = 89
Lissandra = 127
Lucian = 236
Lulu = 117
Lux = 99
Malphite = 54
Malzahar = 90
Maokai = 57
MasterYi = 11
MissFortune = 21
Mordekaiser = 82
Morgana = 25
Nami = 267
Nasus = 75
Nautilus = 111
Nidalee = 76
Nocturne = 56
Nunu = 20
Olaf = 2
Orianna = 61
Pantheon = 80
Poppy = 78
Quinn = 133
Rammus = 33
RekSai = 421
Renekton = 58
Rengar = 107
Riven = 92
Rumble = 68
Ryze = 13
Sejuani = 113
Shaco = 35
Shen = 98
Shyvana = 102
Singed = 27
Sion = 14
Sivir = 15
Skarner = 72
Sona = 37
Soraka = 16
Swain = 50
Syndra = 134
Talon = 91
Taric = 44
Teemo = 17
Thresh = 412
Tristana = 18
Trundle = 48
Tryndamere = 23
TwistedFate = 4
Twitch = 29
Udyr = 77
Urgot = 6
Varus = 110
Vayne = 67
Veigar = 45
VelKoz = 161
Vi = 254
Viktor = 112
Vladimir = 8
Volibear = 106
Warwick = 19
Wukong = 62
Xerath = 101
XinZhao = 5
Yasuo = 157
Yorick = 83
Zac = 154
Zed = 238
Ziggs = 115
Zilean = 26
Zyra = 143

CHAMPION_BASE = [

	(Aatrox, "Aatrox"),
	(Ahri, "Ahri"),
	(Akali, "Akali"),
	(Alistar, "Alistar"),
	(Amumu, "Amumu"),
	(Anivia, "Anivia"),
	(Annie, "Annie"),
	(Ashe, "Ashe"),
	(Azir,"Azir"),
	(Bard, "Bard"),
	(Blitzcrank, "Blitzcrank"),
	(Brand, "Brand"),
	(Braum, "Braum"),
	(Caitlyn, "Caitlyn"),
	(Cassiopeia, "Cassiopeia"),
	(ChoGath, "Cho'Gath"),
	(Corki, "Corki"),
	(Darius, "Darius"),
	(Diana, "Diana"),
	(DrMundo, "Dr. Mundo"),
	(Draven, "Draven"),
	(Ekko, "Ekko"),
	(Elise, "Elise"),
	(Evelynn, "Evelynn"),
	(Ezreal, "Ezreal"),
	(Fiddlesticks, "Fiddlesticks"),
	(Fiora, "Fiora"),
	(Fizz, "Fizz"),
	(Galio, "Galio"),
	(Gangplank, "Gangplank"),
	(Garen, "Garen"),
	(Gnar, "Gnar"),
	(Gragas, "Gragas"),
	(Graves, "Graves"),
	(Hecarim, "Hecarim"),
	(Heimerdinger, "Heimerdinger"),
	(Irelia, "Irelia"),
	(Janna, "Janna"),
	(JarvanIV, "Jarvan IV"),
	(Jax, "Jax"),
	(Jayce, "Jayce"),
	(Jinx, "Jinx"),
	(Kalista, "Kalista"),
	(Karma, "Karma"),
	(Karthus, "Karthus"),
	(Kassadin, "Kassadin"),
	(Katarina, "Katarina"),
	(Kayle, "Kayle"),
	(Kennen, "Kennen"),
	(KhaZix, "Kha'Zix"),
	(KogMaw, "Kog'Maw"),
	(LeBlanc, "LeBlanc"),
	(LeeSin, "Lee Sin"),
	(Leona, "Leona"),
	(Lissandra, "Lissandra"),
	(Lucian, "Lucian"),
	(Lulu, "Lulu"),
	(Lux, "Lux"),
	(Malphite, "Malphite"),
	(Malzahar, "Malzahar"),
	(Maokai, "Maokai"),
	(MasterYi, "Master Yi"),
	(MissFortune, "Miss Fortune"),
	(Mordekaiser, "Mordekaiser"),
	(Morgana, "Morgana"),
	(Nami, "Nami"),
	(Nasus, "Nasus"),
	(Nautilus, "Nautilus"),
	(Nidalee, "Nidalee"),
	(Nocturne, "Nocturne"),
	(Nunu, "Nunu"),
	(Olaf, "Olaf"),
	(Orianna, "Orianna"),
	(Pantheon, "Pantheon"),
	(Poppy, "Poppy"),
	(Quinn, "Quinn"),
	(Rammus, "Rammus"),
	(RekSai, "Rek'Sai"),
	(Renekton, "Renekton"),
	(Rengar, "Rengar"),
	(Riven, "Riven"),
	(Rumble, "Rumble"),
	(Ryze, "Ryze"),
	(Sejuani, "Sejuani"),
	(Shaco, "Shaco"),
	(Shen, "Shen"),
	(Shyvana, "Shyvana"),
	(Singed, "Singed"),
	(Sion, "Sion"),
	(Sivir, "Sivir"),
	(Skarner, "Skarner"),
	(Sona, "Sona"),
	(Soraka, "Soraka"),
	(Swain, "Swain"),
	(Syndra, "Syndra"),
	(Talon, "Talon"),
	(Taric, "Taric"),
	(Teemo, "Teemo"),
	(Thresh, "Thresh"),
	(Tristana, "Tristana"),
	(Trundle, "Trundle"),
	(Tryndamere, "Tryndamere"),
	(TwistedFate, "Twisted Fate"),
	(Twitch, "Twitch"),
	(Udyr, "Udyr"),
	(Urgot, "Urgot"),
	(Varus, "Varus"),
	(Vayne, "Vayne"),
	(Veigar, "Veigar"),
	(VelKoz, "Vel'Koz"),
	(Vi, "Vi"),
	(Viktor, "Viktor"),
	(Vladimir, "Vladimir"),
	(Volibear, "Volibear"),
	(Warwick, "Warwick"),
	(Wukong, "Wukong"),
	(Xerath, "Xerath"),
	(XinZhao, "Xin Zhao"),
	(Yasuo, "Yasuo"),
	(Yorick, "Yorick"),
	(Zac, "Zac"),
	(Zed, "Zed"),
	(Ziggs, "Ziggs"),
	(Zilean, "Zilean"),
	(Zyra, "Zyra"),
]

CHAMPION_STRINGS =[
	"Aatrox",
	"Ahri",
	"Akali",
	"Alistar",
	"Amumu",
	"Anivia",
	"Annie",
	"Ashe",
	"Azir",
	"Bard",
	"Blitzcrank",
	"Brand",
	"Braum",
	"Caitlyn",
	"Cassiopeia",
	"ChoGath",
	"Corki",
	"Darius",
	"Diana",
	"DrMundo",
	"Draven",
	"Ekko",
	"Elise",
	"Evelynn",
	"Ezreal",
	"Fiddlesticks",
	"Fiora",
	"Fizz",
	"Galio",
	"Gangplank",
	"Garen",
	"Gnar",
	"Gragas",
	"Graves",
	"Hecarim",
	"Heimerdinger",
	"Irelia",
	"Janna",
	"JarvanIV",
	"Jax",
	"Jayce",
	"Jinx",
	"Kalista",
	"Karma",
	"Karthus",
	"Kassadin",
	"Katarina",
	"Kayle",
	"Kennen",
	"KhaZix",
	"KogMaw",
	"LeBlanc",
	"LeeSin",
	"Leona",
	"Lissandra",
	"Lucian",
	"Lulu",
	"Lux",
	"Malphite",
	"Malzahar",
	"Maokai",
	"MasterYi",
	"MissFortune",
	"Mordekaiser",
	"Morgana",
	"Nami",
	"Nasus",
	"Nautilus",
	"Nidalee",
	"Nocturne",
	"Nunu",
	"Olaf",
	"Orianna",
	"Pantheon",
	"Poppy",
	"Quinn",
	"Rammus",
	"RekSai",
	"Renekton",
	"Rengar",
	"Riven",
	"Rumble",
	"Ryze",
	"Sejuani",
	"Shaco",
	"Shen",
	"Shyvana",
	"Singed",
	"Sion",
	"Sivir",
	"Skarner",
	"Sona",
	"Soraka",
	"Swain",
	"Syndra",
	"Talon",
	"Taric",
	"Teemo",
	"Thresh",
	"Tristana",
	"Trundle",
	"Tryndamere",
	"TwistedFate",
	"Twitch",
	"Udyr",
	"Urgot",
	"Varus",
	"Vayne",
	"Veigar",
	"VelKoz",
	"Vi",
	"Viktor",
	"Vladimir",
	"Volibear",
	"Warwick",
	"Wukong",
	"Xerath",
	"XinZhao",
	"Yasuo",
	"Yorick",
	"Zac",
	"Zed",
	"Ziggs",
	"Zilean",
	"Zyra",
]