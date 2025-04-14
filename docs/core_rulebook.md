# **BLACKICE – Core Rulebook**

---

## **Chapter 1: Introduction to BLACKICE**

### **What Is BLACKICE?**

BLACKICE is a cyberpunk-themed multi-user dungeon (MUD) where players inhabit a dynamic, ever-evolving digital grid. Every action you take—every line of code you run, every step through cyberspace—is part of a larger, living system. In BLACKICE, your avatar is not a passive presence. It is your mind made manifest: a persona forged of code, logic, and will.

The game merges real-time tactical movement, skill-based challenges, customizable programs, and programmable defenses into a single interactive experience. Whether you are breaching a secure node, crafting a volatile executable, or writing defense code to protect your territory, BLACKICE transforms every action into a meaningful decision.

---

### **Design Philosophy**

BLACKICE is built on three core principles:

1. **Agency through Mechanics**  
   Every system is transparent, interactive, and offers strategic depth. You’re not watching numbers—you’re making decisions that shape outcomes.

2. **Risk-Reward Gameplay**  
   Success is never guaranteed. Systems are balanced to reward creativity and punish carelessness. You can win big—but only if you're willing to risk failure.

3. **Player-Driven World**  
   Every player controls a node in the global cyberspace. Nodes can be fortified, invaded, and evolved. Alliances can be formed. Rivalries can be built. The world moves with its players.

---

### **Core Gameplay Loop**

At the heart of BLACKICE is the digital conflict between attackers and defenders:

- **Explore** the cyberspace grid, locating valuable nodes.
- **Intrude** using stealth and custom-crafted programs.
- **Battle** hostile ICE or player defenses when detected.
- **Escape** with the data—or lose everything.
- **Build** your node’s defenses, ICE behavior, and programs.
- **Adapt** to evolving threats, factions, and global events.

---

### **Key Features**

- **Tactical Grid-Based Movement**: Navigate your persona through node matrices in real time or turn-based modes.
- **Custom Crafting Systems**: Build both hardware and executable programs using logic fragments you collect or design.
- **Programmable ICE**: Defend your node with custom-scripted AI using a simple domain-specific language (DSL).
- **Stealth and Trace Mechanics**: Operate beneath the radar—or burn through defenses with overwhelming power.
- **Faction Warfare and Events**: Influence the larger world through reputation, politics, and dynamic global shifts.

---

### **System Requirements (Player Experience)**

- A text-based interface (CLI or Telnet client)
- Basic command-line literacy
- Curiosity, creativity, and a willingness to learn systems and tactics
- No coding experience required, but deeper scripting features exist for advanced users

---

# **Chapter 2: Core Mechanics & Resolution System (Updated Edition)**

---

## **2.1 Dice Resolution System**

BLACKICE uses a unified D20-based system to resolve actions across every system—whether you’re compiling a ROM, evading ICE, or reprogramming node defenses.

```plaintext
D20 + Skill + Modifiers ≥ Difficulty Class (DC)
```

- **D20**: A 20-sided die generates the base roll.
- **Skill**: One of six core abilities your persona develops.
- **Modifiers**: From ROMs, hardware, node effects, environmental pressure, or special tools.
- **DC**: The target difficulty for the action. Set by system complexity, ICE pressure, or node tier.

### **Result Types**

| Roll Outcome     | Result Description                            |
|------------------|----------------------------------------------|
| Equal or Higher  | Success – the action resolves cleanly.       |
| Lower            | Failure – the action misfires, is blocked, or triggers a consequence. |

---

## **2.2 Persona Skills**

BLACKICE features six distinct skills, each reflecting a core axis of play:

| Skill          | Description |
|----------------|-------------|
| **Stealth**     | Navigate the grid undetected. Suppress trace generation, bypass ICE scans, and operate silently. |
| **Engineering** | Design and craft physical deck components using Subroutines and Architecture Cores. Manages compile stability and hardware integrity. |
| **Programming** | Construct and compile executable ROMs from modular logic blocks (Snippets). Governs compile success, synergy effects, and mutation risk. |
| **Cybercombat** | Engage in direct code warfare. Used for resolving attacks, deploying offensive ROMs, and resisting digital assaults from ICE or rival deckers. |
| **Architecture** | Configure node systems and ICE behaviors. Used for scripting defenses, corrupting logs, building trap networks, and node reprogramming. |
| **Presence**     | Control your digital signature. Used for misdirection, false identity projection, spoofing trace data, and escaping detection. |

---

## **2.3 Action Economy**

BLACKICE supports two operational modes: **Turn-Based** and **Real-Time**. Each mode has distinct action mechanics.

### **Turn-Based (Combat / Grid Ops)**

- Each persona receives **2 Action Points (AP)** per round.
  - **Major Action** = 2 AP (e.g., deploy attack ROM, crack ICE)
  - **Minor Action** = 1 AP (e.g., move one cell, toggle module)
  - **Free Action** = 0 AP (e.g., chat, inspect, ready tool)

### **Real-Time (Exploration / Passive Mode)**

- Each action has:
  - **Execution Time** (duration in seconds)
  - **Cooldown** (delay before it can be used again)
