from commands.blackice_commands.cmdsets.connection.ghost import GhostCmdSet
from evennia import Command
from evennia.server.sessionhandler import SESSION_HANDLER
from evennia.utils import delay, create
import time
import random
import secrets

class CmdRegisterPersona(Command):
    """
    Begin persona registration through a temporary ghost shell.

    Usage:
      register_persona
    """
    key = "register_persona"
    aliases = ["rp"]
    locks = "cmd:all()"

    def func(self):
        session = self.caller
        if not session:
            return

        ghost_id = f"ghost_{int(time.time())}_{random.randint(100, 999)}"
        ghost_password = secrets.token_urlsafe(12)

        ghost_account = create.create_account(
            key=ghost_id,
            email=None,
            password=ghost_password,
            typeclass=None
        )

        ghost_account.db._is_ghost = True
        ghost_account.db._registered = False
        ghost_account.db._ghost_created = time.time()
        ghost_account.db._ghost_ttl = 300  # 5 min

        # Create temporary character
        char = create.create_object("typeclasses.blackice_typeclasses.persona.Persona", key=ghost_id)
        char.home = char.location = "#2"  # TODO: Your registration room ID

        char.locks.add(f"puppet:id({ghost_account.id})")

        char.account = ghost_account
        char.save()

        SESSION_HANDLER.login(session, ghost_account)

        ghost_account.db._last_puppet = char
        ghost_account.puppet_object(session, char)

        ghost_cmdset = GhostCmdSet()
        ghost_cmdset.obj = char
        char.cmdset.add(ghost_cmdset, permanent=True, default=False, merge=True)

        # Setup TTL decay
        delay(270, ghost_account.msg, "|y[TRACE]|n Soulprint unstable. 30 seconds until purge.")
        delay(295, ghost_account.msg, "|r[BLACKICE]|n Final warning. Execute registration or be deleted.")
        delay(300, self.expire_ghost_shell, ghost_account)

        session.msg(f"|g[SYS]|n Ghost shell activated: {ghost_id}. Begin persona creation now.")

    def expire_ghost_shell(self, account):
        if not account or not account.db._is_ghost:
            return

        if not account.db._registered:
            for sess in account.sessions.all():
                sess.msg("|r[ICE]|n Ghost shell TTL expired. Terminating uplink.")
            account.disconnect()
            account.delete()
