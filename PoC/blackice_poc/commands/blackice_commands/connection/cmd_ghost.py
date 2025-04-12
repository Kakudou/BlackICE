from evennia import Command
import time


class CmdGhostStatus(Command):
    """
    Show ghost shell time-to-live.

    Usage:
      status
    """
    key = "status"
    locks = "cmd:all()"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def func(self):
        acc = self.caller.account
        if not acc or not acc.db._is_ghost:
            self.caller.msg("|r[ICE]|n Command restricted to ghost shells only.")
            return

        created = acc.db._ghost_created or time.time()
        ttl = acc.db._ghost_ttl or 300
        remaining = max(0, int(created + ttl - time.time()))
        minutes, seconds = divmod(remaining, 60)

        self.caller.msg(f"|c[SYS]|n Ghost shell TTL: |w{minutes}m {seconds}s|n remaining.")

        if remaining < 60:
            self.caller.msg("|r[ICE]|n Persona expiration imminent. Complete registration now.")