- Cooldown and execution time are affected by system load, RAM usage, Heat, and equipped hardware.

---

## **2.4 Difficulty Classes (DCs)**

BLACKICE calibrates challenge level using standard difficulty tiers:

| Tier        | DC Range |
|-------------|----------|
| Basic       | 10–12    |
| Moderate    | 13–16    |
| Hard        | 17–20    |
| Brutal      | 21–24    |
| Impossible  | 25+      |

DCs are applied to all resolved actions: stealth checks, compilation rolls, ICE interactions, trace evasion, log manipulation, and more.

---

## **2.5 Trace & Heat System**

Your actions generate **Heat**—a measure of how visible your presence is within a node. As Heat rises, your **Trace Level** increases.

- Trace Level is tracked from 0 to 100+
- Every action (movement, hacking, crafting, messaging) adds to your Trace
- Crossing Trace thresholds triggers escalating defensive responses

| Trace Level | Effect |
|-------------|--------|
| 0–24        | Low visibility; safe. |
| 25–49       | ICE begins passive scans and proximity logging. |
| 50–74       | ICE alters patrol paths; increased detection chances. |
| 75–99       | System alarm raised; logs broadcast to nearby nodes. |
| 100+        | Lockdown: Combat ICE deployed, trace-to-source begins. |

### **Managing Trace**

- Use **Stealth ROMs** to reduce gain or spoof location.
- High **Stealth** and **Presence** skills help mask actions or rewrite your footprint.
- Logs can be manually altered, wiped, or forged (see Section 2.6).

---

## **2.6 Log Manipulation**

Every node you interact with logs your presence by default.

Players can interfere with the log system using Architecture-based tools:

| Action         | Roll Required |
|----------------|----------------|
| **Wipe Logs**  | `D20 + Stealth` vs ICE detection DC |
| **Corrupt Logs** | `D20 + Architecture` vs System Integrity DC |
| **Forge Logs** | `D20 + Engineering` + proper template |

Log entries can be:
- **Deleted** to erase tracks.
- **Corrupted** to mask real activity with noise.
- **Forged** to frame others or obscure true intent.

---

# **Chapter 3: Personas, Programs, and Hardware**

---

## **3.1 Persona Overview**

A **Persona** is the player's presence inside the grid—a digital projection of will and identity. It serves as both the interface and the combatant within BLACKICE. Your Persona is customizable through:

- **Installed ROMs** (Programs)
- **Equipped Hardware Components**
- **Chosen Skills** and specializations
- **Trace and Heat footprint**
- **ICE behavior responses based on past activity**

This modularity ensures that no two Personas play the same. Your toolkit defines your approach—stealth operative, brute-force attacker, trap architect, or digital ghost.

---

## **3.2 ROMs – Runtime Operative Modules**

ROMs are executable digital constructs—modular programs built from **Snippets** and designed to be used in tactical scenarios. Each ROM is built from scratch, making every execution unique and player-authored.

### **ROM Attributes**

| Attribute        | Description |
|------------------|-------------|
| **Type**         | Determines program category: `attack()`, `spoof()`, `decrypt()`, etc. |
| **RAM Cost**     | Required memory to execute. |
| **Cooldown**     | Time or turns before the ROM can be used again. |
| **Instability**  | Chance of misfire or glitch on execution. |
| **Detection Rating** | How likely ICE is to identify the ROM. Relevant to stealth payloads. |

---

### **ROM Anatomy**

Each ROM consists of the following components:

| Component        | Role |
|------------------|------|
| **Core**         | Defines ROM category and baseline function. |
| **Snippets**     | Logic modules that provide effects, traits, or payloads. |
| **Flags**        | Optional behavior modifiers (e.g., `auto_eject`, `delayed`). |
| **Payloads**     | Stealthed or hidden logic that may trigger secondary actions. |
| **Description**  | Metadata for player reference and UI tracking. |

---

### **Snippet Examples**

| Snippet             | Tags                   | Effect |
|---------------------|------------------------|--------|
| `trace_damp()`      | `stealth`, `support`   | Reduces trace during use |
| `burst_logic()`     | `damage`, `unstable`   | High-damage burst with risk |
| `failover_branch()` | `backup`, `fail`       | Allows re-roll on failure |
| `trojan_seed()`     | `payload`, `malware`   | Hidden persistent infection |

Snippets can be flagged as **visible**, **hidden**, or **encrypted** for stealth layering.

---

### **ROM Execution Rules**

- Executing a ROM triggers all its Snippets in order.
- Hidden logic (payloads) may activate silently unless revealed.
- Instability rolls are made if tags like `unstable`, `residual`, or `chaos` are present.
- ROMs that crash may leak trace data or trigger ICE countermeasures.

---

### **Programming Skill Impact**

Your **Programming** skill influences:

- Max number of snippets attachable
- Compile DC of the ROM
- Risk of tag mutations
- Success rates on stealth payload integration

---

## **3.3 Hardware Components**

