# 📜 Node Access Roles & Privileges

In BLACKICE, a persona’s capabilities within a node are determined by their current access level. These define what commands and actions are available during a session.

---

## 🟢 Public Access
Minimal rights, reconnaissance and communication only.

- `ping_node()` – Probe the node's existence
- `list_exits()` – Identify exit paths
- `change_node()` – Navigate to another connected node
- `change_comm_mode()` – Adjust communication type:
  - **Persistent** (session-based)
  - **Segmented** (node-by-node relay)
  - **Authenticated** (secure handshake)
  - **Minima** (encrypted payloads)
- `speak()` – Send plaintext message
- `eject()` – Voluntarily disconnect from the node

---

## 🟡 User Access
Grants operational access to non-secure systems and files.

- `analyze_construct()` – Inspect active ICs or personas
- `detect_program()` / `detect_data()` – Discover active elements
- `detect_databomb()` – Identify digital traps
- `disarm_databomb()` – Attempt to neutralize a bomb
- `use_program()` – Execute node-resident programs
- `open_file()` / `edit_file()` / `create_file()` – Access file system
- `decrypt()` – Attempt decryption of accessible files
- `download_data()` – Retrieve visible information
- `perform_task()` – Fulfill node-specific functions or quests
- `attack()` – Engage IC or another persona (if allowed)

---

## 🟠 Security Access
Access to node protection systems and aggressive countermeasures.

- `delete_file()` – Remove or purge data
- `launch_ic()` – Deploy an ICE construct
- `disconnect_persona()` – Force-eject another user
- `read_profile()` – Inspect persona account details
- `restrict_connection()` – Block active link
- `trigger_alert()` – Broadcast trace event
- `read_access_log()` – Review recent log entries
- `crash_program()` – Force a software failure
- `reboot_program()` – Restart corrupted scripts
- `plant_databomb()` – Place traps in files or systems
- `update_program()` / `update_ic()` – Patch or upgrade defenses
- `restore_ic()` – Repair ICE routines
- `use_hacking_tools()` – Enable rogue-level actions
- `conceal_file()` – Hide data or executable logic

---

## 🔴 Admin Access
Master authority. Root-level control over node systems.

- `view_full_logs()` – Review all connection and stat logs
- `reboot_node()` – Reset the entire node
- `edit_node_appearance()` – Change visual/meta layer
- `crash_node()` – Force shutdown and instability
- `manage_accounts()` – Add/remove users or edit their privileges


