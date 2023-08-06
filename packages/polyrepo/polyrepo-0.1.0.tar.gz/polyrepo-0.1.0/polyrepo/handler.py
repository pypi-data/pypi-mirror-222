from wizlib.command_handler import CommandHandler
from .command import PolyRepoCommand


class PolyRepoHandler(CommandHandler):

    @classmethod
    def shell(self):
        try:
            super().shell(PolyRepoCommand)
        except Exception as e:
            raise (e)