Hardware defines your Persona’s loadout, memory capacity, defenses, and passive systems. Hardware is crafted using **Architecture Cores** and **Subroutines**, and it determines how many ROMs you can load, how long you last in combat, and whether you survive a trace strike.

---

### **Core Types**

| Core Type         | Function |
|-------------------|----------|
| **CPU Core**      | Program execution speed and queue size |
| **RAM Array**     | Determines how many ROMs can be loaded |
| **Filter Layer**  | Shields against biofeedback damage |
| **Cooling Shell** | Controls Heat gain and overclocking |
| **Power Cell**    | Determines energy reserve and failover capacity |
| **Signal Chassis**| Controls trace resistance and comm security |

Each core sets:
- Base stats (RAM, Integrity, Stability)
- Compile DC baseline
- Required Subroutine tags for synergy

---

### **Subroutines**

Subroutines are logic fragments that enhance or alter hardware behavior.

| Subroutine          | Tags            | Effect |
|---------------------|------------------|--------|
| `chrono_shift()`    | `timing`         | Reduces ROM delay |
| `ghost_lattice()`   | `stealth`        | Reduces trace signature |
| `kernel_clone()`    | `RAM`, `unstable`| Temporary memory boost |
| `failsafe_jack()`   | `failover`       | Ejects Persona on crash |

Subroutines can be:
- Looted from ICE
- Extracted from defeated nodes
- Purchased on black markets
- Forged via advanced compilation

---

### **Engineering Skill Impact**

Your **Engineering** skill determines:

- Max number of Subroutines slotting
- Compile success and post-compile instability
- Ability to fuse or bind Subroutines
- Failure consequences during crafting (e.g., trace leaks, glitches)

---

### **Compile Mechanics**

Both ROMs and Hardware are compiled through the **Compile Grid Minigame**, covered in Chapter 4. Success depends on:
- Correct spatial placement
- Tag synergy
- Use of tools or modifiers
- Final compile roll

---

**Persona Loadout Summary:**

| Category  | Governed By   | Built Using       |
|-----------|---------------|-------------------|
| ROMs      | Programming   | Snippets          |
| Hardware  | Engineering   | Subroutines       |
| Node AI   | Architecture  | ICE Scripts       |

---

# **Chapter 4: The Compile Grid & Crafting Minigame**

---

## **4.1 Overview: What Is the Compile Grid?**

In BLACKICE, crafting isn’t handled through static menus or abstract timers. It’s a **spatial puzzle system**—a live logic construct called the **Compile Grid**. It manifests when you begin crafting either:

- A **ROM** (program) using Snippets
- A **Hardware Component** using Subroutines

This system transforms crafting into a tactile, visual, and strategic experience.

---

### **Key Principles**

- The grid’s size and complexity scale with:
  - Craft tier
  - Player skill (Programming or Engineering)
  - Compile environment (node condition, interference, ICE pressure)

- Logic blocks (Snippets or Subroutines) are presented as **Tetris-like shapes** with embedded tags and traits.

- Placement rules must be respected to complete a valid compilation.

---

## **4.2 Crafting Flow**

### **Step 1: Initialization**

- Player triggers:
  - `construct_rom <name>` or `construct_component <name>`
- The system responds by:
  - Generating a random Compile Grid
  - Creating an empty draft shell
  - Registering the attempt as “in progress”

---

### **Step 2: Register Logic Units**

- Use:
  - `register_snippet <rom> <snippet>`
  - `register_subroutine <hardware> <subroutine>`
- Each block:
  - Appears as a unique shape
  - Carries tags and function data
  - Is consumed on failure (resources are not recoverable)

---

### **Step 3: Puzzle Phase – The Minigame Begins**

- Goal: **Place all logic blocks onto the grid**
- Constraints:
  - No overlaps or overhangs
  - Blocks may need to connect to ports (e.g., `input`, `output`, `payload`)
  - Certain tags require adjacency to activate (e.g., `support` must touch `malware`)
  - Environmental hazards and bonuses exist on the grid

---

## **4.3 Grid Features & Special Zones**

| Zone Type         | Effect |
|-------------------|--------|
| **Corrupted Cells** | Block placement or destroy blocks placed over them |
| **Trace Nodes**     | Connect to your signature, increasing Trace if touched |
| **Chaos Cells**     | Randomly mutate tag behavior or shape geometry |
| **Overclock Ports** | Boost output, but raise Instability if occupied |

Strategic use of zones is vital—sometimes a small risk yields a major boost.

---

## **4.4 Tag Adjacency System**

Certain tag combinations alter behavior when touching each other on the grid:

| Tag A       | Tag B       | Interaction |
|-------------|-------------|-------------|
| `bio`       | `unstable`  | Triggers biofeedback surge on failure |
| `stealth`   | `payload`   | Payload remains hidden even under scan |
| `trap`      | `signal`    | ICE receives false trace pings |
| `repeat`    | `chaos`     | May trigger infinite loop behavior |
| `backup`    | `deception` | Fakes program crash, deploys clone |

These interactions can reduce the compile difficulty—or drastically increase instability.

---

## **4.5 The Compile Roll**

After successful block placement, the system performs the final **Compile Check**:

