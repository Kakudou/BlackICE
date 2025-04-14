# 📖 BLACKICE Rulebook – Stealth, Social & Comms

## 🕶️ 7. Stealth & Trace System

### Stealth Mechanics
- Each movement or action generates **Trace** (1–5 base)
- Use of stealth programs reduces trace gain
- Stealth Check: `D20 + Stealth + StealthMod` vs `ICE Detection DC`
- Success = Undetected
- Failure = Logged + Possible ICE alert

### Trace Tiers & Effects
| Trace % | Effect |
|---------|--------|
| 0–24    | Safe |
| 25–49   | ICE begins passive scans |
| 50–74   | Random patrols reroute toward you |
| 75–99   | System raises alert, logs transmitted to nearby nodes |
| 100+    | Lockdown. Combat ICE deployed, full trace initiated |

### Stealth Tools
| Tool         | Effect |
|--------------|--------|
| `shadowcloak()` | Reduces all trace gain by 2 per action |
| `silent_move()`  | Negates trace from next movement |
| `spoof_trace()`  | Rewrites trace location history |
| `falseID()`       | Fakes persona ID for 1 session |

---

## 🗣️ 8. Social Engineering & Comms

### Message Types
- **Plaintext**: Visible to all
- **Encrypted**: Requires shared keys or cracking tools
- **One-Time Pad**: Destroyed on read

### Chat Manipulation
| Action        | Roll Type |
|---------------|-----------|
| Spoof Message | `D20 + Logic + SpoofMod` vs Target Insight DC |
| Hijack Comm   | `D20 + Hacking` vs Node Comm Security DC |
| Edit Logs     | `D20 + Engineering` vs ICE Supervision DC |
| Plant Trojan  | `D20 + Hacking + Stealth` vs Trace DC |

### Message Payloads
- `inject_meme()`: Spoof system message (fake breach alert)
- `black_ink()`: Corrupt log history
- `relay_leech()`: Hijack chat routed through backdoored node
- `ghost_talker()`: Send message with no sender log

### Chat & Heat Impact
- Spoofed or intercepted comms increase **Heat** when detected
- Public manipulation in hubs may lower **Reputation** if exposed
- Crew comms can be compromised without alert if passive surveillance succeeds



