# 📖 BLACKICE Rulebook – Core Systems

## 🎲 1. Dice Mechanics & Resolution System

### Base System
- All actions are resolved using a **D20-based system**:
  - `D20 + Skill + Modifier(s) vs Difficulty Class (DC)`
  - A roll equal to or greater than the DC = success

### Core Skills
| Skill         | Description |
|---------------|-------------|
| Stealth       | Avoiding ICE, moving undetected, silent operations |
| Hacking       | Accessing, bypassing, decrypting systems and defenses |
| Engineering   | Crafting, repairing, modifying hardware/software |
| Cybercombat   | Attacks against ICE or deckers, program deployment |
| Logic         | Analyzing flows, decrypting paths, firewall mapping |
| Evasion       | Dodging trace, scrambling identity, escaping traps |

### Modifiers
- **Program Modifier**: Based on the active ROM used
- **Cyberdeck Bonus**: Based on installed gear (e.g. stealth module)
- **Environmental Modifier**: ICE difficulty, noise, system integrity
- **Heat Penalty**: Higher Heat = penalties to stealth, trace, spoof

### Difficulty Classes (DCs)
| Action Difficulty | DC Range |
|-------------------|----------|
| Basic             | 10–12    |
| Moderate          | 13–16    |
| Hard              | 17–20    |
| Brutal            | 21–24    |
| Impossible        | 25+      |

Will associate to that the Core Skills of the crafter.

---

## 🧠 2. Action Economy

### Types of Actions
- **Major Action** – Infiltrate, deploy program, attack, decrypt, reroute
- **Minor Action** – Move, toggle module, read logs, change deck config
- **Free Action** – Speak, chat, crew callout, inspect surroundings

### Action Points (AP)
- Each persona has **2 AP per turn** (in turn-based ops)
  - Major = 2 AP
  - Minor = 1 AP
- Real-time ops calculate **execution time + cooldown** instead of AP

---

## 🔍 3. Traces & Logs

### Trace Level
- Every action raises Trace by a certain amount (1–5 avg)
- At key thresholds (25 / 50 / 75 / 100), new effects occur:
  - 25: Passive ICE begins scanning
  - 50: Log ping triggers remote alert
  - 75: ICE starts to reroute traffic
  - 100: Node lockdown, ICE purge, trace to source begins

### Log System
- All node activity is logged by default
- Logs can be:
  - **Wiped** (`clean_logs()` roll vs ICE DC)
  - **Corrupted** (insert false entries)
  - **Forged** (requires blueprint log format + Engineering)

---

## 🧊 4. ICE Behavior & Structure

### ICE Activation Triggers
- Player detected by patrol or trap
- Trace level threshold hit
- Manual trigger (node admin, AI defense)

### ICE Behavior States
| State      | Description |
|------------|-------------|
| Passive    | Logs, observes, flags data to other ICE |
| Defensive  | Guards key files/programs, counterattacks if tampered |
| Aggressive | Seeks player, disables programs, drains RAM, deals biofeedback |
| Escalated  | Triggers trace-to-source, launches combat routines |

### ICE Types
| Type        | Function |
|-------------|----------|
| Patrol      | Scans for presence, logs movement |
| Guardian    | Defends key locations or programs |
| Supervision | Verifies ICE integrity, restarts disabled ICE |
| Combat      | Engages player directly with attacks |
| Spider      | Multi-role AI ICE, can reroute flows and corrupt logs |



