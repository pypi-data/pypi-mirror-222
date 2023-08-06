from dataclasses import dataclass

from wizlib.command_handler import Command
from wizlib.config_machine import ConfigMachine


@dataclass
class GillionsCommand(ConfigMachine, Command):

    app_name = 'gillions'
    default = 'null'
