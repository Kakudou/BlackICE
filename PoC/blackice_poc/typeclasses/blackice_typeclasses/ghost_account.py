from blackice_poc.commands.blackice_commands.cmdsets.connection.ghost import GhostCmdSet
from typeclasses.accounts import Account as BaseAccount

class GhostAccount(BaseAccount):
    def at_cmdset_get(self, caller=None, current=None, **kwargs):
        self.cmdset.clear()
        self.cmdset.add(GhostCmdSet(), persistent=True)

    def at_post_login(self, session=None):
        self.locks.add("cmd:all();perm(Player):false()")
        self.db._character_storage = []
        self.db._playable_characters = []

