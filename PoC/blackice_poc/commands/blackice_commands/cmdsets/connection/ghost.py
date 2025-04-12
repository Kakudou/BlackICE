from evennia import CmdSet
from commands.blackice_commands.connection.cmd_ghost import CmdGhostStatus
from evennia.utils.logger import log_info

class GhostCmdSet(CmdSet):
    key = "GhostCmdSet"
    priority = 999  # Ensure it's on top of the stack

    def at_cmdset_creation(self):
        self.add(CmdGhostStatus())