```plaintext
D20 + Programming (for ROMs) or Engineering (for Hardware)
+ Tool Bonuses + Adjacency Synergy – Instability Penalties
≥ Compile DC
```

### **Compile Outcomes**

| Roll Range | Result |
|------------|--------|
| 1–5        | Total failure; corruption or trace seed |
| 6–10       | Failed compile; components lost |
| 11–15      | Unstable success; adds glitch tag |
| 16–19      | Clean success |
| 20+        | Bonus trait, stealth enhancement, or hidden payload slot unlocked |

---

## **4.6 Failure States & Consequences**

| Condition      | Effect |
|----------------|--------|
| **Corruption** | Code becomes unpredictable; may trigger on its own |
| **Mutation**   | Snippet/Subroutine gains unexpected tag or behavior |
| **Trace Seed** | Program logs the creator signature on use |
| **Instability**| Raises crash chance on every future use |
| **Burnout**    | One or more blocks destroyed on compile attempt |

Failure isn’t just a lost effort—it might follow you across sessions.

---

## **4.7 Tools & Modifiers**

Advanced users can influence compile outcomes using tools or passives:

| Tool Name           | Effect |
|---------------------|--------|
| `compile_shield()`  | Negates mutation on failure |
| `debug_chip()`       | Reduces compile DC by 2 |
| `chaos_lens()`       | Guarantees tag mutation but lowers instability |
| `grid_anchor()`      | Locks one logic piece in place, can’t be removed |
| `stabilizer_loop()`  | Suppresses adjacency penalty effects |

Players can stack tools tactically—but some tools increase Heat or Trace on use.

---

## **4.8 Design Intent**

The Compile Grid:

- **Prevents automation and min-maxing** by requiring spatial problem-solving
- **Promotes creative builds** by rewarding risky synergy
- **Transforms crafting into a tactical challenge** instead of a background process
- **Allows infinite variation**, since no two grids or tag interactions are identical

---

# **Chapter 5: ICE, Nodes, and Grid Defense**

---

## **5.1 Node Ownership & Structure**

Every player in BLACKICE controls a personal **Node** on the global cyberspace grid. A Node is your digital stronghold—part base, part puzzle, part battlefield.

### **Node Anatomy**

- **Matrix Layout**: Cellular grid (e.g., 8x8 or scalable) where ICE, assets, and traps are placed.
- **Assets**: Logs, data cores, vaults, backdoors, and utility objects.
- **Entry Points**: Defined starting positions for intruders.
- **Exit Routes**: Can be locked, hidden, or protected by ICE.

Nodes are fully explorable by other players—every cell is physically occupied and traveled through.

---

## **5.2 ICE (Intrusion Countermeasure Entities)**

ICE are autonomous security programs designed to monitor, defend, and retaliate against threats inside your Node.

Each ICE unit has:

- **Type**: Patrol, Guardian, Combat, Spider, or Supervisor
- **Behavior Loop**: A script that defines how it reacts to intruders
- **Execution Timer**: Determines when it acts
- **Tags**: Define special effects, weaknesses, or immunities
- **Resources**: May carry ROMs, trigger traps, or deploy decoys

---

### **ICE Types & Behavior**

| Type       | Role |
|------------|------|
| **Patrol**     | Scans logs, reports anomalies, moves predictably |
| **Guardian**   | Defends static assets, activates on proximity |
| **Combat**     | Aggressively pursues targets with attack ROMs |
| **Spider**     | Hybrid—can reroute, replicate, or fake signals |
| **Supervisor** | Monitors other ICE, restarts disabled defenses |

Each ICE has an **Integrity score (HP)** and unique attack vectors (trace spikes, feedback loops, RAM floods).

---

## **5.3 ICE Behavior Programming**

Nodes are programmable using an in-game **DSL (Domain-Specific Language)** designed for MUD environments. No coding knowledge is required—just clear logic and intent.

### **Programming Example**

```plaintext
> config_ice patrol_alpha
Editing behavior for ICE "patrol_alpha"
(type .save to compile, .help for keywords)

every: 2min
do: scan_logs()

if: persona_heat > 50
then:
  - activate(combat_ice_3)
  - log("High-heat signature detected")

if: persona_location = D3
then:
  - move(patrol_alpha, D3)
  - deploy_rom(trace_swap())
```

### **ICE Script Blocks**

| Component     | Function |
|---------------|----------|
| `every:`      | Defines a repeating timer |
| `if:`         | Triggers based on condition (heat, location, logs) |
| `then:`       | Actions taken on trigger success |
| `do:`         | Passive recurring actions |
| `on_detect:`  | Reacts to player presence |
| `trap_zone()` | Deploys ROM traps in specific cells |
| `alert_defender()` | Notifies the node owner or logs a trigger |

Scripts are sandboxed, parsed, and validated in real-time. They live in `ICE.db.behavior_tree`.

---

### **Architecture Skill Impact**

The **Architecture** skill directly influences:

- Script complexity and number of conditions allowed
- ICE logic parsing speed and execution priority
- Access to advanced conditions (e.g., nested if-statements, location tags)
- Post-breach forensic tools and automatic behavior overrides

