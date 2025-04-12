r"""
Evennia settings file.

The available options are found in the default settings file found
here:

https://www.evennia.com/docs/latest/Setup/Settings-Default.html

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "blackice_poc"
CMDSET_UNLOGGEDIN = "commands.blackice_commands.cmdsets.connection.unloggedin.CustomUnloggedinCmdSet"

GUEST_ENABLED = True
GUEST_PASSWORD = ""
GUEST_LIST = [
    "drifter",
    "phantom",
    "trace",
    "shell0",
    "error404",
    "0xdeadbeef",
    "0xbadc0de",
    "0xbabecafe",
    "0xfeedface",
    "guest",
]


START_LOCATION = "world.null"

COMMAND_MODULES = [
    "commands.blackice_commands",
    "commands.evennia_commands",
]

TYPECLASS_PATHS = [
    "scripts.blackice_scripts"
    "typeclasses.blackice_typeclasses",
    "typeclasses.evennia_typeclasses",
]

BASE_ACCOUNT_TYPECLASS = "typeclasses.accounts.Account"
BASE_CHARACTER_TYPECLASS = "typeclasses.blackice_typeclasses.persona.Persona"

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
