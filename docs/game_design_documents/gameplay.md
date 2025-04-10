# 🎮 Core Gameplay Systems – BLACKICE GDD

## 1. Node Building
- ASCII-based grid layout with visual ICE placement
- Flow logic scripting behind the scenes to control:
  - ICE patrol paths
  - Data access conditions
  - Traps, honeyfiles, databombs
- Upgradeable modules for node security (RAM, bandwidth, stability)

## 2. Infiltration
- Real-time or turn-based parser interface
- Player executes commands like:
  - `decrypt firewall`
  - `spoof_trace`
  - `extract data_core`
- Each action triggers skill checks:
  - `D20 + Skill + Program/Deck Mod` vs `DC`
- Programs burn RAM + Heat
- Success/failure affects trace level, ICE reaction

## 3. Traversal
- Nodes are connected across a webbed Cyberspace
- Reaching a node requires hop traversal (1–X)
- Each hop adds:
  - Time cost
  - Log signature left behind
  - Passive ICE scan chance
- Routing tools:
  - `spoof()`, `reroute()`, `transcloak()`
- Backdoors skip traversal but link nodes permanently (high risk)

## 4. Crafting
- ROMs and hardware are modular
- Programs crafted with tags:
  - `attack()`, `logger()`, `backdoor()`, `autoEject()`
- Hardware blueprints contain:
  - RAM modules, CPU cores, feedback filters
- Use crafting stations, black market kits, or crew techies
- Skill rolls determine:
  - Hidden traits (exploits, crashes)
  - Max tier support

## 5. Combat
- Triggered via ICE, defense, or forced detection
- Action stack based on:
  - Initiative (Speed stat or Surprise)
  - Program used (e.g. `BlackHammer`, `NeuroScramble`)
- Combat rolls:
  - `D20 + CyberCombat + Program Bonus` vs `ICE Defense` or vice versa
- Player damage types:
  - Code damage (program lockouts)
  - Biofeedback (user damage)

## 6. Minigames
- Optional, high-reward or mission-critical
- **Log Cleaner:** Match patterns to erase traces
- **Trace Delay:** Tap/timer mini-skill to extend stealth time
- **Compiler Puzzle:** Assemble capability blocks to fit limited ROM shell space
- **RAM Juggle:** Time-limited inventory shuffle to avoid program crash
