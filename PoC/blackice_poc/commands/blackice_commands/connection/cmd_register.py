from evennia import Command
from evennia.server.sessionhandler import SESSION_HANDLER
from evennia.utils import delay, create
import time
import random
import secrets

from evennia.utils.search import search_object_by_tag

from blackice_poc.typeclasses.blackice_typeclasses.ghost_chamber import GhostChamber


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
            typeclass="typeclasses.blackice_typeclasses.ghost_account.GhostAccount",
        )

        ghost_account.db._is_ghost = True
        ghost_account.db._registered = False
        ghost_account.db._ghost_created = time.time()
        ghost_account.db._ghost_ttl = 300  # 5 min
        ghost_account.save()

        ghost_room = search_object_by_tag("GhostChamber")
        if not ghost_room:
            ghost_room = create.create_object(GhostChamber, key="GhostChamber")
            ghost_room.db.desc = (
                "\n|c[BLACKICE NODE]|n Cybernetic soulforge. Memory residue clings to the walls.\n"
            )
        else:
            ghost_room = ghost_room[0]

        # Create temporary character
        char = create.create_object("typeclasses.blackice_typeclasses.ghost_persona.GhostPersona", key=f"persona_{ghost_id}",
                                    home=ghost_room)
        char.location = ghost_room

        char.locks.add(f"puppet:id({ghost_account.id})")

        char.account = ghost_account
        char.save()

        SESSION_HANDLER.login(session, ghost_account)

        ghost_account.db._last_puppet = char
        ghost_account.puppet_object(session, char)

        session.msg(f"|g[SYS]|n Ghost shell activated: {ghost_id}. Begin persona creation now.\n")

        char.execute_cmd("look")

        # Setup TTL decay
        delay(240, ghost_account.msg, "|y[TRACE]|n Soulprint unstable. 1 minute until purge.")
        delay(270, ghost_account.msg, "|r[BLACKICE]|n Final warning. Execute registration or be deleted in 30 seconds.")
        delay(300, self.expire_ghost_shell, ghost_account)

    def expire_ghost_shell(self, account):
        if not account or not account.db._is_ghost:
            return

        puppet = account.db._last_puppet
        if puppet:
            puppet.msg("|r[ICE]|n Persona expiration imminent. Shell collapse triggered.")
            puppet.delete()

        for sess in account.sessions.all():
            sess.msg("|r[ICE]|n Ghost shell TTL expired. Terminating uplink.")
            sess.disconnect()

        account.msg("|r[BLACKICE]|n Erasing ghost uplink…")
        account.delete()

