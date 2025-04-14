# BLACKICE Game Design Document – PvP Intrusion & ICE Programming

> *“You don’t outplay your enemies. You outscript them.”*

This Game Design Document (GDD) outlines two core pillars of BLACKICE:

1. **Player-vs-Player Intrusion Gameplay**  
2. **ICE Programming & Automation System**

These systems are the foundation of conflict, strategy, and progression inside BLACKICE’s hostile cyberspace.

---

## I. PVP NODE INFILTRATION SYSTEM

### Overview

Every player in BLACKICE owns a **single node** on a spiraling global grid.  
Players can traverse nodes, discover fog-covered systems, and attempt **real-time or passive intrusions** against others for data, ROMs, logs, credits, or control.

---

### Core Gameplay Loop

| Phase               | Description |
|---------------------|-------------|
| **Preparation**     | Loadout, ROM selection, route planning |
| **Traversal**       | Travel through grid via manual steps or warps |
| **Infiltration**    | Stealth recon on target node, heat-sensitive probing |
| **Combat Trigger**  | When detected, ICE engage and node enters combat |
| **Attack/Defend**   | Player executes ROMs, manipulates assets, dodges ICE |
| **Escape or Die**   | Exit the node, or get shutdown and possibly traced |
| **Remediation**     | Defender investigates logs, repairs, retaliates |

---

### Systems Breakdown

#### 1. Grid World
- **Spiral Placement:** Prevents early/new player harassment
- **Directional Flow:** Players can move in 8 directions
- **Backdoors:** Create direct links (double-edged)

#### 2. Node Grid
- Each node is a 2D grid (e.g. 8x8)
- Fog of War per node
- Assets are hidden until scanned or triggered

#### 3. Persona Movement
- Player has a **pawn** on the node
- Can move using:
  - `move north`, `move C4`
  - ROM-based movement (blink, ghost_slide)
- Movement affects:
  - Heat level
  - ICE LoS
  - Action radius

#### 4. Heat + Stealth
- Every action increases **HEAT**
- HEAT threshold → **Detection**
- ROMs and gear can:
  - Suppress trace
  - Delay detection
  - Fake logs

#### 5. Attack Actions
- Interact with:
  - Logs
  - ROMs
  - Vaults
  - Triggers
- Use ROMs like:
  - `erase_log()`, `deploy_payload()`, `elevate_privileges()`

#### 6. Escape Phase
- Path to exit must be physically reachable
- May be blocked by ICE, traps, firewalls
- Some ROMs assist: `eject_safely()`, `blind_trace()`

---

### PvP Edge Cases

- **Multiple intruders** can clash inside a node
- **Team raids** vs high-value targets
- **Ghost ICE** that continues operating post-player death
- **Persona bounty system** for high-risk intruders

---

## II. ICE PROGRAMMING SYSTEM

### Overview

ICE are not dumb turrets.  
They are **custom-programmed constructs** that act based on logic trees.

Each ICE has:
- **Behavior Script** (stored per ICE)
- **Trigger Conditions**
- **Actions & Reactions**
- Optional ROM slots (to deploy reactive programs)

---

### Programming Interface (CLI v1)

- Players configure ICE via:
```bash
> config_ice patrol_3
```

- Enter DSL mode:
```yaml
every: 5min
do: scan_logs()

if: persona_heat > 40
then:
  - activate(combat_ice_2)
  - log("High trace detected.")
```

- Save with `.save`, `.preview`, `.help`, `.cancel`

---

### Scripting Syntax (DSL)

| Block       | Description |
|-------------|-------------|
| `every:`    | Repeating triggers (time-based) |
| `if:`       | Conditional evaluation |
| `then:`     | Consequence block |
| `do:`       | Simple scheduled actions |

---

### Supported Logic

| Condition               | Effect |
|-------------------------|--------|
| `persona_heat > N`      | Heat-based behavior |
| `persona_location = C4` | Spatial logic |
| `log_contains()`        | Log check |
| `persona_trace = id`    | Recognized persona |

| Action                  | Effect |
|-------------------------|--------|
| `move(ice, cell)`       | Reposition ICE |
| `activate(ice)`         | Summon another ICE |
| `log()`                 | Write to node log |
| `deploy_rom()`          | Execute ROM from ICE |
| `jam_persona()`         | Debuff persona |
| `trap_zone()`           | Triggers trap |

---

### ICE Runtime Logic

- ICE behavior runs per tick or event
- Trigger/Action structure is validated
- Stored on `ICE.db.behavior_tree`
- Compiled once per `.save`

---

### Design Philosophy

| Principle        | Implementation |
|------------------|----------------|
| No dev skills    | Friendly scripting DSL |
| Depth            | Conditions + multiple triggers |
| Counterplay      | Attackers can analyze ICE behavior |
| Modular upgrades | Unlock more conditions/actions as ICE level increases |
| RP-immersive     | Logs, alerts, trace memory allow real investigation |

---

## Long-Term Integration

- Visual Editor for GUI/browser version
- Behavior Blueprint sharing
- Craftable ICE personalities (aggressive, reactive, passive)
- Player-built ICE ROMs
- AI ICE with partial learning memory
- Post-breach ICE behavior change tracking

---

## Summary

This GDD defines a deeply tactical PvP loop rooted in:
- Physical positioning
- Trace-based stealth
- ICE behavior logic
- High-stakes digital warfare

BLACKICE isn’t about stats.  
It’s about who can **read**, **adapt**, and **outscript** their enemies faster than they can disappear.

**Own your node. Or lose it.**

