from gillions.command import GillionsCommand

class NullCommand(GillionsCommand):

    name = 'null'

    def execute(self):
        return "Welcome to Gillions!"