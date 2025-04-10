# 📖 BLACKICE Rulebook – Crafting & Blueprint System

## 🧪 10. Crafting System Overview
Crafting in BLACKICE allows players to create custom ROMs and cyberdeck gear by combining resources, components, and blueprints. All crafted items can have visible and hidden traits.

---

## 🧠 ROM Crafting (Software)
### Crafting Steps
1. Select ROM shell (size, shape, RAM capacity)
2. Select capabilities (tags):
   - `decrypt()`, `logger()`, `backdoor()`, `autoEject()`, etc.
3. Fit capability blocks into the ROM shell (via Compiler Puzzle)
4. Roll: `D20 + Engineering + Workshop Mod` vs DC

### Outcome Tiers
| Roll Result | Result |
|-------------|--------|
| ≤ DC        | Faulty ROM, may crash or misfire |
| DC+1 to DC+4| Stable ROM with standard performance |
| DC+5 to DC+9| Optimized ROM (reduced RAM use / faster exec) |
| DC+10+      | Legendary ROM: hidden passive effect (e.g. spoof immunity, echo-leech)

need to evaluate the DC base on the engineering skill so legendary stay legendary.

---

## 🛠️ Hardware Crafting (Cyberdeck)
### Crafting Paths
- Blueprints for deck components:
  - CPU Core, RAM, Filter, Stealth Mod, Cooling, Power Unit
- Components require:
  - Raw materials (Silicrete, Ghostfiber, Blackplate, etc)
  - Engineering toolkits or workshop access

### Assembly
- Roll: `D20 + Engineering + Component Bonus`
- Component synergy adds +1–3 per match (e.g. Filter + Stealth Mod)
- Failure = degraded part / instability

### Enhancement Options
- **Overclocked Core**: +Speed, +Crash Risk
- **Fused RAM**: Combine RAM sticks for higher burst but higher heat
- **Adaptive Shells**: Morph part traits in combat (stealth to shield)

---

## 🔍 Hidden Traits & Corruption
- Every crafted item has a chance to carry hidden flags:
  - **Passive trace beacon**
  - **Data leak**
  - **Spoofable signature**
  - **Self-degrade at Heat threshold**
- High Engineering adds detection pre-deployment
- Programs like `inspect_core()` or `ROM_cleanse()` can verify or patch hidden flags

---

## 📦 Crafting Materials & Storage
- Materials stack in secure stashes or node lockers
- Weight/volume simulated in mobile deck cache
- Rarer parts are node-bound unless uploaded



