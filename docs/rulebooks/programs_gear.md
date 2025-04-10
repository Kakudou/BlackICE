# 📖 BLACKICE Rulebook – Programs & Gear

## 💾 5. Program Types & Mechanics

### Program Categories
| Type     | Description |
|----------|-------------|
| Attack   | Damages ICE or users (e.g. `BlackHammer`, `Overflow`) |
| Defense  | Protects deck integrity (e.g. `RAMShield`, `FeedbackFilter`) |
| Utility  | Enhances function, logistics (e.g. `log_cleaner`, `trace_spoof`) |
| Stealth  | Conceals persona, modifies trace/logs (e.g. `ghost()`, `shadowcloak()`) |

### Program Attributes
- **Tags**: `attack()`, `decrypt()`, `logger()`, `spoof()`, `backdoor()`
- **RAM Cost**: Memory required to run
- **Cooldown**: Turns or seconds before reuse
- **Stability**: % chance of crashing per run (increases with Heat or overload)
- **Detection Rating**: Difficulty for ICE to detect (Stealth programs only)

### Program States
| State    | Result |
|----------|--------|
| Active   | Consumes RAM, runs per loop or action |
| Dormant  | Loaded, but inactive. Ready to deploy |
| Crashed  | Failed to run, must be rebooted or restored |
| Corrupted| May cause unintended effects, e.g. misfire, leak logs |

## 🦾 6. Cyberdeck Gear System

### Core Components
| Component      | Function |
|----------------|----------|
| CPU Core       | Determines program execution speed |
| RAM Modules    | Determines number of programs loaded |
| Cooling Unit   | Affects overheating and program stability |
| Feedback Filter| Absorbs or mitigates biofeedback damage |
| Stealth Module | Reduces trace gain, improves spoof/stealth success |

### Modding & Overclocking
- **Overclock CPU** = +Speed, +Heat, +Crash chance
- **RAM Overload** = +Program count, risk of freeze or partial deck lockout
- **Component Fusion** = Combine two modules for hybrid effects

### Damage & Degradation
- Decks have integrity (100 max)
- Overuse, attacks, failed programs cause integrity loss
- Below 50%: Crashes become more likely
- 0%: System hard-crashes, locks player out for a duration (or boots them to node entry)

### Repair Tools
- `deck_patch()`: Temporary fix
- `hardware_restore()`: Requires workshop or techie
- `auto_reboot()`: Built-in failsafe, can misfire



