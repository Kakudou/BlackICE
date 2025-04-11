# 🛠️ BLACKICE Rulebook – Hardware Crafting via Subroutines

> *“In the matrix, form is code. Strength is logic. Gear isn’t built—it’s compiled.”*

This section outlines how players construct cyberdeck components using logic fragments called **subroutines**.  
In BLACKICE, physical materials don’t exist—hardware is built by stitching together **functional routines** extracted from the net.

---

## 🧬 Concept Overview

Cyberdeck hardware isn’t forged—it’s **compiled** from subroutines, executable logic units harvested from defeated ICE, corrupted nodes, or legacy programs.

Each subroutine represents a **coded behavior** or **passive trait**, and by assembling them into an **architecture core**, a decker crafts new hardware components.

---

## 🧱 Crafting Overview

### 1. **Architecture Core**

Every piece of hardware is built from a blueprint-like object called an **architecture core**.

| Core Type         | Defines |
|-------------------|---------|
| `CPU Core`        | Execution speed, program queue |
| `RAM Array`       | Program load capacity |
| `Filter Layer`    | Biofeedback protection |
| `Cooling Shell`   | Heat mitigation |
| `Power Cell`      | Energy pool, reboot threshold |
| `Signal Chassis`  | Trace resistance, comm security |
| `Module Interface`| Passive slot expansion |

Each core determines:
- What **tags** are needed from subroutines
- How many slots it can accept
- Base instability and compile difficulty

--- 

### Modding & Overclocking
- **Overclock CPU** = +Speed, +Heat, +Crash chance
- **RAM Overload** = +Program count, risk of freeze or partial deck lockout
- **Component Fusion** = Combine two modules for hybrid effects

--- 

### Damage & Degradation
- Decks have integrity (100 max)
- Overuse, attacks, failed programs cause integrity loss
- Below 50%: Crashes become more likely
- 0%: System hard-crashes, locks player out for a duration (or boots them to node entry)

---

### 2. **Subroutines**

Subroutines are logic fragments with one or more tags and effects.

| Subroutine Name         | Tags            | Effects |
|-------------------------|------------------|---------|
| `chrono_shift()`        | `timing`         | Reduces program delay |
| `spike_buffer()`        | `defense`, `RAM` | Adds passive RAM shield |
| `failsafe_jack()`       | `failover`       | Auto-ejects on crash |
| `ghost_lattice()`       | `stealth`        | Lowers trace signature |
| `kernel_clone()`        | `RAM`, `unstable`| Adds temp RAM at risk of overflow |

Subroutines can be:
- Looted from ICE or system corpses
- Extracted via `extract_routine()` from broken gear
- Purchased on black markets
- Crafted through `subroutine_forge()` (advanced)

---

### 3. **Compiling Hardware**

Once a core and subroutines are ready, the player compiles the component.

#### Command:
```bash
compile_component(cpu_core_t2, [
    chrono_shift(),
    core_anchor(),
    kernel_clone()
])
```

#### System Roll:
```
D20 + [Engineering or Software skill] + [tool bonuses] vs Compile DC
```

- Success = Hardware is installed and stable  
- Mixed Success = Installed but unstable or glitch-tagged  
- Failure = Compilation fails, may corrupt a subroutine

---

## ⚠️ Compilation Variables

| Variable             | Impact |
|----------------------|--------|
| `compile_dc`         | Set by core tier and tag synergy |
| `subroutine synergy` | Matching tags may reduce DC |
| `instability tags`   | Some subroutines are cursed or volatile |
| `compile_mods`       | Special programs/tools that assist or hinder |

---

## 🔧 Post-Compile Integration

Once compiled, the hardware:
- Is installed into the deck via `equip_component()`
- Consumes system slots or module interfaces
- May carry **passive effects**, **triggered defenses**, or **stat boosts**
- Can be removed, replaced, or broken

---

## 🧪 Advanced Crafting Techniques

- `bind_subroutines()` – Fuses two subroutines into one high-risk hybrid
- `scramble_signature()` – Alters trace profile of crafted gear
- `implant_relic()` – Inserts ghost-coded subroutines (high reward, high risk)
- `analyze_ICE_residue()` – Converts ICE death log into usable code fragment

---

## 🛑 Failure Consequences

| Type           | Effect |
|----------------|--------|
| `corruption`   | Component includes unstable behavior |
| `burnout`      | One or more subroutines are lost |
| `trace_seed`   | Hardware leaks trace pings to ICE |
| `ghost_echo`   | Creates a false signal persona on compile |
| `system_lock`  | Deck requires full reboot to recover |

---

## 📌 Summary

- Hardware is logic. You build it with subroutines.  
- Crafting = Picking a core + slotting subroutines + compiling successfully.  
- Loot, reverse-engineering, and ICE kills give you the parts.  
- Failure isn’t just wasted effort—it could mark you forever.

Your deck is **as strong as the logic you stitch into it**.  
Don’t build safe. Build smart. Or build dangerous.

