from evennia.commands.default.cmdset_unloggedin import UnloggedinCmdSet
from blackice_poc.commands.blackice_commands.connection.cmd_register import CmdRegisterPersona
from commands.blackice_commands.connection.cmd_login import CmdUnloggedinLookPrompt, CmdLoginHelp, CmdBlackICEQuit, CmdJackIn

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
        self.add(CmdJackIn())
        self.add(CmdRegisterPersona())








