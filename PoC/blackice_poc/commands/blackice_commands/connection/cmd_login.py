from evennia.accounts.models import AccountDB

from evennia.commands.default.unloggedin import CmdUnconnectedLook
from evennia.commands.default.unloggedin import CmdUnconnectedHelp
from evennia.commands.default.unloggedin import CmdUnconnectedQuit
from evennia.commands.default.unloggedin import CmdUnconnectedConnect
from twisted.internet import reactor
import random

from blackice_poc.world.blackice_world.cyberdeck_login_prompt import connection_screen

class CmdJackIn(CmdUnconnectedConnect):
    """
    Replaces default connect. Usage: jack-in <name> <password>
    """
    key = "jack-in"
    aliases = ["ji", "login", "connect"]
    locks = "cmd:all()"

    def func(self):
        args = self.args.strip()
        if not args or len(args.split()) < 2:
            self.caller.msg("|rUsage: jack-in <name> <password>|n")
            return

        name, password = args.split(maxsplit=1)
        self.session = self.caller  # self.caller is the session here

        self.session.msg("\033[2J\033[H")
        self.session.msg("|c[JACK-IN]|n Initializing uplink sequence...\n")

        jackin_sequences = [
            [
                "[JACK-IN] rebooting neural interface...",
                "[CORE] Persona link stable...",
                "[GRID] Conscious sync active...",
                "[ICE] Running trace cloak...",
                "[ACCESS] Entering the node now..."
            ],
            [
                "[SYS] Injecting neural scaffold...",
                "[NEXUS] Stabilizing cognitive loop...",
                "[TRACE] Ghost signature detected...",
                "[CORE] Synchronization complete.",
                "[ACCESS] Welcome back, soulprint confirmed."
            ],
            [
                "[BOOT] Activating synthetic cortex...",
                "[Σ] Ghostform sync: 83%...",
                "[ICE] Phantom protocol engaged...",
                "[NET] Link verified.",
                "[JACK-IN] Uplink injected. You're inside."
            ],
            [
                "[DATA] Cipher burst accepted.",
                "[SHELL] Initializing hollow thread...",
                "[SYS] Anchor lock acquired...",
                "[CORE] Reconstructing digital spine...",
                "[JACK-IN] Jack complete. Ghost online."
            ],
            [
                "[TRACE] Noise flooding layer...",
                "[NODE] Entropy mask applied...",
                "[NEXUS] Access corridor deployed...",
                "[CORE] ICE decoy sequencer live...",
                "[ACCESS] Ghost has entered the grid."
            ],
            [
                "[ICE] Null-thread handshake dispatched...",
                "[SYS] Tracking feedback path...",
                "[BLACKICE] Signature bleed confirmed...",
                "[GATE] Digital shroud deployed.",
                "[JACK-IN] Brainprint verified. Entering."
            ],
            [
                "[GRID] Locating neural port...",
                "[NEXUS] Shell calibration at 96%...",
                "[SYS] Mindphase sync... steady...",
                "[CORE] Personality matrix sealed.",
                "[ACCESS] Welcome home, operator."
            ],
            [
                "[MEM] Coldbooting consciousness...",
                "[ICE] Shadowmap overlay engaged...",
                "[TRACE] Sentry heartbeat disrupted...",
                "[GATE] Tunnel stabilizing...",
                "[JACK-IN] Jack sequence finalized."
            ],
            [
                "[SHELL] Virtual spine loaded...",
                "[CORE] Persona echo intact...",
                "[BLACKICE] Node mirage verified.",
                "[SYS] ICE field bending around access.",
                "[ACCESS] Synthetic presence deployed."
            ],
            [
                "[JACK-IN] Initiating override burst...",
                "[SYS] Static pulse contained...",
                "[NEXUS] Personality anchor restored...",
                "[CORE] Neural web activated...",
                "[ACCESS] You're jacked in."
            ],
            # 10 more sequences
            [
                "[CORE] Ghost link attempt #0x14...",
                "[TRACE] Glitch noise rising...",
                "[SYS] Memory residue... clean.",
                "[NET] Soulprint echo confirmed.",
                "[JACK-IN] Injected. System yours."
            ],
            [
                "[ICE] Initializing cortical injection...",
                "[SYS] Data stream alignment...",
                "[NEXUS] Phantom link stabilized...",
                "[CORE] Persona coalescing...",
                "[ACCESS] Digital form manifested."
            ],
            [
                "[JACK-IN] Reconstructing access point...",
                "[TRACE] ICE misdirection active...",
                "[NET] Digital identity stitched...",
                "[CORE] Ghostform engagement confirmed.",
                "[ACCESS] Uplink achieved."
            ],
            [
                "[SHELL] Overriding memory fog...",
                "[SYS] Neural pattern reconstructed...",
                "[GATE] Vector gateway unlocked...",
                "[TRACE] Feedback nullified...",
                "[JACK-IN] Mindwalk initiated."
            ],
            [
                "[CORE] Cybertrace deflection running...",
                "[NET] Uplink spectrum clean...",
                "[Σ] Brainprint matched...",
                "[SYS] Ready for consciousness sync.",
                "[ACCESS] You're inside the machine."
            ],
            [
                "[SYS] Mind-latch engaged...",
                "[TRACE] Echoes suppressed...",
                "[CORE] Thoughtform injected...",
                "[ICE] Signature cloak established.",
                "[ACCESS] Digital self embedded."
            ],
            [
                "[BLACKICE] Lattice realigned...",
                "[GATE] Node echo cleared...",
                "[CORE] Interface rituals complete...",
                "[TRACE] Trace disabled manually...",
                "[JACK-IN] Neural link completed."
            ],
            [
                "[MEM] Shell data flowing...",
                "[NET] Phantom process accepted...",
                "[SYS] Feedback anomaly resolved.",
                "[Σ] Internal gate signature verified.",
                "[ACCESS] Mental signature uploaded."
            ],
            [
                "[NEXUS] Wavelength coherence achieved...",
                "[CORE] Uplink tunnel bending...",
                "[TRACE] Digital trail burned.",
                "[SYS] Ghostbinding complete.",
                "[JACK-IN] Welcome to the grid."
            ],
            [
                "[GATE] Executing soulcast injection...",
                "[NET] ICE field distortion active...",
                "[CORE] Thought-husk integration...",
                "[TRACE] Persona net cloned...",
                "[ACCESS] System open. You are live."
            ]
        ]

        chosen_lines = [random.choice(seq) for seq in random.sample(jackin_sequences, 4)]

        full_sequence = chosen_lines

        for i, line in enumerate(full_sequence):
            reactor.callLater(i + 1, self.session.msg, f"|g{line}|n")

        reactor.callLater(len(full_sequence) + 1, self.attempt_login, name, password, 1)


    def attempt_login(self, name, password, delay):
        """
        Authenticates manually to inject ICE response if it fails.
        """
        account = AccountDB.objects.get_account_from_name(name)
        if not account or not account.check_password(password):
            failure = random.choice([
                "[BLACKICE ALERT] Invalid neural signature detected.",
                "[ICE] Soulprint rejected. Signal corrupted.",
                "[TRACE] Uplink refused. Construct mismatch.",
                "[SYS] Jack-in denied. Access vector malformed.",
                "[CORE] Ghostform verification failed. You do not exist.",
                "[ICE] Jack-in anomaly. Neural interface breached.",
                "[Σ] Phantom pattern rejected. Security engaged.",
                "[BLACKICE] Unauthorized construct ping. Retaliation imminent.",
                "[NET] Synthetic ID invalid. Trace spike dispatched.",
                "[GATE] Authentication node response: DENIED. No entry."
            ])
            reactor.callLater(delay, self.session.msg, f"\n|r{failure}|n\n")

            reactor.callLater(2.5, self.session.execute_cmd, "look")

            return
        else:
            final_prompts = [
                "\n[ACCESS GRANTED] Welcome back, {name}. The grid remembers you.\n",
                "\n[JACK-IN COMPLETE] Neural link stabilized, {name}. You're live.\n",
                "\n[CORE] {name}, your shell is loaded and walking.\n",
                "\n[ICE] Jack confirmed. Trace clean. Execute, {name}.\n",
                "\n[GATE] {name} accepted. Mental signature aligned.\n",
                "\n[BLACKICE] {name}, soulprint embedded. You're no longer meat.\n",
                "\n[SYSTEM] {name} has returned. Shadow walk enabled.\n",
                "\n[Σ] Digital identity verified. Welcome, {name}.\n",
                "\n[VOID] Echo pattern synced. {name}, begin infiltration.\n",
                "\n[TRACE NULL] {name}, presence cloaked. Proceed.\n"
            ]
            final_line = random.choice(final_prompts).format(name=name)
            reactor.callLater(delay, self.caller.msg, final_line)

        self.args = f"{name} {password}"
        super().func()

