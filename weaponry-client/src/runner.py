import requests
import command

# ToDo: create bash script for nodejs server start
# ToDo: intro with ascii art
# ToDo: Plug in ip address from docker build
# ToDo: Check IP address to ensure validity. Possibly with request library?
# ToDo: do work for each command


class Runner:
    def print_welcome(self):
        print("Welcome to the Daggerfall Armory! Here you may store and retrieve any weapons within the "
              "Daggerfall armory. Emperor Septim has granted you access to the following commands: \n"
              "  -Retrieve (r) \n"
              "  -Store (s) \n"
              "  -Inspect (i) \n"
              "  -Modify (m) \n"
              "  -Quit (q) \n"
              "If you wish to learn more about any of the commands available, please type <COMMAND> -help")

    def get_command(self):
        commands = ["r", "retrieve", "s", "store", "inspect", "i", "modify", "m", "quit", "q"]

        response = input("Enter your command: ")
        while response.lower() not in commands:
            print("Command not recognized. Emperor Septim has granted you access to the following commands: \n" 
                  "  -Retrieve (r) \n"
                  "  -Store (s) \n"
                  "  -Inspect (i) \n"
                  "  -Modify (m) \n"
                  "  -Quit (q) \n")

            response = input("Enter your command: ")

        return {
            "r": command.Retrieve(),
            "s": command.Store(),
            "i": command.Inspect(),
            "m": command.Modify(),
            "q": command.Quit()
        }[response[0]]

    def run(self):
        while true:
            user_command = get_command()
            user_command.execute()


# Start the client app
Runner().run()
