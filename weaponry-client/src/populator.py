import json
import requests

class InventoryPopulator:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def populate_initial_inventory(self):
        """
        sets up the MongoDB with inital values by making various rest-api
        calls for every weapon in the initial-inventory.json file
        """

        weapons_file = open('initial-inventory.json', "r")
        json_data = json.loads(weapons_file.read())
        weapons_file.close()

        weapons = json_data['weapons']
        for weapon in weapons:
            requests.post("http://" + self.ip_address + ":3000/Weapons", data=weapon)
