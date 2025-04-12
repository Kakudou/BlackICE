from evennia.commands.default.cmdset_unloggedin import UnloggedinCmdSet
from commands.blackice_commands.connection.cmd_login import CmdUnloggedinLookPrompt, CmdLoginHelp, CmdBlackICEQuit
from evennia.commands.default.unloggedin import CmdUnconnectedConnect

class CustomUnloggedinCmdSet(UnloggedinCmdSet):
    """
    Custom command set for unconnected users — stripped down to bare ops.
    """
    key = "Unloggedin"
    priority = 0

    def at_cmdset_creation(self):
        self.add(CmdUnloggedinLookPrompt())
        self.add(CmdLoginHelp())
        self.add(CmdBlackICEQuit())
        self.add(CmdUnconnectedConnect())







