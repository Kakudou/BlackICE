## 🧠 BLACKICE DEV ROADMAP (Evennia Edition)

> Agile. Modular. Combat-tested.

---

### 🔰 **PRE-SPRINT 0 – FOUNDATION**
- ✅ Set up version control (GitHub/GitLab)
- ✅ Fork + install Evennia
- ✅ Create custom game skeleton: `blackice` project dir
- ✅ Configure environments (local/test/staging)
- ✅ Import rulebook + GDD into Notion/Wiki

---

## 🧪 SPRINT 1 – CORE STRUCTURE 

### 🎯 Goal: World architecture + core commands bootstrapped

#### Tasks:
- [ ] Override base `Character` to `Persona` (custom stats, RAM, trace, heat)
- [ ] Create `NodeRoom` (custom room class for BLACKICE nodes)
- [ ] Implement basic commands:
  - `connect`, `disconnect`, `scan`, `move`, `talk`, `inspect`
- [ ] Build CLI parser base for D20 roll integration
- [ ] Hook up `Skill` stat and `RAM` limits
- [ ] Base logging system (local trace log)

#### Deliverable:
✅ Players can connect, walk through node-rooms, and see trace logs being built

---

## 💾 SPRINT 2 – PROGRAMS & RAM SYSTEM 

### 🎯 Goal: ROM system + RAM restrictions + program actions

#### Tasks:
- [ ] Create `Program` objects (ROMs) with tags + effects
- [ ] Build `program_loader` and `unload`
- [ ] Enforce RAM capacity + check on each run
- [ ] Implement core programs:
  - `ghost()`, `spoof_trace()`, `decrypt()`, `logger()`
- [ ] Basic failure/stability logic (`crash`, `overload`)

#### Deliverable:
✅ Players can load/run programs, get RAM overflow messages, and spoof traces

---

## 🧊 SPRINT 3 – ICE & TRACE SYSTEM 

### 🎯 Goal: Reactive ICE, escalation based on player trace

#### Tasks:
- [ ] Create ICE templates (`Patrol`, `Guardian`, `Combat`)
- [ ] Add ICE state machine logic (`Passive`, `Defensive`, `Aggressive`)
- [ ] Implement `trace_level` mechanics
- [ ] ICE activates based on logs, trace %, player profile
- [ ] Add `alert()` trigger and escalation paths

#### Deliverable:
✅ ICE patrols, spots runners, attacks based on trace thresholds

---

## ⚔️ SPRINT 4 – COMBAT & DAMAGE SYSTEM 

### 🎯 Goal: Cybercombat loop with D20 rolls and program interaction

#### Tasks:
- [ ] Add cybercombat command: `attack`, `blackhammer`, `eject`
- [ ] Integrate D20 roll: `D20 + skill + modifiers vs ICE defense`
- [ ] Apply RAM/program loss, feedback, and crash
- [ ] Support ICE response + loot drops on defeat
- [ ] Log combat events into trace history

#### Deliverable:
✅ Turn-based combat with ICE, working damage, and loot responses

---

## 💣 SPRINT 5 – NODE SYSTEM & LOOT 

### 🎯 Goal: Procedural node structure + loot + access logic

#### Tasks:
- [ ] Expand `NodeRoom` to include:
  - Tier level, loot tables, ICE density
- [ ] Add procedural node generator (template-based)
- [ ] Implement loot command + randomized ROM/material drops
- [ ] Add node `access_key` and `backdoor` items
- [ ] Trace logs leave footprint through visited nodes

#### Deliverable:
✅ Players raid procedurally generated nodes, find loot, and risk detection

---

## 🕷️ SPRINT 6 – COMMS & ROLEPLAY LAYER 

### 🎯 Goal: Fully reactive chat system + spoofing and corruption

#### Tasks:
- [ ] Override comm system to allow encrypted/plaintext messages
- [ ] Implement spoof tools: `inject_meme()`, `ghost_talker()`, `black_ink()`
- [ ] Hook chat events into trace/heat modifiers
- [ ] Allow comm hijack via node-based MITM positioning

#### Deliverable:
✅ Roleplay layer with attackable comms, log injection, and passive surveillance tools

---

## 🚀 SPRINT 7 – TEST OPS & BALANCING 

### 🎯 Goal: MVP polish, test runs, and balance passes

#### Tasks:
- [ ] Playtest stealth op, brute force op, loot op
- [ ] Tune roll DCs, RAM caps, cooldowns
- [ ] Add failsafes: auto-eject, heat decay, trace dampener
- [ ] Clean CLI output, reinforce parser fail feedback
- [ ] Deploy demo server for remote tests

#### Deliverable:
✅ Fully playable test run with character sheet, ops loop, ICE reaction, loot drop

---

## 📈 OPTIONAL SPRINTS (Post-MVP)
- 🧩 Advanced crafting system (blueprints, mods)
- 📦 Data market + black market vendors  
- 🧠 War 
- 🔥 Event engine 
- 🌐 Web client 
- 📱 Mobile UI 
- ...

---

## 👁️ Summary Timeline (Agile Agile Agile)

| Focus              | Milestone                     |
|--------------------|-------------------------------|
| Setup              | Repo, Evennia, docs live      |
| Core Framework     | Persona, nodes, parser        |
| Programs & RAM     | Run logic, spoof tools        |
| ICE + Trace        | Escalation + combat triggers  |
| Cybercombat        | Full player/ICE encounter     |
| Loot + Nodes       | Procedural ops, rewards       |
| Comms & Spoofing   | Chat spoof / corruption       |
| Playtest + Polish  | MVP launch run                |