---

## **5.4 Node Defense Programming**

Beyond ICE, players can configure their entire node grid:

| Tool           | Description |
|----------------|-------------|
| `grid_morph()` | Rearranges grid layout post-breach |
| `blackout_patch()` | Obscures ICE signals for a duration |
| `bio_pulse()`  | Triggers area-based feedback stun |
| `trace_swap()` | Rewrites the intruder’s signature |

Defender ROMs can be **pre-scripted** to activate on conditions—just like ICE scripts.

---

## **5.5 Environmental Cells & Terrain Effects**

Certain node cells carry passive effects that shape player movement:

| Cell Type         | Effect |
|-------------------|--------|
| **Shadow Zone**     | Reduces trace from actions |
| **Firewall Cell**   | Increases Heat on entry |
| **Locked Zone**     | Requires key or backdoor |
| **Trap Node**       | Activates scripted effects on contact |
| **Line-of-Sight Cell** | Blocks or enhances detection from ICE |

These cells are combinable and can be triggered dynamically by ICE or scripts.

---

## **5.6 Post-Intrusion Recovery**

After a successful or failed breach, defenders can:

- Review system logs
- Trace the intruder’s identity
- Reconfigure ICE patrols
- Deploy decoys
- Install countermeasures for future visits

Advanced defenders can even **learn from attacks**, creating evolving nodes that adapt over time.

---

# **Chapter 6: Intrusion, Combat, and Escape**

---

## **6.1 The Global Cyberspace Grid**

The world of BLACKICE is a massive, evolving network of interconnected Nodes, laid out in a **spiral formation** that favors early adopters with distance and security.

- **Node Traversal**:
  - Use cardinal movement (`move north`, `move west`) or direct targeting (`move C4`)
  - Each movement may trigger passive scans, trace gain, or ICE reaction

- **Fog of War**:
  - Unexplored nodes are obscured until scanned or traversed
  - Defenders can refresh this fog to conceal new layouts

---

## **6.2 Stealth Phase: The Infiltration Begins**

When entering a node, you begin in **stealth mode**. Every action you take generates **Heat**, which contributes to your **Trace Level**.

### **Heat Gain Table**

| Action               | Heat Gain | Notes |
|----------------------|-----------|-------|
| `move`               | +2        | Modified by cell type |
| `stealth_move()`     | +0–2      | Consumes RAM; reduced trace |
| `scan_cell()`        | +5        | Reveals grid or assets |
| `hack_asset()`       | +10       | High-risk action |
| Using a ROM          | Varies    | Depends on Instability & Tags |

### **Detection Thresholds**

| Trace %   | ICE Response |
|-----------|--------------|
| 0–24      | Safe         |
| 25–49     | Passive scans and logging begin |
| 50–74     | ICE begins rerouting toward your position |
| 75–99     | System raises alarm; log transmission starts |
| 100+      | Combat ICE deploys and node locks down |

The **Stealth** skill and tools (like `shadowcloak()` or `spoof_trace()`) help mitigate detection risk.

---

## **6.3 Combat Phase**

When you're detected, the node enters **combat mode**. ICE behavior trees activate and the attacker is locked in visible status.

### **Combat Modes**

- **Turn-Based**: Used for precision ops or high-tier nodes
- **Real-Time**: Used in faster raids or low-tier environments

Combat is resolved using the standard dice system:

```plaintext
D20 + Cybercombat + ROM Modifiers ≥ ICE Defense
```

### **Actions per Turn (Turn-Based)**

| Action Type   | AP Cost |
|---------------|---------|
| Deploy ROM    | 2 AP    |
| Move to Cell  | 1 AP    |
| Interact / Hack | 1 AP  |
| Communicate / Inspect | Free |

---

## **6.4 Damage Types**

| Type         | Description |
|--------------|-------------|
| **Code Damage**   | Crashes programs or depletes RAM |
| **Biofeedback**   | Inflicts mental damage; may force disconnect |
| **Trace Spike**   | Rapidly increases Trace by 10–25% per hit |

### **Defense Options**

- **Armor Programs**: Absorb code damage
- **Feedback Filters**: Mitigate biofeedback effects
- **Presence Skill**: Reduces hit chance or re-routes target lock

---

## **6.5 Intrusion Tactics**

| Tactic          | Tool/Skill           | Benefit |
|-----------------|----------------------|---------|
| **Trace Spoofing** | `spoof_trace()`, Presence | Delays detection or misleads ICE |
| **ROM Chains**     | Programming         | Combos of payloads, traps, and triggers |
| **Log Disruption** | Architecture        | Deletes or forges your presence |
| **Overclocking**   | Hardware-based      | Faster actions, higher risk |

Skilled intruders prepare layered ROMs, use trap disarms, or modify terrain in real time.

---

## **6.6 Escape Phase**

When the job’s done—or when things go bad—you need to get out.

### **Escape Conditions**

- Reach a **grid edge** or designated **backdoor cell**
- Use `eject()` command (requires cooldown)
- Delay ICE using stealth tools or jammers

### **Evacuation Tools**

