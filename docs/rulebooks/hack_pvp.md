# ⚔️ BLACKICE Rulebook – Intrusion, Defense & Cybercombat System

> *“You don’t just hack the grid—you walk through its fire.”*

This rulebook documents the **core gameplay loop** of BLACKICE:  
**Player-vs-Player (PvP) Node Intrusion, Defense Programming, Combat, and Remediation**,  
with **spatial grid movement**, **heat-based stealth**, and **tactical presence** at the core of every operation.

---

## OVERVIEW

At its core, BLACKICE is a war of wits, code, and chaos inside a living cyberspace network.

- Every player owns **one node** in the global grid.
- Players can explore, discover, and **invade others' nodes** in real-time.
- Each node has **programmable defenses**, **assets**, and **ICE**.
- Attackers rely on **crafted ROMs**, stealth, and timing.
- Defenders must **plan ahead** and respond after intrusion with **digital forensics** and **rebuilds**.

---

## 🌐 GLOBAL CYBERSPACE GRID

- Nodes are placed in a **Fibonacci spiral pattern**.
  - Older players are placed further, giving natural buffer.
- Players can traverse the cyberspace by:
  - **Manual movement** across cardinal directions
  - **Coordinate targeting**, which passively passes through intermediate nodes
- Every node passed may:
  - Log your passage
  - Trigger ICE behavior
  - Detect you if stealth is broken

---

## 🌫 FOG OF WAR & DISCOVERY

- Every node is obscured until:
  - You scan or traverse it
  - The owner refreshes/re-obscures it

- The node itself is a **cellular grid** (e.g., 8x8)
  - Assets, ICE, traps, and logs are hidden inside this matrix
  - Your **persona is physically present** within the grid

---

## ♟️ PERSONA MOVEMENT – Tactical Grid Presence

> “Your code isn’t remote—it walks the battlefield.”

### 🧭 Movement Methods

- `move C3` — move to a coordinate
- `move north/east/etc.` — relative direction
- Movement may cost:
  - **Action Points** in combat
  - **RAM or trace** if using stealth movement

### 🕹 Interaction Zones

| Asset Type       | Requires Proximity? | Range Mods |
|------------------|----------------------|------------|
| Logs, data cores | Yes                 | None       |
| ICE scanners     | No                  | ROM-defined |
| Vaults           | Yes                 | Always     |
| Escape routes    | Yes                 | Must reach node edge or tagged cell |

### 📦 Cell Traits

- **Shadow zones** — reduce trace gain
- **Firewall cells** — spike heat if passed through
- **Locked zones** — require key or backdoor
- **Line of sight** — affects ICE detection and targeting

---

## 🕵️‍♂️ STEALTH PHASE

- On node entry, you are **stealthed by default**
- Each action (movement, scan, ping) raises **HEAT**
- Some ROMs help reduce trace or obscure movement

| Action             | Heat Gain | Notes |
|--------------------|-----------|-------|
| `scan_cell()`      | +5        | Low-risk recon |
| `move` (normal)    | +2        | Can vary by zone |
| `hack_asset()`     | +10       | Immediate ICE check |
| `stealth_move()`   | +0–2      | ROM-modified, consumes RAM |

When **HEAT crosses threshold**, you are detected and combat begins.

---

## ⚠️ DETECTION & DEFENSE ACTIVATION

- Once detected, node enters **combat mode**:
  - **ICE behavior trees** engage
  - Defender cannot act directly—only via **preloaded ROMs** or **automated ICE**
  - Attacker loses all stealth and is now visible on grid

---

## 🛡 DEFENSE PROGRAMMING

### 📈 ICE Programming

ICE is scripted using flowcharts, not real AI.  
Example:
```yaml
- every: 5min
  do: scan_access_logs()

- if: heat > 40
  then: activate('combat_ice_2')

- if: persona_location = cell_C3
  then:
    - move('guard_1', 'cell_C3')
    - log("ICE moving to intercept")
```

### 🤖 ICE Movement

- ICE has speed, behavior patterns, and detection rules
- ICE reacts to:
  - Persona position
  - Asset changes
  - Log anomalies

### 🔁 Defender ROMs (Preloaded)

| ROM Name          | Triggered By      | Function |
|-------------------|-------------------|----------|
| `grid_morph()`    | Breach Detected    | Shuffles grid layout to disorient attacker |
| `blackout_patch()`| Heat > 40         | Disables scans temporarily |
| `trace_swap()`    | Persona detected  | Rewrites trace ID |
| `bio_pulse()`     | Manual/Auto-fire  | Stuns intruder in radius 1 |

ROMs can be scripted into ICE routines and deployed automatically.

---

## ⚔️ COMBAT PHASE

### 🎮 Turn-Based Combat Rules

- Players and ICE act based on initiative or loop speed
- Persona can:
  - Move cell-to-cell
  - Execute ROMs
  - Interact with assets
  - Escape

- ICE will:
  - Pursue based on LoS or programmed patterns
  - Use ROMs or natural abilities to hunt, disable, or trace

---

## 🧳 ESCAPE PHASE

- Reach a node edge or **backdoor cell**
- Can use:
  - `eject()`
  - `trace_damp()` before escape
  - `jam_trace()` to delay ICE
- Smart play includes:
  - Covering logs (`erase_log`)
  - Masking footprints (`residue_fake()`)

---

## 🧹 POST-BREACH: DEFENSE RECOVERY

Defender Actions:
- Review logs (access, system, ICE patrol logs)
- Detect anomalies
- Reobfuscate grid layout
- Update ICE patrols
- Load counter-ROMs into defense script
- Reprogram compromised ICE
- Investigate backdoors or corrupted data nodes

---

## STRATEGIC HIGHLIGHTS

| System                | Impact |
|------------------------|--------|
| Persona Positioning    | Directly affects what you can access or avoid |
| Tactical Movement      | Turns nodes into stealth-puzzle maps |
| Programmable ICE       | Gives defenders agency beyond dumb patrols |
| Live Defense ROMs      | Deepens defender tactics |
| Line-of-Sight          | Enables shadowplay, jukes, kiting |
| Heat-Based Stealth     | Forces smart action economy |
| Grid Terrain           | Adds risk-reward zones and resource traps |

---

You don’t just *hack* in BLACKICE.

You **move**,  
you **hide**,  
you **evade**,  
you **burn the grid**,  
or **die inside it.**

Welcome to *The Grid War*.
