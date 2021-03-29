import requests

hero_name = ['Hulk', 'Thanos', 'Captain America']
hero_list = []

for name in hero_name:
  url = "https://superheroapi.com/api/2619421814940190/search/" + name
  resp = requests.get("https://superheroapi.com/api/2619421814940190/search/" + name)
  superhero = resp.json()

  for hero_name in superhero:
    hero_name = superhero['results'][0]["name"]
    hero_intelligence = superhero['results'][0]["powerstats"]["intelligence"]
  all_heroes = [hero_name, int(hero_intelligence)]
  hero_list.append(all_heroes)
most_intelligence = max(hero_list, key=lambda item: item[1])
print(f'Cамый умный супергерой - {most_intelligence[0]}')