| Tool               | Effect |
|--------------------|--------|
| `trace_damp()`     | Slows trace increase |
| `jam_trace()`      | Freezes ICE pursuit for X turns |
| `falseID()`        | Temporarily erases you from logs |
| `residue_fake()`   | Leaves misleading signature on exit |

Careless exits leave trails. Strategic departures erase you completely.

---

## **6.7 Failure States**

If your Persona is defeated:

| Outcome       | Result |
|---------------|--------|
| **Crash**     | Forced disconnect; Trace logged |
| **Hard-Kill** | Lose active ROMs; gear may be flagged or exposed |
| **Data Leak** | ICE may capture your payload, revealing code to the defender |

Post-crash recovery depends on node tier and deck integrity.

---

# **Chapter 7: Communication, Deception, and Social Engineering**

---

## **7.1 Communication Systems**

BLACKICE features an integrated messaging framework that blends roleplay, tactical deception, and system-layer subterfuge.

### **Message Types**

| Type           | Description |
|----------------|-------------|
| **Plaintext**   | Readable by anyone. Logged openly in node history. |
| **Encrypted**   | Requires a matching decryption key or `decrypt()` ROM. |
| **One-Time Pad**| Can be read once. Self-deletes after delivery. |

Messages can be used for direct communication or as **delivery systems** for digital traps, payloads, or false intel.

---

## **7.2 Chat Manipulation Tactics**

These are high-risk, high-reward actions governed primarily by the **Presence** and **Architecture** skills. They target player communications, logs, and the perception of events.

| Action         | Roll Type |
|----------------|-----------|
| **Spoof Message**  | `D20 + Presence + Mod` vs Target Insight DC |
| **Hijack Comm**    | `D20 + Architecture` vs Node Comm Security DC |
| **Edit Logs**      | `D20 + Architecture` vs ICE Supervision DC |
| **Plant Trojan**   | `D20 + Programming + Stealth` vs Trace DC |

These moves allow attackers to reshape narratives inside the grid—altering what defenders see or believe.

---

## **7.3 Communication Payloads**

Some ROMs or tools carry **communication-specific payloads** that can alter node behavior or influence social outcomes:

| Payload          | Function |
|------------------|----------|
| `inject_meme()`  | Broadcasts fake alerts or system messages |
| `black_ink()`    | Corrupts chat history or node logs |
| `relay_leech()`  | Intercepts messages routed through compromised nodes |
| `ghost_talker()` | Sends messages with no sender trace or return path |

Payloads can be embedded inside ROMs or attached to terminal scripts, hidden from surface scans.

---

## **7.4 Social Manipulation & Reputation**

Deception actions affect a player’s standing in the world of BLACKICE.

### **Positive Outcomes**

- Convincing players to lower defenses
- Masking your presence in faction operations
- Avoiding ICE attacks via false credentials

### **Negative Consequences**

- Public exposure of forgery attempts
- Traceable payloads leading to faction penalties
- Reduced access to black market resources if trust is broken

Reputation systems are persistent and track both direct outcomes and subtle manipulations.

---

## **7.5 Surveillance and Passive Threats**

Not every defense screams. Some **listen**.

| Surveillance Tool | Effect |
|-------------------|--------|
| `passive_scan()`  | Logs message metadata and patterns |
| `comm_ghost()`    | Creates decoy persona in chat feeds |
| `metadata_bait()` | Embeds trace anchors in reply chains |

The defender's Architecture skill determines how advanced their passive systems can become. With high skill, even your silence may leave footprints.

---

## **7.6 Strategic Applications**

Social engineering blends with gameplay in the following systems:

| System        | Use Case |
|---------------|----------|
| **Factions**  | Mislead or turn rival crew members |
| **Events**    | Seed panic or disinformation during a node war |
| **Log Warfare**| Frame another player for your intrusion |
| **ICE Scripts**| Modify behavior based on faked messages or trace IDs |

These tools turn BLACKICE into more than a hacking sim—it becomes a political, strategic, and psychological battlefield.

---

# **Chapter 8: Factions, Events, and the Living Grid**

---

## **8.1 Factions Overview**

In BLACKICE, power is not static. It moves through **Factions**—entities that control territory, resources, and influence within the global grid. Factions can be NPC-driven, player-created, or emergent collectives.

### **Faction Types**

| Type             | Traits |
|------------------|--------|
| **Megacorporations** | Own high-security nodes. Hostile to intrusion. |
| **Corpos**       | Smaller subsidiaries. Valuable, less protected. |
| **Rogue AIs**    | Evolving, unstable behavior. Not always hostile—but unpredictable. |
| **Netrunner Clans** | Player-led crews with node territory and shared defenses. |
| **Neutral Syndicates** | Black market dealers, info brokers, non-aligned operators. |

Each faction has its own agendas, resources, and relationships with players.

---

## **8.2 Faction Mechanics**

- Players can:
  - **Join** or **form** factions
  - **Control** or **liberate** nodes in their name
  - **Contribute** to faction reputation through ops
  - **Access** special gear, ROMs, and black market tools

