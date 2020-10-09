team = [
    (1, {"name": "Zelimkhan Bakaev", "rating": "75", "pos": "CAM", "pac": "86", "sho": "70", "pas": "71"}),
    (2, {"name": "Mário Figueira Fernandes", "rating": "82", "pos": "RWB", "pac": "82", "sho": "61", "pas": "74"}),
    (3, {"name": "Guilherme Alvim Marinato", "rating": "78", "pos": "GK", "pac": "82", "sho": "73", "pas": "72"}),
    (4, {"name": "Fedor Smolov ", "rating": "76", "pos": "ST", "pac": "82", "sho": "75", "pas": "71"}),
    (5, {"name": "Georgiy Dzhikiya", "rating": "77", "pos": "CB", "pac": "82", "sho": "53", "pas": "61"}),
    (6, {"name": "Alexandr Kokorin", "rating": "78", "pos": "ST", "pac": "81", "sho": "77", "pas": "72"}),
    (7, {"name": "Alexandr Golovin", "rating": "79", "pos": "CM", "pac": "80", "sho": "72", "pas": "79"}),
    (8, {"name": "Denis Cheryshev", "rating": "77", "pos": "LM", "pac": "79", "sho": "76", "pas": "76"}),
    (9, {"name": "Georgiy Schennikov", "rating": "75", "pos": "LWB", "pac": "79", "sho": "54", "pas": "69"}),
    (10, {"name": "Igor Akinfeev", "rating": "80", "pos": "GK", "pac": "77", "sho": "72", "pas": "78"}),
    (11, {"name": "Roman Zobnin", "rating": "78", "pos": "CDM", "pac": "76", "sho": "62", "pas": "76"})
]

team_2 = {"name": "", "rating": "", "pos": "", "pac": "", "sho": "", "pas": ""}

for i in team_2.keys():
    result = []
    for j in range(len(team)):
        result.append(team[j][1].get(i))
    team_2.update({i: result})

print(team_2)
