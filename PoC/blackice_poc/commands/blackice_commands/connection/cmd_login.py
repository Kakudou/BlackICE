from evennia.commands.default.unloggedin import CmdUnconnectedLook
from evennia.commands.default.unloggedin import CmdUnconnectedHelp
from evennia.commands.default.unloggedin import CmdUnconnectedQuit
import random

class CmdUnloggedinLookPrompt(CmdUnconnectedLook):
    """
    Custom look command that appends a cyberpunk prompt.
    """
    def func(self):
        super().func()
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
        final_prompt = f"{color1}$> |n{color2}{prompt1}|n\n{color2}$> |n{color1} {prompt2} |n\n{color3}$> Waiting for user input... |n\n"
        self.caller.msg(f"{final_prompt}")

class CmdLoginHelp(CmdUnconnectedHelp):
    """
    Custom help for the login screen.
    """
    def func(self):
        self.caller.msg("""
|wYou are not yet connected to a persona. Available commands:

  |gconnect <name> <password>|n - access your cyberdeck
  |glook|n                    - reprint the connection log
  |ghelp|n                    - this message
  |gquit|n                    - abort connection sequence

Unauthorized access will trigger ICE trace.
""")

class CmdBlackICEQuit(CmdUnconnectedQuit):
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
        self.caller.msg(f"|r{message}|n\n")
        super().func()

