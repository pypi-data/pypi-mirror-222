from wizlib.command_handler import CommandHandler
from .command import PolyRepoCommand


class PolyRepoHandler(CommandHandler):

    @classmethod
    def shell(self):
        super().shell(PolyRepoCommand)
