# 🌐 Network, Comms & Social Layer – BLACKICE GDD

## 1. Network & Node Structure
- ASCII-based maps (grid) per node
- Flow-logic behind each tile (entry condition, triggers, path redirects)
- Node types:
  - Personal
  - Corp-sec
  - Black market hubs
  - Relay transit
- ICE Types:
  - Patrol (detects)
  - Guardian (protects)
  - Combat (attacks)
  - Supervision (verifies ICE)
  - Spider (active monitor + trace AI)
- Traffic triggers ICE even if player is not interacting directly

## 2. Comms System
- DM, Crew Chat, Hub Broadcasts
- Message types:
  - Plaintext
  - Encrypted (requires keys)
  - One-time pad (burn on read)
- Message states:
  - Corruptible
  - Spoofable
  - Hijackable (MITM tools)
  - Traceable via log leaks

## 3. Comms Programs
| Program | Effect |
|--------|--------|
| `GhostTalker()` | Sends untraceable DM |
| `EchoSnare()` | Logs comms in nearby nodes |
| `BlackInk()` | Alters chat history |
| `InjectMeme()` | Spoofs UI alerts/messages |
| `RelayLeech()` | Hijacks routed conversations through backdoors |
| `Whispershard()` | Encodes message for shard-only readers |
| `DeadEcho()` | Auto-deletes message on read |
| `ForkMessage()` | Sends different versions of same message |
| `GhostKey()` | Breaks encrypted crew chat temporarily |

## 4. Roleplay Hooks
- Players communicate to:
  - Trade intel
  - Set up ops
  - Deceive or bait others
- Logs can be:
  - Forged
  - Sold
  - Used to blackmail
- Comms feed into Heat and Rep systems depending on:
  - Visibility
  - Message manipulation
  - Trace discovery

