# 🧠 BLACKICE Rulebook – ICE Behavior Scripting (DSL v1)

> *“In BLACKICE, your ICE isn’t just code—it’s thought, paranoia, and premeditated violence wrapped in logic.”*

This rulebook details the **first implementation** of ICE scripting for the BLACKICE cyberspace PvP system.

It is designed for **text-based MUD (Evennia)** environments using a **domain-specific language (DSL)**  
with **in-game CLI input** to let players program their node's ICE behavior dynamically.

---

## 🎯 Goal

To allow **non-developer players** to configure complex, reactive ICE behavior through:
- Simple, readable scripting syntax
- Prompt-based line input (telnet/CLI-friendly)
- A behavior structure that can be parsed, validated, and executed in-game

---

## ⚙️ Entering Configuration Mode

```bash
> config_ice <ice_name>
```

This enters an **editor prompt**, where you can write the ICE’s logic line-by-line.

```plaintext
Editing behavior for ICE "patrol_alpha"
(type .save to compile, .cancel to abort, .help for keywords)
>
```

---

## 🧾 Script Syntax Overview

Each script is made up of **statements**:
- **Triggers** (`every:`, `if:`)
- **Actions** (`do:`, `then:`)
- **Events** (optional callbacks)
- **Modifiers** (timing, location, heat levels)

### Basic Block Example

```yaml
every: 5min
do: scan_logs()

if: persona_heat > 50
then:
  - activate(combat_ice_3)
  - log("High heat breach detected")

if: persona_location = D4
then:
  - move(patrol_alpha, D4)
```

---

## 🔑 Supported Keywords

### TRIGGERS

| Keyword       | Description |
|---------------|-------------|
| `every: <time>` | Repeats on interval (1min, 5min...) |
| `if:`          | Conditional logic check |
| `on_detect:`   | Fires when persona is revealed |
| `on_intrusion:`| Fires once combat starts |

---

### CONDITIONS (Used after `if:`)

| Condition                  | Description |
|----------------------------|-------------|
| `persona_heat > <value>`  | Checks intruder’s current heat |
| `persona_location = <cell>` | Cell coordinate match |
| `persona_trace = <id>`    | Match known intruder |
| `log_contains("keyword")` | Check access/system logs |

---

### ACTIONS (Used after `do:` or `then:`)

| Action                     | Description |
|----------------------------|-------------|
| `scan_logs()`              | Scan access/system logs |
| `activate(<ice_id>)`       | Deploy another ICE |
| `move(<ice_id>, <cell>)`   | Move ICE to location |
| `log("<msg>")`             | Write to ICE log |
| `trap_zone(<cell>)`        | Deploys trap ROM in cell |
| `alert_defender()`         | Sends ping to node owner |
| `reboot_self()`            | Resets ICE behavior loop |
| `jam_persona()`            | Temporarily disables target action |
| `deploy_rom(<rom_id>)`     | Executes ROM from ICE inventory |

---

## ✨ Inline Example

```yaml
every: 2min
do: scan_access_logs()

if: persona_heat > 30
then:
  - move(guard_1, attacker_location)
  - log("Guard repositioning to high-heat signature")

if: persona_location = D3
then:
  - deploy_rom(trace_swap())
```

---

## 📋 Input Commands (CLI)

| Command     | Description |
|-------------|-------------|
| `.save`     | Validate + compile script into ICE |
| `.cancel`   | Abort editing |
| `.clear`    | Wipe current buffer |
| `.example`  | Display sample script |
| `.preview`  | Show current script tree |
| `.help`     | List keywords + syntax tips |

---

## 🧠 Notes on Behavior

- You can mix multiple `if`/`then` blocks
- Each ICE runs its behavior loop independently
- Scripts are stored in `ICE.db.behavior_tree`
- Invalid scripts will return friendly error messages
- You may unlock **advanced triggers** and **passive routines** via skill or software upgrades

---

## 🚨 Future Features (v2+ Ideas)

| Feature           | Status |
|-------------------|--------|
| `unless:` logic   | [Planned] Negation logic support |
| Variable support  | [Planned] Use stored persona tags, heat tracking |
| Event callbacks   | [Planned] `on_exit`, `on_breach`, `on_fail` |
| ICE memory        | [Planned] Let ICE remember prior persona behavior |
| Debug commands    | [Planned] `simulate()`, `test_trace()` |

---

## 💥 Final Thought

This isn’t just automation.  
It’s *digital defense poetry*, written in the blood of would-be intruders.

**You don’t just defend your node. You teach it how to fight.**

Build smarter ICE, and let the black grid *learn your enemies.*

