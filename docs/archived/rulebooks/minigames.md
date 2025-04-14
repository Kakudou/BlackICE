# 📖 BLACKICE Rulebook – Minigames & Subsystems

## 🎮 9. Minigame Systems
Each minigame is tied to a specific system or action type. Success modifies rolls, opens access, or prevents trace penalties. Failure can result in ICE activation, program corruption, or node instability.

---

### 1. Log Cleaner
**Purpose:** Erase trace logs from node systems.
- Gameplay: Pattern-match log strings in limited time.
- Difficulty scales with Trace level and ICE presence.
- Success: Removes logs and trace entries.
- Failure: Incomplete wipe, possible ICE ping or rollback.

---

### 2. Trace Delay
**Purpose:** Delay incoming ICE or trace events.
- Gameplay: Time-based button tap / input sequence.
- Patterns become faster as Heat rises.
- Success: Adds delay (1–3 turns or seconds) to trace countdown.
- Failure: Immediate escalation to next Trace tier.

---

### 3. Compiler Puzzle
**Purpose:** Craft custom ROMs under RAM constraints.
- Gameplay: Tetris-like block puzzle
- Each block = program capability (`decrypt()`, `logger()`, etc)
- ROM shell has shape and size restrictions.
- Success: Compiled custom ROM with tags.
- Failure: Crashes at boot or hidden instability rolls.

---

### 4. RAM Juggle
**Purpose:** Manage programs during high load or ICE attack.
- Gameplay: Real-time inventory shift to move active programs into free slots
- Time-limited; failure = freeze or program crash
- Success: Active programs maintained, freeze avoided
- Failure: Random crash, corruption, or deck freeze for 1–3 turns

---

### 5. Firewall Cracker
**Purpose:** Bypass firewalls silently
- Gameplay: Color/wire match or pattern-replication challenge
- Layered defenses mean multi-stage challenge (ICE applies time pressure)
- Success: Firewall bypassed, entry logged as admin or ghost
- Failure: Firewall logs alert, ICE traces begin

---

### Minigame Triggers
- Can appear during parser ops or after failed/successful rolls
- Optional in low-tier nodes
- Required for elite corp or high-value nodes
- Can be influenced by persona stats (e.g. `Logic` makes puzzles easier)

---

### Difficulty Scaling
| Tier        | Effect |
|-------------|--------|
| Easy        | Static challenge, longer timers |
| Moderate    | Moderate speed / complexity |
| Hard        | Timer pressure, false cues, misleading patterns |
| Extreme     | Randomized layers, ICE interference, multi-tool switching |


