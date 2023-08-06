from wizlib.command_handler import CommandHandler
from .command import GillionsCommand


class GillionsHandler(CommandHandler):

    @classmethod
    def shell(self):
        try:
            super().shell(GillionsCommand)
        except Exception as e:
            print(e)
