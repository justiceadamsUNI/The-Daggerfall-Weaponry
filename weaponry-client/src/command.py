import requests
import json
import pprint
import time

class Command:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def report_and_wait(self, message):
        # Report status, wait while user reads it, and continue
        print(message)
        time.sleep(2)
        print()

    def check_response_for_error(self, response, error_message):
        if response.status_code != 200 or \
                (response.json() is not None and "Error" in str(response.json())):
            self.report_and_wait(error_message)
            return True
        return False

    def help_prompt(self):
        raise Exception("Implement method help_prompt()")

    def execute(self):
        raise Exception("Implement method execute()")


class Retrieve(Command):
    def execute(self):
        """
        Prompts the user for a weapon ID and deletes that weapon from the database
        """
        weapon_id = input("What is the ID of the weapon you wish to remove from the weaponry: ")

        response = requests.delete("http://" + self.ip_address + ":3000/Weapons/" + weapon_id)

        if self.check_response_for_error(response,
                                         "ERROR while removing weapon, did you enter the correct weapon ID? Taking"
                                         + " you back to the command menu"):
            return

        self.report_and_wait("Successfully removed weapon")

    def help_prompt(self):
        print("This command will remove a weapon from the armory (delete it from the DB). "
              + "All you must provide is the weapon ID \n")


class Store(Command):
    def execute(self):
        """
        Prompts the user for weapon values, then stores the weapon in the database
        via a rest API call.
        """
        weapon = {
            'name': input("Enter the name of the weapon you want to store: "),
            'damage': input("Enter the base damage of the weapon you want to store: "),
            'value': input("Enter the value of the weapon you want to store: "),
            'weight': input("Enter the weight of the weapon you want to store: "),
            'type': input("Enter the type of the weapon you want to store: ")
        }

        response = requests.post("http://" + self.ip_address + ":3000/Weapons", data=weapon)

        if self.check_response_for_error(response,
                                         "ERROR while storing weapon, did you enter all values correctly? Taking"
                                         + " you back to the command menu"):
            return

        self.report_and_wait("Successfully stored weapon: " + weapon['name'])

    def help_prompt(self):
        print("This command will store a weapons within the Daggerfall armory. "
              + "You must provide the following values when prompted: \n"
              + "  -Weapon name \n"
              + "  -Weapon damage \n"
              + "  -Weapon value \n"
              + "  -Weapon weight \n"
              + "  -Weapon type \n")


class Inspect(Command):
    def execute(self):
        """
        Prints the stats of whichever weapon is specified via the weapon ID
        """
        weapon_id = input("What is the ID of the weapon you wish to inspect: ")
        response = requests.get("http://" + self.ip_address + ":3000/Weapons/" + weapon_id)

        if self.check_response_for_error(response,
                                         "ERROR while inspecting weapon, did you enter the correct weapon ID? Taking"
                                         + " you back to the command menu"):
            return

        pprint.pprint(response.json())
        print()

    def help_prompt(self):
        print("This command will inspect a weapons within the Daggerfall armory "
              + "(List its' attributes). You only need to provide the weapon ID. \n")


class Modify(Command):
    def execute(self):
        """
        Prompts the user for updated weapon values, then stores the updated weapon in
        the database.
        """
        weapon_id = input("Enter the id of the weapon you want to modify: ")

        response = requests.get("http://" + self.ip_address + ":3000/Weapons/" + weapon_id)

        if self.check_response_for_error(response,
                                         "ERROR while modifying weapon, did you enter the correct weapon ID? Taking"
                                         + " you back to the command menu"):
            return

        print(" --- CURRENT WEAPON STATS --- ")
        pprint.pprint(response.json())

        weapon = {
            'name': input("Enter the updated name of the weapon: "),
            'damage': input("Enter the updated base damage of the weapon: "),
            'value': input("Enter the updated value of the weapon: "),
            'weight': input("Enter the updated weight of the weapon: "),
            'type': input("Enter the updated type of the weapon: ")
        }

        response = requests.put("http://" + self.ip_address + ":3000/Weapons/" + weapon_id, data=weapon)

        if response.status_code != 200:
            print("ERROR while modifying weapon, did you enter the correct weapon ID? Taking"
                  + " you back to the command menu")
            return

        self.report_and_wait("Successfully modified weapon: " + weapon['name'])

    def help_prompt(self):
        print("This command will update a weapons within the Daggerfall armory. "
              + "You must provide the following values when prompted: \n"
              + "  -Weapon ID \n"
              + "  -Weapon name \n"
              + "  -Weapon damage \n"
              + "  -Weapon value \n"
              + "  -Weapon weight \n"
              + "  -Weapon type \n")


class List(Command):
    def execute(self):
        """
        Print all weapons received from API to standard out.
        """
        response = requests.get("http://" + self.ip_address + ":3000/Weapons")

        if self.check_response_for_error(response,
                                         "ERROR retrieving weapons, did you enter the correct IP address? Taking"
                                         + " you back to the command menu"):
            return

        pprint.pprint(response.json())
        print()

    def help_prompt(self):
        print("This command will list all weapons in the Daggerfall armory. "
              + "You don't need to give us any more information to see all our housed "
              + "weapons! \n")


class Quit(Command):
    def execute(self):
        """
        Exits the client application
        """
        print("See you around Tamriel, traveler!")
        exit(0)

    def help_prompt(self):
        print("This command will exit the client program when executed \n")
