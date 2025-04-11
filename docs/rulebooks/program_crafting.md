# 💾 BLACKICE Rulebook – Program (ROM) Crafting via Snippets

> *“Programs aren't bought. They're built—stitched together from system wreckage, blackboxed logic, and blood-soaked fragments of dead ICE.”*

In **BLACKICE**, programs—known as **ROMs (Runtime Operative Modules)**—aren’t loot drops. They’re **assembled**, line-by-line, from executable logic blocks called **snippets**.  
These aren’t clean apps. They’re digital rituals—chaotic, unstable, and sometimes alive.

This rulebook outlines how to build, corrupt, and deploy ROMs inside the matrix.  
No crafting bench. No real-world tools. Just your **cyberdeck**, your **snippets**, and the **guts to risk running what you build**.

---

## 🧬 What Is a ROM?

A ROM is a **modular executable payload** that:
- Is crafted from a ROM core + snippets
- Loads into your deck (RAM) and executes directly
- Can contain **visible** or **hidden** logic
- May include **payloads**, **failovers**, **triggers**, or **malware**
- Has a **compile risk**, and **execution consequence**

ROMs behave like programmable spells—dynamically built, risk-balanced, and fully modifiable.  
They can crash, mutate, expose you, or take out a fortress node in one click.

---

### Program Attributes
- **Type**: `attack()`, `decrypt()`, `logger()`, `spoof()`, `backdoor()`
- **RAM Cost**: Memory required to run
- **Cooldown**: Turns or seconds before reuse
- **Stability**: % chance of crashing per run (increases with Heat or overload)
- **Detection Rating**: Difficulty for ICE to detect (Stealth programs only)

---

### Program States

| State    | Result |
|----------|--------|
| Active   | Consumes RAM, runs per loop or action |
| Dormant  | Loaded, but inactive. Ready to deploy |
| Crashed  | Failed to run, must be rebooted or restored |
| Corrupted| May cause unintended effects, e.g. misfire, leak logs |

---

## ⚙️ ROM Anatomy

| Component        | Role |
|------------------|------|
| **ROM Core**     | Base logic structure: attack, stealth, utility, etc. |
| **Snippets**     | Modular code blocks that determine behavior |
| **Flags**        | Optional execution modifiers (auto_eject, delayed, etc.) |
| **Payload**      | Embedded secondary program (e.g. trojan, virus) |
| **Hidden Logic** | Snippets that are concealed from standard scans |
| **Description**  | Player-facing metadata (editable) |

---

## 📥 ROM Core Types

| Core Type     | Purpose |
|---------------|---------|
| `attack_core` | Damages ICE, personas, or node integrity |
| `cloak_core`  | Obscures signature, suppresses trace |
| `decrypt_core`| Breaks encryption on data or programs |
| `crash_core`  | Disrupts ICE/program functionality |
| `track_core`  | Tags a persona or logs node movements |
| `sniff_core`  | Intercepts or logs matrix communications |
| `bomb_core`   | Traps files or node constructs |
| `heal_core`   | Repairs corrupted programs or systems |

Each core determines:
- Base RAM/CPU load
- Execution slot required
- Snippet compatibility
- Compile DC baseline

---

## 🔹 Snippets

Snippets are **atomic logic routines** that define the function, flavor, and risk of a ROM.

| Snippet Name           | Tags                   | Effect |
|------------------------|------------------------|--------|
| `burst_logic()`        | `damage`, `unstable`   | High burst damage with variance |
| `trace_damp()`         | `stealth`, `support`   | Reduces trace gain during use |
| `echo_lag()`           | `chaos`, `delay`       | Delays ICE response |
| `dampener_hook()`      | `support`, `mod`       | Reduces RAM/CPU cost |
| `trojan_seed()`        | `payload`, `malware`   | Injects persistent infection |
| `anti_feedback()`      | `bio`, `stability`     | Suppresses physical feedback |
| `chain_repeater()`     | `repeat`, `unstable`   | Enables limited re-use |
| `pack_split()`         | `spread`, `multi`      | Affects multiple targets |
| `failover_branch()`    | `backup`, `fail`       | Allows re-roll on failure |
| `heat_echo()`          | `trap`, `signal`       | Spoofs trace post-execution |

> Snippets may be **visible**, **stealthed**, or **encrypted**.

---

## 🛠 ROM Crafting Process

### 1. **Choose Core**
- Sets the ROM’s core function
- Defines snippet compatibility and compile DC

### 2. **Attach Snippets**
- Slot up to N snippets depending on deck/core
- Flag any as `hidden` for stealth or deception
- Ensure synergy or accept increased risk

### 3. **Assign Flags**
Optional modifiers:
- `auto_eject()` – Disconnects on glitch
- `delayed()` – Executes after a delay
- `faux_persona()` – Spoofs a fake sender
- `fail_hard()` – Hard crash on failure (extra power)

### 4. **Embed Payload**
Attach secondary logic:
- `trojan`, `sniffer`, `logger`, `trace anchor`, etc.
- Can be hidden or disclosed
- Executed silently if not detected

### 5. **Compile**
```plaintext
D20 + Software Skill + Tool Bonuses vs Compile DC
```
- Success = Clean ROM  
- Partial = Glitched (tags: `unstable`, `leaky`, `residual`)  
- Failure = Corrupted (may auto-execute, trigger ICE, backfire)

---

## 💣 Execution Rules

- On `use rom` all **snippets execute in order**
- Hidden logic triggers silently unless revealed
- Any `payload` embedded will run with default or preset params
- Results may include trace, feedback, node alerts

Example:
```bash
use rom stealth_probe
→ reduces trace by 4
→ hidden payload transmits node index to "ZeroCool"
```

---

## 🕵️ Detection & Counterintelligence

- `analyze <rom>` lets players scan for hidden logic
```plaintext
Roll: D20 + InfoSec vs snippet.stealth_DC
```
- Success: reveals hidden components
- Failure: returns “clean”
- Detection may:
  - Trigger alerts
  - Log player in `grid.db`
  - Expose payload or sender identity

---

## ⚠️ Risk Matrix

| Threat              | Description |
|---------------------|-------------|
| `instability`       | Too many unstable snippets |
| `feedback`          | Poor logic synergy or failed safety layer |
| `trace_trigger`     | Signature too noisy or payload detected |
| `compile_fail`      | Failed ROM craft – glitches or backfires |
| `stealth_breach`    | Hidden logic discovered during analysis |
| `rogue_execution`   | Corrupted ROM executes unpredictably |

---

## 🧠 Sample DSL (Developer Scripting)

```bash
rombuild build("leech_protocol")
  .add("trace_damp(),dampener_hook()")
  .hide("trojan_seed()")
  .inject("trojan_seed()", "ZeroCool")
  .desc("A diagnostic ROM with hidden sniffer payload.")
  .compile()
```

---

## 🧬 Advanced System Hooks

- `at_use()` – Snippet’s runtime effect
- `db.injection_target` – Payload target
- `db.hidden_snippets` – Non-visible logic
- `db._result_log` – Execution output
- `rom.traced()` – Returns boolean if ROM triggered ICE trace
- `rom.payloads()` – Returns active hidden logic

---

## 🔥 Final Word

**ROMs are weapons. Spells. Sabotage. Lies in executable form.**  
You don’t install them. You conjure them.  
From dead code and shattered ICE memory, you summon power and burn it into motion.

In BLACKICE, every time you build a ROM, you’re writing your signature across the battlefield of the Net.

And someone’s always watching.
