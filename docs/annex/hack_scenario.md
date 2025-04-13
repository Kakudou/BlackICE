# 🧪 BLACKICE PvP Scenario Walkthrough – Full Cycle Example

> *"No simulation. No training wheels. Just real blood on digital asphalt."*

This example walks through a full attack-defense loop in BLACKICE, including preparation, infiltration, combat, escape, and post-breach analysis.

---

## 🎮 PLAYER ROLES

- **Attacker**: `ZeroCool`, a stealth specialist hacker
- **Defender**: `Vanta` – seasoned node architect with trap-heavy defenses

---

## 1. PREPARATION PHASE

### **ZeroCool (Attacker) Prepares**

- Loads Cyberdeck:
  - `leech_protocol()` (sniffer + auto-upload)
  - `trace_damp()` (stealth heat control)
  - `backdoor_tag()` (plant quick-return link)
  - `erase_log()` (cover identity)
  - `scan_pattern()` (detect ICE patrol behavior)

- Configures Deck:
  - RAM: 8 slots
  - ROM Slots: 6 (3 stealth, 2 attack, 1 utility)

- Target: `node:AE12C-Vanta`
  - High-rank user node
  - Suspected to hold rare compiled ROM cores

---

## 2. INFILTRATION PHASE

### **ZeroCool warps to target coordinate**

- Enters via passive traversal, crossing 6 nodes
  - **3 nodes detect traversal**, 1 triggers log
  - Heat level starts at 0, climbs to 8 on entry

### **Inside Vanta’s node:**

- Fog of War active
- ZeroCool uses:
  - `scan_cell(C2)` → Reveals proxy router
  - `trace_damp()` → Heat reduced from 12 → 6
  - `scan_pattern()` → Detects ICE guard sweep every 10min

- ZeroCool marks likely asset at `D4`, low activity zone

---

## 3. DETECTION EVENT

- Attempts to `peek_log()` entry on `C1`
  - Minor failure: triggers alert + ICE check
- Heat jumps to 42
- **ICE “Patrol-7” detects presence**
- Node switches to **combat mode**

---

## 4. COMBAT PHASE

### **Defender ROMs Activate (pre-loaded)**

- `grid_morph()` shuffles node layout (ZeroCool loses map data)
- `blackout_patch()` executes: ZeroCool can’t scan for 2 turns
- `heat_surge()` adds 25 heat → now at 67

### **ICE Patrol-7 locks target and opens combat**

- ICE uses:
  - `bio_feedback_burst()` → inflicts 2 RAM damage
  - `lock_area()` → seals cells `D3–E4` temporarily

### **ZeroCool Response**

- Uses `leech_protocol()` to steal log fragments from ICE
- Deploys `backdoor_tag()` on exit node (B1)
- Fires `erase_log(entry:access_AE12C)` → success, logs cleared

---

## 5. ESCAPE PHASE

- ICE attempts `trace_ping()` but fails (trace signature now spoofed)
- ZeroCool runs `stealth_boost()` and exits via manual route through C3 → B1
- Escapes node with:
  - Partial log package
  - Extracted ICE patrol script
  - Personal trace level: 3 (low, due to cleanup)

---

## 6. POST-BREACH (DEFENDER RESPONSE)

### **Vanta Logs In**

- Alert received: `Minor breach detected on AE12C`
- Reviews:
  - Logs: Entry missing (tampered)
  - ICE-7 report: Patrol interrupted at 04:12:33
  - System logs: ROM `heat_surge()` auto-executed on schedule
  - Network ping echo from B1

### **Analysis Actions**

- Runs `cross_log_check()` → detects log overwrite on access file
- Confirms breach via secondary ICE memory (guard-3 report)
- Identifies likely persona by reverse-linking trace from B1 exit node

### **Remediation**

- Rewrites patrol script to scan logs **every 3min**
- Replaces `grid_morph()` ROM with `signal_scrambler()` for variety
- Purges infected proxy router at `D4`
- Tags `ZeroCool` with `intruder_profile()` for future encounters

---

## 🧠 Takeaways

| Role        | What Worked                            | What Failed                         |
|-------------|-----------------------------------------|--------------------------------------|
| **ZeroCool** | Stealth heat management, log erase, mapped patrol | Got caught scanning logs too early  |
| **Vanta**    | Automated defense scripts, defensive ROM synergy  | ICE scan loop too slow to react     |

---

## Result: Draw

- Attacker escapes with intel and some loot
- Defender detects and adapts for next breach
- The war between minds continues...

--- 

*Every encounter writes history. Every breach leaves scars.*

