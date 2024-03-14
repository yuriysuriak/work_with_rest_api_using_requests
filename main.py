
from star_wars_api import StarWarsApi
api_client = StarWarsApi()
person = api_client.get_person(1)
print(f"Person name: {person.name}")
print(f"Person skin color:{person.skin_color}")


planet = api_client.get_planet(3)
print(f"planet name {planet.name}")


starship = api_client.get_starship(9)
print(f'starship name: {starship.name}')

