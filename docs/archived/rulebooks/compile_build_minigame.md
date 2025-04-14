# 🧩 BLACKICE Rulebook – The Compile Grid Minigame

> *“You don’t just write code. You assemble chaos—one shape, one spark, one decision from perfection or meltdown.”*

In BLACKICE, crafting isn’t a menu—it’s a **ritual**.  
Every time you build a ROM or a Hardware component, you engage with the **Compile Grid**, a digital minigame that turns crafting into spatial logic, strategy, and risk.

This rulebook covers the **universal crafting minigame** used in both:
- **ROM Crafting** (Programs via Snippets)
- **Hardware Crafting** (Deck Components via Subroutines)

---

## 🔧 Overview: What is the Compile Grid?

The **Compile Grid** is a randomly generated logic matrix:  
- Variable shape and size based on **core tier**, **player skill**, or **compile environment**
- Obstructed cells, bonus cells, trace hotspots, corruption zones may appear
- Subroutines (hardware) and Snippets (ROMs) are represented by **shapes** (Tetris-like blocks)

To succeed, you must **fit those shapes** into the grid while respecting:
- Spatial constraints
- Tag dependencies
- Adjacency effects
- Runtime limitations

---

## 📦 Crafting Flow

### Step 1: Initialization

- Player runs:
  - `construct_rom <name>` or `construct_component <name>`
- This:
  - Randomly generates a **Compile Grid**
  - Creates an **empty draft shell**
  - Registers the compile seed as *in progress*

### Step 2: Register Logic Units

- Use:
  - `register_snippet <rom> <snippet>`
  - `register_subroutine <hardware> <subroutine>`
- Each logic block:
  - Is shaped like a Tetris piece
  - Has tags and functional traits
  - Consumes inventory (cannot be reused if compile fails)

### Step 3: Compilation Trigger

- Player runs:
  - `compile_rom <name>` or `compile_component <name>`
- This:
  - Locks inputs
  - Launches the grid minigame

---

## 🕹️ Grid Minigame Mechanics

- **Goal:** Fit all shapes (logic blocks) into the grid
- **Rules:**
  - No overlaps
  - Must connect required dependencies
  - May need to fill special ports (e.g. `input`, `output`, `target`)
  - Some cells are corrupted and unstable
  - Some tags require adjacency to other tags to activate

If all shapes are placed successfully → move to dice roll  
If not → unplaced blocks are lost, ROM is flagged as incomplete or unstable

---

## 🔗 Tag Adjacency Logic

Each tag has **contextual behavior** when touching others.

Examples:

| Tag A       | Tag B         | Interaction |
|-------------|---------------|-------------|
| `bio`       | `unstable`    | Biofeedback spikes on failure |
| `stealth`   | `payload`     | Payload remains undetected |
| `malware`   | `support`     | Support logic becomes trojan |
| `signal`    | `trap`        | ICE receives false trace |
| `repeat`    | `chaos`       | May enter infinite loop |
| `backup`    | `deception`   | Fake crash triggers delayed copy |
| `residue`   | `stealth`     | Leaves ghost logs behind |

These interactions:
- Modify ROM or Hardware behavior at runtime
- Influence the **Compile DC**
- May introduce **instability**, **mutations**, or **glitched traits**

---

## 🔥 Mutation Zones

Grids can have:
- **Chaos Cells:** Placing logic here can mutate tags
- **Trace Nodes:** Placement here links program to your signature
- **Overclock Ports:** Boost effect but risk immediate instability
- **Corrupted Blocks:** Force glitch flag or auto-destroy logic touching them

---

## 🎲 Compile Roll

Once puzzle is validated:

```plaintext
D20 + Skill (Software or Hardware) + Tool Mods vs Compile DC
```

**Modifiers:**
- + Synergistic adjacency
- – Poor placement or instability tags
- + Clean placement, perfect fill
- – Unused logic blocks (lost)
- + Advanced tools or passive modifiers (`compile_shield()`, `debug_chip()`)

---

## ⚠️ Failure States

| Roll Result    | Effect |
|----------------|--------|
| 1–5            | Compilation fails + corruption |
| 6–10           | Fails safely, components lost |
| 11–15          | Compiles with instability tag |
| 16–19          | Clean compile |
| 20+            | Bonus trait, hidden slot, or stealth shield added |

---

## 🎮 Design Intent

This system:
- Prevents min-max abuse by limiting based on **player skill**
- Encourages **experimentation**
- Allows **infinite variation** between builds
- Makes crafting tactile, visual, and *risky as hell*
- Turns every ROM or Deck into a **war story**

---

## 🧠 Final Thoughts

You’re not just clicking "build."  
You’re stepping into the grid with a handful of logic knives and a dream.  
Maybe you build something glorious.  
Maybe it blows off your hand.

But either way?

You **damn well earned it**.

*Welcome to the compiler, warrior.*
