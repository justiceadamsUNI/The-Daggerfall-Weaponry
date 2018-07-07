import requests
import command

# ToDo: Plug in ip address from docker build
# ToDo: Check IP address to ensure validity. Possibly with request library?
# ToDo: do work for each command

class Runner:
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
                        \                      ------_/' """)

        print("Welcome to the Daggerfall Weaponry, traveler! Here you may store and retrieve any weapons within the "
              "Daggerfall armory. Emperor Septim has granted you access to the following commands: \n"
              "  -Retrieve (r) \n"
              "  -Store (s) \n"
              "  -Inspect (i) \n"
              "  -Modify (m) \n"
              "  -List (l) \n"
              "  -Quit (q) \n"
              "If you wish to learn more about any of the commands available, please type <COMMAND> -help\n")

    def get_command(self):
        """
        Prompts the user to enter a command, validates the input, and returns an instantiation of the
        appropriate Command class. Also determines if the user asked for help with the '-help' suffix
        and returns a boolean variable accordingly.
        :return A tuple containing the command object, and a boolean value
        """

        commands = ["r", "retrieve", "s", "store", "inspect", "i", "modify", "m", "quit", "q"]
        response = input("Enter your command: ").lower()

        # If response is invalid, keep trying until a valid command is entered
        while response.split("-help")[0].strip() not in commands:
            print("\nCommand not recognized. Emperor Septim has granted you access to the following commands: \n" 
                  "  -Retrieve (r) \n"
                  "  -Store (s) \n"
                  "  -Inspect (i) \n"
                  "  -Modify (m) \n"
                  "  -List (l) \n"
                  "  -Quit (q) \n"
                  "If you wish to learn more about any of the commands available, please type <COMMAND> -help \n")

            response = input("Enter your command: ").lower()

        help_needed = response.endswith("-help")
        return {
            "r": command.Retrieve(),
            "s": command.Store(),
            "i": command.Inspect(),
            "m": command.Modify(),
            "l": command.List(),
            "q": command.Quit()
        }[response[0]], help_needed

    def run(self):
        """
        Method to run the client application code
        """
        self.print_welcome()
        while True:
            user_command, help_needed = self.get_command()
            user_command.help_prompt() if help_needed else user_command.execute()


# Start the client app
Runner().run()
