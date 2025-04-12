import random

from twisted.internet import reactor

def connection_screen(caller):
    SCREEN_CLEAR = "\033[2J\033[H"
    glitch_fragments = ["▒▒▒", "░░░", "▓▓▓", "⸮⸮⸮", "███", "///", "💀💀💀"]
    net_states = [
        "SCANNING NODE...",
        "LINK STABLE",
        "TRACE IN PROGRESS",
        "GRID COLLAPSE IMMINENT",
        "AUTH BYPASSED",
        "SIGNAL LOST",
        "JACKPORT OPEN",
        "WATCHDOG DISABLED"
    ]
    rand_ip = f"2077.404.{random.randint(100,999)}.AI"
    glitch = random.choice(glitch_fragments)
    net_state = random.choice(net_states)

    caller.msg(SCREEN_CLEAR)
    bootsplash = [
        "[BOOT]> Initializing Cyberdeck Firmware v3.77-BLACKICE...",
        "[OK] Deck core.................. \x1b[38;5;46mLOADED\x1b[0m",
        "[OK] Optic socket interface..... \x1b[38;5;46mREADY\x1b[0m",
        "[WARN] ICE signature scan....... \x1b[38;5;214mMUTATING\x1b[0m",
        f"[SYS] Injecting bootloader traps......... {random.choice(glitch_fragments)}",
        "[ERR] Trace echo detected in uplink node...",
        "[RECOVER] Disabling watchdog......... \x1b[38;5;33m✔\x1b[0m",
        "[OK] Node mask compiled from entropy lattice.\n",
    ]

    delay = 1
    for entry in bootsplash:
        reactor.callLater(delay, caller.msg, entry)
        delay+=0.5

    terminal_hud = fr"""
┌──────────────────────────────────────────────────────┐
│  CYBERDECK: BLACKICE ∷ SYSTEM BOOT                   │
├──────────────────────────────────────────────────────┤
│  ∷ STATUS : {net_state:<34}       │
│  ∷ GRID   : SPIRAL[∞]     |  NODE_COM[OK]            │
│  ∷ UPLINK : {rand_ip:<34}    │
│                                                   │
│                <: Commands :>                  {glitch}│
│  jack-in <persona> <password>  #Jack-in cyberspace  │
│  register_persona            #Create a Persona       │
│                                                      │
│  jack-out                   #Back to your meat shell  │
├──────────────────────────────────────────────────────┤
│  WARNING: BlackICE signature detected on this port.   │
│  INFO: if your lost, just call the `help`.           │
│  Unauthorized access will trigger neuroburn protocol. │
└──────────────────────────────────────────────────────┘
"""
    for entry in terminal_hud.splitlines():
            reactor.callLater(delay, caller.msg, entry)
            delay+=0.2

    return delay


