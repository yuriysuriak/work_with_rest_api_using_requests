import requests

from entity.person import Person
from entity.planet import Planet
from starship import Starship


class StarWarsApi:
    def __init__(self):
        self.base_url = 'https://swapi.dev'
    def get_entity(self, entity, entity_id):
        url = f"{self.base_url}/api/{entity}/{entity_id}"
        reponse =  requests.get(url)
        if reponse.status_code == 200:
            return reponse.json()
        else:
            raise ValueError(f'Неможливо отримати дані у сутності {entity} з ідентифікатором {entity_id}')
    def get_person(self, person_id):
        person_dict = self.get_entity('people', person_id)
        return Person(person_dict)

    def get_plant(self, planet, planet_id):
        url = f"{self.base_url}/api/{planet}/{planet_id}"
        reponse = requests.get(url)
        if reponse.status_code == 200:
            return reponse.json()
    def get_planet(self, planet_id):
        planet_dict = self.get_plant('planets', planet_id)
        return Planet(planet_dict)

    def get_ship(self, ship, ship_id):
        url = f"{self.base_url}/api/{ship}/{ship_id}"
        reponse = requests.get(url)
        if reponse.status_code == 200:
            return reponse.json()
    def get_starship(self, starship_id):
        starship_dict = self.get_ship('starships', starship_id)
        return Starship(starship_dict)





