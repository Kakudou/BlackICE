# BLACKICE – Compile Grid Minigame GDD

## Overview
The Compile Grid is a core minigame mechanic used in BLACKICE during the crafting of both ROMs (programs) and Hardware (cyberdeck components). It introduces a strategic, spatial puzzle system that determines whether a player can successfully construct powerful logic-based tools.

## Purpose
To transform the act of crafting into a high-stakes interactive experience that:
- Rewards planning and experimentation
- Limits power through spatial constraints
- Allows emergent behaviors and unpredictable outcomes
- Integrates core gameplay themes of logic, control, and corruption

---

## Game Loop Integration
### Entry Points:
- `construct_rom <name>`
- `construct_component <name>`

These commands trigger:
- Creation of a logic draft shell
- Random generation of a compile grid
- Storage of crafting session state

### Logic Registration:
- `register_snippet <rom> <snippet>`
- `register_subroutine <hardware> <subroutine>`

Logic units are:
- Tetris-style shapes with tags
- Irretrievable once registered (locked-in resource)

### Trigger:
- `compile_rom <name>` or `compile_component <name>`
- Launches grid puzzle interface

---

## Grid Specifications
### Base Shape:
- Grid is a 2D matrix (6x6, 8x8, or irregular based on tier)
- Core Tier defines:
  - Grid size
  - Number of special cells
  - Base DC

### Cell Types:
- Normal
- Corrupted (increases instability)
- Trace Node (adds trace to ROM)
- Overclock Port (boosts output at risk)
- Locked Cell (unusable)
- Bonus Cell (reduces DC if filled)

---

## Logic Piece System
### Each logic unit (snippet/subroutine) includes:
- Name
- Tag list
- Shape (Tetris pattern)
- Effects on compile and execution

Units must:
- Be placed without overlap
- Touch all required dependencies
- Comply with grid rules

### Example Tags:
- `damage`, `bio`, `stealth`, `unstable`, `support`, `payload`, `trap`, `cloaking`, `signal`, `residue`, `failover`, `chaos`

---

## Adjacency Effects
When tags are adjacent, they may:
- Mutate other tags
- Add effects (residue, stealth field, malware propagation)
- Increase or decrease instability

Special interactions:
- Hidden + Payload = autonomous stealth trigger
- Malware + Support = support logic becomes trojan
- Chaos + Repeat = infinite loop potential

---

## Minigame Objectives
- Fit all logic blocks into the grid
- Connect required tag interactions
- Avoid corruption and instability

---

## Post-Grid Compile Roll
After placement:
- System runs: `D20 + Skill + Tool Mods vs Compile DC`
- Grid layout modifies DC (bonus/malus)

### Outcomes:
- Full success: Stable program/component
- Partial: Tagged with instability or glitches
- Fail: Logic destroyed or corrupted

---

## Development Requirements
### Engine Features:
- Grid rendering (CLI/ASCII + Browser Canvas)
- Shape placement with validation
- Tag-based adjacency engine
- Compile DC generator

### Player Feedback:
- Highlight tag synergy/conflicts
- Warn of corruption zones
- Visualize connection lines

---

## Optional Enhancements
- Community Blueprint Library (share shapes/layouts)
- Mutation Tracker (track which ROMs mutated how)
- Leaderboards for legendary ROMs
- ROM Vault history/log system

---

## Summary
The Compile Grid mechanic is a puzzle-strategy system that turns digital crafting into an artform of layout, risk, and tactical coding. It reinforces the world’s themes, encourages mastery, and makes every ROM or hardware component **truly earned.**