- Faction alignment affects:
  - ICE behavior toward the player
  - Prices in marketplaces
  - Access to rare crafting materials
  - PvP targeting and bounty eligibility

---

## **8.3 Territory Control & Node Wars**

Nodes can be flagged as:

- **Controlled** – Defended and occupied by a faction
- **Contested** – Under active siege or recon
- **Liberated** – Unclaimed or freshly purged

Factions may initiate **Faction Ops** to:

- Plant persistent backdoors
- Hijack ICE behavior
- Override grid layout or obscure logs

### **Dynamic Node War Events**

When nodes go to war, a unique rule set is triggered:

- Timed capture windows
- Live ICE mutation under stress
- Boosted rewards for attackers
- Risk of permanent trace leak for defenders

Node wars are visible on the global grid and open for outside interference.

---

## **8.4 World Events**

BLACKICE is designed to evolve dynamically, even when players aren’t logged in. The system generates global **Events** that affect all nodes, factions, and operations.

### **Event Types**

| Event             | Trigger |
|-------------------|---------|
| **Node War**      | Conflict escalates between factions |
| **AI Awakening**  | Rogue AI achieves singularity—alters ICE logic across a region |
| **Black Market Flush** | Rare goods flood shops, but trace risk increases |
| **Trace Storm**   | System-wide ICE upgrade; detection DCs rise sharply |
| **Grid Collapse** | Temporary system failure; logs wiped, chaos spreads |

Events are real-time or time-locked. They may reward players who respond—or punish those who ignore the signs.

---

## **8.5 Player Politics & Reputation**

Reputation is a living variable. It defines your relationship with factions, NPCs, and the wider player base.

### **High-Reputation Players Can:**

- Influence faction policy
- Post global bounties
- Modify market exchange rates
- Represent factions in events or diplomacy

### **Reputation Decay**

| Action                | Effect |
|-----------------------|--------|
| Inactivity            | Reputation slowly degrades |
| PvP Losses            | Heavy defeats reduce standing |
| Event Failure         | Faction backlash, restricted access |
| Stealth Exposure      | Leaks and trace trails damage reputation |

Players can regain reputation through contracts, victories, or social maneuvering.

---

## **8.6 Living Grid Mechanics**

The global cyberspace is alive.

- **Node Logs** accumulate over time
- **ICE Behavior** adapts if not reset
- **Markets** shift with player activity and event outcomes
- **Scripts and Traps** persist until disabled, not just when the player is online

The system ensures that no player is an island. You leave marks. You inherit consequences. You write history.

---

# **Chapter 9: Minigames and Subsystems**

---

## **9.1 Minigame Purpose**

Minigames in BLACKICE represent **critical digital actions** that require more than a roll. They simulate the complexity, timing, or stress of real-time hacking maneuvers.

They appear when:
- Engaging high-tier systems
- Failing certain passive rolls
- Triggered by ICE behavior
- Crafting or interacting with volatile systems

Minigame outcomes directly affect trace, access, resource loss, or system crash.

---

## **9.2 List of Core Minigames**

### **1. Log Cleaner**

| Purpose         | Erase system trace logs |
|-----------------|-------------------------|
| Gameplay        | Pattern-match strings under time pressure |
| Difficulty Mod  | Based on Trace Level and ICE activity |
| Success         | Logs deleted, trace history erased |
| Failure         | ICE ping, rollback, or false clean report |

---

### **2. Trace Delay**

| Purpose         | Delay ICE or trace triggers |
|-----------------|-----------------------------|
| Gameplay        | Time-based input sequences (e.g., button taps, keystrokes) |
| Heat Effect     | The faster your Heat rises, the harder the pattern becomes |
| Success         | Buys time before next ICE or detection stage |
| Failure         | Immediate trace escalation; trigger chain begins |

---

### **3. Compiler Puzzle**

| Purpose         | Live ROM crafting under RAM constraints |
|-----------------|-----------------------------------------|
| Gameplay        | Real-time block fitting (Tetris-like grid logic) |
| Failure States  | Unstable ROM, boot crash, hidden glitches |
| Success Bonus   | Synergistic tag bonuses or hidden payload unlocks |

> This puzzle runs in real-time during `compile_rom` and `compile_component` actions and replaces static crafting bars.

---

### **4. RAM Juggle**

| Purpose         | Prevent overload during ICE attack or program spam |
|-----------------|----------------------------------------------------|
| Gameplay        | Quickly move active programs to safe RAM slots |
| Environment     | Real-time pressure; ICE adds debuffs as timer ticks |
| Success         | Active programs preserved; no crash |
| Failure         | Random crashes, deck freeze (1–3 turns), or forced ROM ejection |

---

### **5. Firewall Cracker**

| Purpose         | Silent access past node firewalls |
|-----------------|-----------------------------------|
| Gameplay        | Pattern replication or wire-color matching under ICE timers |
| Structure       | Multi-stage challenge (defenders can have layered firewalls) |
| Success         | Stealth access; backdoor route opened |
| Failure         | ICE logs alert; countermeasures launch |

---

## **9.3 Difficulty Scaling**

Each minigame has four difficulty tiers:

