from unittest import TestCase

from wizlib.command_handler import CommandHandler
from gillions.command import GillionsCommand


class TestCommandSync(TestCase):

    def test_from_handler(self):
        r, s = CommandHandler(GillionsCommand).handle()
        self.assertEqual(r, 'Welcome to Gillions!')
