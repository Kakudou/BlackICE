
1) setup your python venv:
```bash
python3.13 -m venv .venv --prompt=PoC
source .venv/bin/activate
```

2) install requirements:
```bash
python -m pip install -e .
```

3) Then migrate the database for a first time:
```bash
evennia migrate
```

4) Then to run the server:
```bash
evennia start
```

5) Then to stop the server:
```bash
evennia stop
```

# BlackICE: Proof-of-Concept Journal

This folder is not about building *The Game™*.  
It's about **understanding how Evennia ticks**—one pulse at a time.

The goal of this Proof-of-Concept (PoC) is to **experimentally implement foundational mechanics** drawn from the conceptual DNA of the BlackICE universe. Think of it as a **sandbox** for testing systems, stress-testing logic, and defining the rules of our digital world—before actual gameplay enters the stage.

We're not optimizing. We're not polishing.  
We're learning by doing—**with intent**.

---

## Core Purposes:
- **Understand Evennia internals** (commands, sessions, puppeting, cmdsets, accounts, etc.)
- **Prototype mechanics in isolation** before designing systems for real
- **Test narrative scaffolding** like cybernetic login flows, ghost personas, node travel, and digital crafting
- **Build an experimental design lab** for future modular reuse

---

## Identified Steps (unordered and intentionally lightweight):

- [x] Custom connection screen with immersive prompts  
- [x] `register_persona`: Ghost-shell style account creation  
- [x] `login_persona`: Seamless persona authentication  
- [ ] Procedural **grid world** generation  
- [ ] Fibo-spiral placement of user node coordinates  
- [ ] A `GhostChamber` that **moves daily**—node instability  
- [ ] Movement between nodes  
- [ ] `use rom`: simple item interaction  
- [ ] Crafting ROMs  
- [ ] Crafting Cyberdecks  
- [ ] **Cyberdeck sheet**: minimal attributes display  
- [ ] **Node sheet**: state + coordinate display  
- [ ] **Persona sheet**: simplified profile interface  
- [ ] Inventory management  
- [ ] Node-based building (temp structures or upgrades)  
- [ ] Node hacking (light minigame or command trigger)  
- [ ] Peer-to-peer **trading**

---

Each of these will be built with **minimum effort to prove feasibility**.  
No full systems. No balance. No polish.  
Just **concept validation through code.**

---  

If it breaks, we learn.  
If it clicks, we iterate.

This is the forge. This is the path. This is BlackICE.