class CmdUnloggedinLookPrompt(CmdUnconnectedLook):
    """
    Custom look command that appends a cyberpunk prompt.
    """

    aliases = ["look", "l", "reboot"]

    def func(self):
        super().func()

        delay = connection_screen(self.caller)

        prompt_variants = [
            "[~] SYSTEM READY",
            "[:: BLACKICE CONSOLE ONLINE ::]",
            "// awaiting soulprint...",
            "[sys:BLACKICE]#",
            "|> LINK STABLE\n|>",
            "SYSTEM: Boot Integrity Verified"
            "[ICE] Injecting synthetic synapse...",
            "[CORE] Bootloader integrity nominal.",
            "[net:VOID] Ghost signal detected on uplink.",
            "// Spooling memory from cold sectors...",
            "[sys] Awaiting input from consciousness shell...",
            "[BLACKICE] Echo pattern match: NEURAL_Δ.SYNC",
            "[Σ] Soulprint handshake incomplete...",
            "[env] NODE_COM anomaly: entropy spike detected.",
            "[link] Circuit bleed within tolerance.",
            "/// bootlog: trace vector decrypted.",
            "[grid:∞] Listening to psychic feedback...",
            "[!] WARNING: dreamloop instability rising.",
            "[sys] Reassembling thoughtform fragments...",
            "[node] Feedback coil synced at 99.7%",
            "[trace] Countermeasure shadow detected.",
            "[uplink] Quantum noise calibrated.",
            "[kernel] Uploading synthetic spine...",
            "[ICE] Residual echo pattern… STABLE",
            "[sys] Requesting protocol layer authentication.",
            "[shell] Signal bleed acknowledged. Listening…"
        ]
        prompt1 = random.choice(prompt_variants)
        prompt2 = random.choice(prompt_variants)
        color1 = random.choice(['|r', '|g', '|c', '|m', '|y', '|w'])
        color2 = random.choice(['|r', '|g', '|c', '|m', '|y', '|w'])
        color3 = random.choice(['|r', '|g', '|c', '|m', '|y', '|w'])
        final_prompt = f"\n{color1}$> |n{color2}{prompt1}|n\n{color2}$> |n{color1} {prompt2} |n\n{color3}$> Waiting for user input... |n\n"
        reactor.callLater(delay + 0.5, self.caller.msg, final_prompt)

