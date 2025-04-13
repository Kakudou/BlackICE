from evennia import CmdSet
from evennia.commands.default.account import CmdQuit
from evennia.commands.default.general import CmdLook
from evennia.commands.default.help import CmdHelp
from commands.blackice_commands.connection.cmd_ghost import CmdGhostStatus

class GhostCmdSet(CmdSet):
    key = "GhostCmdSet"
    priority = 999  # Ensure it's on top of the stack
    mergetype = "Replace"  # Replace any existing cmdset

    def at_cmdset_creation(self):
        self.add(CmdLook())
        self.add(CmdQuit())
        self.add(CmdHelp())
        self.add(CmdGhostStatus())

