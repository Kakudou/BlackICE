# 📖 BLACKICE Rulebook – Node Generation & Loot Tables

## 🗺️ 12. Node Generation Rules

### Node Tiers
| Tier | Description |
|------|-------------|
| T1   | Low-risk, public, basic data nodes |
| T2   | Moderately protected, personal or minor corp |
| T3   | High-value corpsec, encrypted hubs |
| T4   | Critical core net zones, blacksite nodes |

### Node Components
- **Entrypoints:** Number of access routes
- **Data Cores:** Loot or mission objective locations
- **ICE Presence:** Count and type of constructs
- **Flow Logic:** Conditional paths, logic locks, dead ends
- **Traffic Density:** Number of travelers, visibility risk

### Node Traps & Hazards
- Databombs
- Trace Loops
- Decoy Nodes
- Reroute Wormholes

### Procedural Elements
- Blueprint-based generation logic
- Each node carries:
  - Difficulty Rating (1–10)
  - Loot Tier Cap
  - Traffic Score (affects log risk)

---

## 🎁 13. Loot Tables & Rewards

### Loot Categories
| Type          | Description |
|---------------|-------------|
| ROMs          | Ready-to-run programs, from basic to legendary |
| Blueprints    | Crafting recipes or system maps |
| Materials     | Silicrete, Ghostfiber, Blackplate, rare ICE seeds |
| Credits       | Datacred + Rep Tokens |
| Logs          | Exposed chat records, trace maps, blackmail data |
| Access Keys   | Unlocks to hidden or private nodes |
| Backdoor Paths| Pre-linked node jumpways (can be traced) |

### Loot Roll Formula
`D20 + Loot Bonus + Node Tier Mod` vs Drop Table Threshold

### Drop Table Example (T3 Node)
| Roll Range | Reward Type |
|------------|-------------|
| 1–8        | Common ROM, trace map fragment |
| 9–14       | Blueprint + mid-tier credits |
| 15–18      | Rare crafting materials, stealth ROM |
| 19–20+     | Legendary payload + node access token |

### Modifiers
- **Program Used:** `trace_cleaner()` increases blueprint chance
- **Heat:** High heat reduces credit yield, increases log drops
- **Stealth Success:** Full stealth grants loot bonus and trace wipe



