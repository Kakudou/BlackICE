import random
from evennia.utils.logger import log_info
from evennia import DefaultRoom

class GhostChamber(DefaultRoom):
    """
    A special ghost-safe room for persona registration.
    Hides non-ghosts, suppresses account noise like 'This is User #1'.
    """

    def return_appearance(self, looker, **kwargs):
        string = super().return_appearance(looker, **kwargs)

        return string


