
# 💾 Programs, Options & Execution Logic

Programs—ROMs, payloads, scripts—are the heartbeat of BLACKICE ops.  
They’re loaded into your cyberdeck and executed within nodes or during encounters.

Programs can be offensive, defensive, stealthy, supportive, or downright malicious.  
They cost RAM, require time to boot, and can **crash, misfire, or corrupt**.

---

## 🧠 Program Categories

### 🛡 Security Programs
- `analyze()` – Scan for constructs, databombs, and hidden logic
- `encrypt()` – Lock a file or data stream
- `databomb()` – Trap an asset with logic-triggered damage
- `comm_control()` – Trace or restrict communication channels
- `medic()` – Stabilize nodes or restore corrupted programs

### 🧨 Hacking Programs
- `intrusion()` – Breach node defenses
- `lockpick()` – Bypass rights, deactivate databombs
- `decrypt()` – Crack encrypted data
- `stealth()` – Mask or forge your persona
- `crash()` – Force errors on programs or nodes

### ⚔️ Cybercombat Programs
- `attack()` – Standard digital damage to ICE or personas
- `blackhammer()` – Direct neural feedback assault (biofeedback)
- `armor()` – Reduce incoming code damage
- `biofeedback_filter()` – Absorbs physical feedback from ICE

### 📡 Electronic Warfare Tools
- `scan()` – Detect hidden nodes or trap constructs
- `sniffer()` – Eavesdrop on active comms
- `jammer()` – Disrupt outgoing transmissions
- `protocol_override()` – Override or hijack local comm logic

---

## ⚙️ Execution Logic

- **Load Cost:** Consumes RAM when loaded; some programs have persistent cost
- **Execution Time:** Delay before effect; modifiable via gear
- **Cooldown:** Required wait before reuse
- **Stability:** Risk of crash or malfunction (affected by heat, traits)

```plaintext
run ghost_spike()
→ [loaded: 3 RAM | execute in 2s | stability: 92%]
```

---

## 🧬 Program Options (Modifiers)

Programs can include optional modules or enhancements, either coded in manually or added via crafting or loot.

| Modifier           | Effect |
|--------------------|--------|
| `optimize()`       | Reduces processor and RAM load |
| `anti_crash()`     | Improves stability during high-heat operations |
| `fast_boot()`      | Reduces execution delay |
| `quick_shutdown()` | Interrupts execution safely |
| `usage_limit()`    | Restricts number of uses per encounter |
| `databomb_detector()` | Auto-detects traps during load |
| `hidden_node_detector()` | Reveals stealth nodes |
| `persona_tracker()` | Adds trace tag to targets |
| `backdoor_tag()`   | Adds persistent network link between nodes |
| `auto_eject()`     | Persona is ejected on overload or fail |
| `spoof_resist()` / `anti_scan()` / `anti_sniff()` | Blocks detection attempts |
| `corpse_protocol()`| Program executes upon deletion or ICE death |
| `bio_pierce()` / `armor_pierce()` | Boosts damage through filters or defense |
| `retaliation()`    | Auto-executes countermeasure if disabled |
| `poison()` / `anti_poison()` | Applies or counters lingering effects |
| `trap_logic()`     | Delays or obfuscates intent or output |

---

## ☣️ Special Flags

- `zone_effect` – Affects all entities in node (e.g., silence, slow)
- `cadaver()` – Script remains active after decker death (ghost code)
- `faux_persona()` – Masks program as something else
- `fake_option()` – Appears selectable but is a trap
