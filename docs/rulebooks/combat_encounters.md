# 📖 BLACKICE Rulebook – Combat & Encounter Systems

## ⚔️ 11. Combat Encounters
Combat is triggered when stealth fails, ICE detects a threat, or a player initiates offensive action. Combat uses a round-based system in turn-based ops, or cooldowns + active timers in real-time.

---

## ⚡ Initiative
- **Turn-Based:**
  - `D20 + Speed + Mod` determines action order
- **Real-Time:**
  - Each action has execution time and cooldown (modified by gear + RAM usage)

---

## 🔄 Action Economy (Combat)
- Players have **2 Action Points** per round (turn-based)
  - Major Action = 2 AP (e.g. deploy attack program)
  - Minor Action = 1 AP (e.g. move, reload, toggle buff)
  - Free Action = 0 AP (comms, inspect, taunt)

---

## 🧊 ICE Combat AI
| ICE Type | Behavior |
|----------|----------|
| Patrol   | Attempts to trace and ping other ICE |
| Guardian | Shields data and counter-attacks if it's accessed |
| Combat   | Seeks persona, attacks cyberdeck directly |
| Spider   | Hybrid AI; can override, reroute, or replicate routines |

Each ICE has:
- **Integrity (HP)**
- **Attack Type** (code damage, biofeedback, trace spike)
- **Execution Timer** (attack every X turns or seconds)

---

## 🧠 Attack Resolution
### Formula
`D20 + Cybercombat + Program Bonus vs Target Defense`

### Damage Types
- **Code Damage:** RAM or program crash
- **Biofeedback:** Physical/mental pain to decker/Cyberdeck 
- **Trace Spike:** Increases Trace by 10–25% per hit

### Player Defense
- **Armor Programs:** Reduce code damage
- **Feedback Filters:** Absorb or deflect biofeedback
- **Evasion:** Reduces hit chance

---

## 📉 Defeat Conditions
- **Player Defeated:**
  - Crash: Disconnect + Trace logged
  - Hard-Kill: Deck damage forces lockout (lose payload + leave loot)

- **ICE Defeated:**
  - Deactivates
  - Logs may remain
  - Guardian ICE may attempt self-repair if not purged

---

## 🔥 Combat Modifiers
- **RAM Usage:** High RAM lowers evasion, increases cooldown
- **Heat:** Affects stability, may cause program misfire
- **Overclocking:** Boosts speed, risks overheating

---

## 💣 Special Effects
- **BlackHammer:** Biofeedback weapon; deals decker HP damage
- **CrashOverride:** Disables target's currently loaded program
- **PingFlood:** Forcefully fills trace log, triggers ICE swarm
- **SpoofKill:** Tricks ICE into disabling itself or allies



