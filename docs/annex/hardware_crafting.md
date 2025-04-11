# 🛠️ Annex: Cyberdeck Hardware Crafting

> In BLACKICE, hardware is not physical—it’s logic. Devices are compiled from executable subroutines extracted from the ruins of corrupted systems.

This annex provides a reference to the cyberdeck hardware crafting system, focusing on subroutine components, core architecture types, and examples.

---

## 🧬 What is Hardware in BLACKICE?

Hardware components are assembled from:

- **Architecture Cores** – Define the component type and logic structure
- **Subroutines** – Modular logic shards with tagged functions and effects

Hardware crafting is done entirely in the matrix using `compile_component()` logic.

---

## 🧱 Architecture Core Types

| Core Name               | Function                          |
|-------------------------|-----------------------------------|
| `cpu_core`              | Execution speed, cooldowns        |
| `ram_array`             | Load capacity for programs        |
| `cooling_shell`         | Heat resistance, overclock buffer |
| `filter_layer`          | Feedback resistance               |
| `power_cell`            | Uptime and reboot thresholds      |
| `signal_chassis`        | Trace signature dampening         |
| `module_interface`      | Adds mod slots to deck            |

---

## 💾 Subroutine Library

Below is a growing list of subroutines used for hardware compilation:

| Subroutine Name         | Tags              | Description |
|-------------------------|-------------------|-------------|
| `chrono_shift()`        | `timing`          | Speeds up program execution |
| `core_anchor()`         | `stability`       | Reduces compile DC |
| `spike_buffer()`        | `defense`, `RAM`  | Adds a passive RAM shield |
| `temp_flood_gate()`     | `cooling`         | Reduces heat buildup |
| `ghost_lattice()`       | `stealth`, `signature` | Lowers trace profile |
| `feedback_kill_loop()`  | `biofilter`       | Absorbs feedback spikes |
| `failsafe_jack()`       | `failover`        | Auto-ejects on crash |
| `silent_bus()`          | `cloaking`, `comm`| Obfuscates comm signature |
| `recursive_mem_clone()` | `RAM`, `unstable` | Temporary RAM boost with corruption risk |
| `echo_suppression()`    | `noise`, `trace`  | Hides program calls from ICE logs |
| `compile_shield()`      | `crafting`        | Prevents subroutine corruption |
| `retaliation_reflex()`  | `counter`         | Triggers self-defense action on attack |
| `signal_noise_bubble()` | `jammer`, `signal`| Suppresses comm tracking temporarily |
| `armor_baffling()`      | `defense`, `shell`| Enhances deck shell resistances |
| `biofeedback_damper()`  | `biofilter`       | Lowers physical feedback damage |
| `trace_spike_loop()`    | `trap`, `unstable`| Adds trace risk to aggressor |
| `cool_core_surge()`     | `cooling`, `burst`| One-time heat dump on trigger |
| `ghost_echo()`          | `stealth`, `residue`| Creates false persona on trace logs |
| `memory_shard_link()`   | `RAM`, `passive`  | Enables modular memory sharing |
| `compile_inverter()`    | `debug`, `chaos`  | Randomizes outcome for risky compile gambits |

---

## 🧠 Usage Tips

- Match subroutine tags to the core for reduced compile DC
- Avoid stacking too many `unstable` tags unless using a `compile_shield()`
- Stealthy builds benefit from `ghost_*` and `silent_*` routines
- Defensive decks lean on `biofilter`, `armor`, and `failsafe` tags
- Offensive / brute-force decks can run high `RAM`, `burst`, `counter` routines

---

Subroutines are loot, power, memory, and death all in one.  
To build better gear, you have to carve it from the bones of the Net.

Jack in. Break code. Recompile your future.

