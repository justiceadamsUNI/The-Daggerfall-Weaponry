import requests
import command
import sys
import os

# ToDo: Plug in ip address from docker build
# ToDo: Check IP address to ensure validity. Possibly with request library?
# ToDo: do work for each command


class Runner:
    COMMAND_INFO = "Emperor Septim has granted you access to the following commands: \n"\
                   + "  -Retrieve (r) \n" \
                   + "  -Store (s) \n" \
                   + "  -Inspect (i) \n" \
                   + "  -Modify (m) \n" \
                   + "  -List (l) \n" \
                   + "  -Quit (q) \n" \
                   + "If you wish to learn more about any of the commands available, please type <COMMAND> -help\n"

    def print_welcome(self):
        """
        Prints the welcome information to stdout for the user to see upon startup
        """

        print("*** Developed by Justice Adams ***")

        print("""
               _,---,_
             /'_______`
            (/'       `\|___________----------------------,
             \#########||______                          /'
              ^^^^^^^^^||      ----------_____          /'
                        \                      ------_/' \n""")

        print("Welcome to the Daggerfall Weaponry, traveler! Here you may store and retrieve any weapons within the "
              "Daggerfall armory. " + self.COMMAND_INFO)

    def get_command(self, ip_address):
        """
        Prompts the user to enter a command, validates the input, and returns an instantiation of the
        appropriate Command class. Also determines if the user asked for help with the '-help' suffix
        and returns a boolean variable accordingly.
        :return A tuple containing the command object, and a boolean value
        """

        commands = ["r", "retrieve", "s", "store", "inspect", "i", "modify", "m", "list", "l", "quit", "q"]
        response = input("Enter your command: ").lower()

        # If response is invalid, keep trying until a valid command is entered
        while response.split("-help")[0].strip() not in commands:
            print("\nCommand not recognized. " + self.COMMAND_INFO)

            response = input("Enter your command: ").lower()

        help_needed = response.endswith("-help")
        return {
            "r": command.Retrieve(ip_address),
            "s": command.Store(ip_address),
            "i": command.Inspect(ip_address),
            "m": command.Modify(ip_address),
            "l": command.List(ip_address),
            "q": command.Quit(ip_address)
        }[response[0]], help_needed

    def check_ip(self, ip_address):
        if os.system("ping -c 1 " + ip_address + "> /dev/null 2>&1") != 0:
            raise Exception("ERROR: couldn't communicate with IP address - " + ip_address)

    def run(self, ip_address):
        """
        Method to run the client application code
        """
        self.check_ip(ip_address)
        self.print_welcome()
        while True:
            user_command, help_needed = self.get_command(ip_address)
            user_command.help_prompt() if help_needed else user_command.execute()
            print(self.COMMAND_INFO)


# Start the client app
if len(sys.argv) == 1:
    raise Exception("ERROR: please provide an IP address")

Runner().run(str(sys.argv[1]))