| Tier     | Gameplay Impact |
|----------|------------------|
| **Easy**     | Generous timers, simple patterns |
| **Moderate** | Increased pace, limited hints |
| **Hard**     | Fast timers, decoys, pattern inversion |
| **Extreme**  | Randomized inputs, ICE interference, tool-lock penalties |

Difficulty scales dynamically based on:
- Node tier
- ICE aggression level
- Trace pressure
- Player condition (e.g., RAM load or hardware instability)

---

## **9.4 Stat Integration**

Minigames aren’t isolated—they pull from player stats and gear:

| Modifier           | Affected Minigame |
|--------------------|-------------------|
| **Logic Skill**        | Reduces Firewall & Cleaner difficulty |
| **Programming**        | Lowers Compile Puzzle DC and speeds |
| **Engineering**        | Boosts RAM Juggle capacity |
| **Hardware Tools**     | Some tools (e.g., `compile_shield()`, `auto_anchor()`) provide minigame fail-safe bonuses |

Your deck and loadout define whether these systems are barriers—or opportunities.

---

## **9.5 Optional or Required?**

- **Optional** in low-tier nodes or simple systems
- **Required** for:
  - High-value nodes
  - Encrypted loot
  - Elite faction vaults
  - Rare ICE defeat sequences

If you’re aiming for the top tiers of BLACKICE, mastering minigames is not a choice—it’s survival.

---

# **Chapter 10: Advancement, Progression, and Player Growth**

---

## **10.1 Skill Advancement**

Players evolve through action, not grinding. Skills level independently based on use:

| Skill          | How It Improves |
|----------------|------------------|
| **Stealth**     | Successful undetected operations, trace reduction |
| **Engineering** | Crafting or modifying hardware, fusing subroutines |
| **Programming** | Building ROMs, successful compilations |
| **Cybercombat** | Combat encounters, program-based victories |
| **Architecture** | ICE scripting, node defense design, log manipulation |
| **Presence**     | Successful deception, spoofing, message tampering |

Each skill levels with diminishing returns to maintain balance but always rewards mastery.

---

## **10.2 Persona Growth**

### **Stat Milestones**

As players progress, they unlock **Milestones**:

- **+Slot Capacity** (RAM, Subroutines, Snippets)
- **+Minigame Tool Use**
- **Access to High-Tier ROM Flags** (e.g., `faux_persona()`, `fail_hard()`)
- **Passive Perks** (e.g., reduced Heat gain, faster cooldowns)

Milestones occur at key skill thresholds or reputation markers.

---

## **10.3 Loadout Expansion**

You don't just grow stronger—you grow more complex.

### **Deck Expansion Paths**

| Upgrade         | Source |
|-----------------|--------|
| **Architecture Cores (T3+)** | Faction markets or event rewards |
| **Modular Interfaces**       | Unlocks passive modules or hybrid ROM slots |
| **Legacy Ports**             | Enables relic integration or corrupted tech |
| **Backdoor Slots**           | Hides payloads inside hardware components |

Players must choose carefully—some upgrades introduce instability or trace risk.

---

## **10.4 Reputation Tracks**

Reputation is not linear. It splits into parallel **Reputation Tracks** based on actions:

| Track         | Description |
|---------------|-------------|
| **Uplink**    | Trusted systems operator—clean hacker, faction-aligned |
| **Downlink**  | Mercenary agent, neutral or wildcard |
| **Ghost**     | Operates in silence, leaves minimal trace |
| **Echo**      | Known manipulator of others—frames, false logs, social tools |
| **Dead Signal** | Detected rogue; hunted by ICE, factions, or player bounties |

Each track unlocks different perks, vendors, and missions. Your reputation isn’t just who you are—it’s what you have access to.

---

## **10.5 Player Identity & Impact**

### **Persistent Signature**

- Each player leaves a unique **trace fingerprint**
- Can be scrubbed, spoofed, or cloned—but it always exists somewhere
- Nodes remember who broke them, who died inside them, and who walked out clean

### **Node Evolution**

- Your personal node evolves with you
- High-skill Architecture players can:
  - Create adaptive ICE
  - Trigger reactive scripts based on attacker ID
  - Log behavioral trends and auto-modify defense trees

### **Digital Immortality (Optional)**

Advanced players may pursue **construct status**—converting their persona into a persistent ICE or AI construct inside the grid, leaving behind a trace-bound legacy.

---

## **10.6 Endgame Philosophy**

BLACKICE has no traditional endgame—because in this world, the war never ends.

Instead, players focus on:

- **Dominating Grid Sectors**
- **Becoming Legends in Faction Lore**
- **Mastering Rare Crafting Techniques**
- **Writing Self-Defending Nodes**
- **Influencing Global Events via Player-Driven Actions**

You’re not climbing a ladder. You’re etching your name into the net’s architecture.

---

## **Final Thought**

Your growth in BLACKICE is not gated by time, stats, or gear.

It’s earned through understanding.  
Through mistakes.  
Through outwitting a system designed to evolve with you.

**Every compiled ROM, every broken ICE, every message spoofed is a step in writing your story into the bones of the Grid.**

---

