# 🧱 Node Structure & Contents

Nodes are the backbone of the cyberspace. Each one holds systems, defenses, data, and presence—yours or someone else's. Navigating or attacking a node involves understanding what it’s made of.

---

## 🧩 Core Components

- **Constructs**
  - Active entities tied to the node
  - Includes ICE (defensive AI), other personas, daemons, etc.

- **Programs**
  - Executables installed on the node
  - Used for defense, automation, task processing, or traps

- **Data**
  - Files, logs, encrypted payloads
  - Includes quest items, loot, secrets, or false trails

---

## ⚙️ Node Attributes

| Attribute      | Description |
|----------------|-------------|
| `energy_bar`   | Represents system stability (crash at 0%) |
| `equipment`    | Node-specific upgrades (passive defenses, filters, stealth walls) |
| `inventory`    | Stored data or programs |
| `skillsheet`   | Defines node-based resistances or trace manipulation |

---

## 🧠 Node-Level Actions

| Action              | Description |
|---------------------|-------------|
| `launch_ic()`       | Deploys ICE from local bank |
| `update_ic()`       | Applies patch or mutation |
| `reboot_program()`  | Attempts to restore stability of malfunctioning logic |
| `restore_ic()`      | Repairs ICE integrity post-conflict |
| `plant_databomb()`  | Traps an asset (program or file) with logic bomb |
| `conceal()`         | Masks file/program from scans |
| `scan_constructs()` | Broad sweep of known constructs in the node |
| `crash_program()`   | Force-error on a program (user or ICE) |
| `reboot_node()`     | Global system-level reboot (Admin only) |
| `crash_node()`      | Induce overload and system instability (Admin privilege) |

---

## 🧊 Node Security Infrastructure

- **Firewall**  
  Filters incoming connections, sets base difficulty for intrusion or spoofing.

- **ICE (Intrusion Countermeasures Electronics)**  
  AI-driven security agents deployed within nodes.

  | Type         | Function |
  |--------------|----------|
  | `Patrol`     | Detects intruders, logs movements |
  | `Guardian`   | Protects specific data or code regions |
  | `Supervision`| Verifies ICE health and reboots crashed instances |
  | `Combat`     | Engages and disables hostile intrusions |
  | `Spider`     | High-tier, multi-role ICE with predictive behavior |

---

## 🚨 Intrusion Protocols

Triggered on failed stealth, trace overload, or flagged program activity.

- Sends `access_id` of the attacker to all active ICE
- Elevates security (can downgrade persona profile)
- Triggers auto-deploy of `combat_ic`
- Increases trace pressure and comms surveillance