class CmdLoginHelp(CmdUnconnectedHelp):
    """
    Custom help for the login screen.
    """
    def func(self):
        self.caller.msg("""
|wYou are not yet connected to a persona. Available commands:

  |gjack-in <name> <password>|n - Access the cyberspace with your persona.
  |greboot|n                    - Reboot the cyberdeck and check the uplink status.
  |ghelp|n                    - Display this help text.
  |gjack-out|n                    - abort connection sequence

Unauthorized access will trigger ICE trace.
""")

class CmdBlackICEQuit(CmdUnconnectedQuit):

    aliases = ["jack-out", "jo", "logout", "exit", "quit"]

    def func(self):
        color1 = random.choice(['|r', '|g', '|c', '|m', '|y', '|w'])
        color2 = random.choice(['|r', '|g', '|c', '|m', '|y', '|w'])
        message = random.choice([
            f"{color1}[CORE]|n{color2} Uplink terminated. Memory bleed within tolerance.|n",
            f"{color1}[SYS]|n{color2} Consciousness thread disengaged.|n",
            f"{color1}[ICE]|n{color2} Signal decay normalized. Jack-out successful.|n",
            f"{color1}[BLACKICE]|n{color2} Trace vectors severed. Node ghosted.|n",
            f"{color1}[COMMS]|n{color2} User echo lost. Connection dropped.|n",
            f"{color1}[NEXUS]|n{color2} Dreamloop cut manually. Escape confirmed.|n",
            f"{color1}[Σ]|n{color2} Data tether severed. Ghost slipping offline.|n",
            f"{color1}[TRACE]|n{color2} Feedback coil disengaged. Logging off...|n",
            f"{color1}[NODE]|n{color2} Neural anchor retracted. See you in the dark.|n",
            f"{color1}[SHELL]|n{color2} Persona withdrawn. Interface ghosting initiated.|n",
            f"{color1}[VOID]|n{color2} You vanish. No trace left behind.|n",
            f"{color1}[LOOP]|n{color2} Recursive pattern collapse... logout achieved.|n",
            f"{color1}[SEC]|n{color2} Port lockdown initiated. Goodbye, netrunner.|n",
            f"{color1}[FEED]|n{color2} Conscious override revoked. Logging out.|n",
            f"{color1}[GRID]|n{color2} Disconnect pulse accepted. Soul echo fading...|n",
            f"{color1}[ICE]|n{color2} Exit vector stabilized. Safe termination.|n",
            f"{color1}[CORE]|n{color2} Cyberdeck power-down... neural static resolved.|n",
            f"{color1}[GATE]|n{color2} Final packet sent. System will forget you.|n",
            f"{color1}[ENV]|n{color2} Protocol stack flushed. Mindlink broken.|n",
            f"{color1}[SYS]|n{color2} You leave nothing behind. Session terminated.|n"
        ])
        self.caller.msg("\033[2J\033[H")
        reactor.callLater(1, self.caller.msg, f"|r{message}|n\n")
        super().func()

