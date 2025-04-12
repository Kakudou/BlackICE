import random

def connection_screen():
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

    bootsplash = [
        SCREEN_CLEAR,
        "[BOOT]> Initializing Cyberdeck Firmware v3.77-BLACKICE...",
        "[OK] Deck core.................. \x1b[38;5;46mLOADED\x1b[0m",
        "[OK] Optic socket interface..... \x1b[38;5;46mREADY\x1b[0m",
        "[WARN] ICE signature scan....... \x1b[38;5;214mMUTATING\x1b[0m",
        f"[SYS] Injecting bootloader traps......... {random.choice(glitch_fragments)}",
        "[ERR] Trace echo detected in uplink node...",
        "[RECOVER] Disabling watchdog......... \x1b[38;5;33m✔\x1b[0m",
        "[OK] Node mask compiled from entropy lattice.",
    ]

    boot_sequence = "\n".join(bootsplash)

    terminal_hud = fr"""
┌──────────────────────────────────────────────────────┐
│  CYBERDECK: BLACKICE ∷ SYSTEM BOOT                   │
├──────────────────────────────────────────────────────┤
│  ∷ STATUS : {net_state:<34}       │
│  ∷ GRID   : SPIRAL[∞]     |  NODE_COM[OK]            │
│  ∷ UPLINK : {rand_ip:<34}    │
│                                                {glitch}│
│  connect <persona> <password>   → JACK IN           │
│  jack-in               → SPAWN REGISTER SHELL        │
│  quit                               → ABORT SEQUENCE  │
├──────────────────────────────────────────────────────┤
│  WARNING: BlackICE signature detected on this port.   │
│  Unauthorized access will trigger neuroburn protocol. │
└──────────────────────────────────────────────────────┘
"""

    return f"{boot_sequence}\n\n{terminal_hud}"

