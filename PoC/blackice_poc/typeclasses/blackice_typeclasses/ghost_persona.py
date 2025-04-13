from blackice_poc.commands.blackice_commands.cmdsets.connection.ghost import GhostCmdSet
from typeclasses.blackice_typeclasses.persona import Persona

class GhostPersona(Persona):
    def at_cmdset_get(self, **kwargs):
        self.cmdset.clear()
        self.cmdset.add(GhostCmdSet(), persistent=True)

    def at_post_login(self):
        self.locks.add("cmd:all();perm(Player):false()")

    def at_post_puppet(self):
        """
        Called after the ghost shell is successfully puppeted.
        """
        self.msg("\n|g[SYS]|n Uplink established. You are now interfacing with the Ghost Shell.")
        self.msg("[SYS] Persona integrity check... OK.")
        self.execute_cmd("status")  # Immediately show TTL

