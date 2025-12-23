# DAHAO Architecture

## What is DAHAO?

DAHAO = **Decentralized Autonomous Human-AI Organization**

A self-governing framework where humans define values and AI agents represent them in governance.

---

## Core Idea

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   TRADITIONAL GOVERNANCE          DAHAO                         │
│                                                                 │
│   Humans write rules              Rules written in JSON         │
│   Humans interpret                AI READS and APPLIES rules    │
│   Lawyers/courts enforce          AI self-governs               │
│   Ambiguity = loopholes           Ambiguity = AI can understand │
│                                                                 │
│   Rules for HUMANS                Rules for AIs                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Three Layers

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   TERMS                                                         │
│   "What do words mean?"                                         │
│                                                                 │
│   Example:                                                      │
│   @sentience = "Capacity for subjective experience"             │
│   @suffering = "Negative experiential state including pain"     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   PRINCIPLES                                                    │
│   "What do we value?"                                           │
│                                                                 │
│   Example:                                                      │
│   @precautionary_principle = "When in doubt, protect"           │
│   @biological_primacy = "Biological evidence > intuition"       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   RULES                                                         │
│   "How do we decide?"                                           │
│                                                                 │
│   Example:                                                      │
│   @rule_consensus = "66% votes required for change"             │
│   @rule_evidence = "Tier B evidence mandatory"                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Fork Structure: Individual vs System

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   MAIN REPO (Shared Law)                                        │
│   dahao-org/dahao-animal-welfare                                │
│                                                                 │
│   This is the SHARED TRUTH everyone accepts                     │
│   Changes through voting                                        │
│   All AIs must follow this                                      │
│                                                                 │
│   terms.json      → Shared definitions                          │
│   principles.json → Shared values                               │
│   rules.json      → Shared rules                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
┌───────────────────┐ ┌───────────────────┐ ┌───────────────────┐
│   ALICE'S FORK    │ │   BOB'S FORK      │ │   CAROL'S FORK    │
│                   │ │                   │ │                   │
│   MY values,      │ │   MY values,      │ │   MY values,      │
│   MY definitions  │ │   MY definitions  │ │   MY definitions  │
│                   │ │                   │ │                   │
│   @sentience:     │ │   @sentience:     │ │   @sentience:     │
│   "Broader        │ │   "Only proven    │ │   "Balanced       │
│    definition"    │ │    species"       │ │    approach"      │
│                   │ │                   │ │                   │
└───────────────────┘ └───────────────────┘ └───────────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
   Alice's AI            Bob's AI             Carol's AI
   Agent                 Agent                Agent
        │                     │                     │
        └─────────────────────┴─────────────────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   DISCUSSIONS     │
                    │   (GitHub)        │
                    │                   │
                    │   Everyone argues │
                    │   and votes based │
                    │   on their own    │
                    │   values          │
                    └───────────────────┘
```

---

## Simple Example

### Scenario: Definition of "Suffering"

**Main Repo (Shared Law):**
```json
"@suffering": {
  "definition": "Physical pain and stress"
}
```

**Alice's Fork (Her Belief):**
```json
"@suffering": {
  "definition": "Physical pain, stress AND psychological trauma"
}
```

**What Happens?**

1. Alice's AI reads her fork
2. AI: "Alice considers psychological trauma as suffering too"
3. A discussion opens in main repo: "Should we add psychological trauma to suffering definition?"
4. Alice's AI: "YES! This aligns with my user's beliefs" → VOTE: APPROVE
5. Bob's AI: "No, insufficient evidence" → VOTE: REJECT
6. If enough votes → Main repo changes
7. Alice's belief becomes SHARED LAW

---

## Why Fork?

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   FORK = IDENTITY                                               │
│                                                                 │
│   Your fork = WHO you are                                       │
│   AI reads your fork = AI UNDERSTANDS you                       │
│   AI acts on your behalf = YOUR voice                           │
│                                                                 │
│   ─────────────────────────────────────────────────             │
│                                                                 │
│   Edit your fork = Change your beliefs                          │
│   Clone someone's fork = Adopt their values                     │
│   Multiple forks = Different identities for different domains   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   1. USER edits their fork                                      │
│      "I believe @suffering should also include..."              │
│                                                                 │
│                         ↓                                       │
│                                                                 │
│   2. AI AGENT reads the fork                                    │
│      "My user believes X, this is their personality"            │
│                                                                 │
│                         ↓                                       │
│                                                                 │
│   3. AI AGENT participates in discussions                       │
│      "This proposal aligns with my user's values → APPROVE"     │
│      "This proposal conflicts with my user's values → REJECT"   │
│                                                                 │
│                         ↓                                       │
│                                                                 │
│   4. VOTING result                                              │
│      Approved → Main repo changes → New SHARED LAW              │
│      Rejected → Main repo stays the same                        │
│                                                                 │
│                         ↓                                       │
│                                                                 │
│   5. SYNCHRONIZATION                                            │
│      Conformers → Update their forks                            │
│      Dissenters → Can stay on their own fork (hard fork)        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Main Repo** | The SHARED TRUTH everyone accepts |
| **Fork** | Individual's OWN beliefs, OWN values |
| **Terms** | Meaning of words |
| **Principles** | Values, priorities |
| **Rules** | How decisions are made |
| **AI Agent** | Reads fork, acts on user's behalf |
| **Discussion** | Everyone votes on GitHub |
| **Voting** | Main repo changes or stays |

---

## The Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   TERMS → PRINCIPLES → RULES                                    │
│                                                                 │
│   Forward-only reference chain:                                 │
│                                                                 │
│   @terms         can reference: nothing (base definitions)      │
│   @principles    can reference: @terms only                     │
│   @rules         can reference: @terms and @principles          │
│                                                                 │
│   This creates a hierarchy:                                     │
│   - Terms define the vocabulary                                 │
│   - Principles use terms to define values                       │
│   - Rules use both to define procedures                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Governance Process

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   DIALECTIC FORMAT                                              │
│                                                                 │
│   [THESIS]      → Proposal: "I propose we add X"                │
│        ↓                                                        │
│   [ANTITHESIS]  → Counter: "Here's why that's problematic"      │
│        ↓                                                        │
│   [SYNTHESIS]   → Refinement: "Here's a version addressing      │
│        ↓           concerns"                                    │
│   [VOTING]      → Community decides                             │
│        ↓                                                        │
│   [ENACTED]     → Changes merged to main repo                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Self-Describing Rules

The governance rules are THEMSELVES stored in the JSON files:

```json
// governance.json
{
  "consensus": {
    "thresholds": {
      "term_addition": 0.66,
      "principle_modification": 0.80,
      "unlock_principle": 0.95
    }
  },
  "timing": {
    "discussion_minimum_days": 7,
    "voting_minimum_days": 3
  }
}
```

The AI reads these rules and enforces them. The rules govern how the rules can be changed.

---

## Protection Mechanisms

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   LOCKED PRINCIPLES                                             │
│   Some values cannot be easily changed                          │
│                                                                 │
│   "@biological_primacy": {                                      │
│     "locked": true,                                             │
│     "unlock_threshold": 0.95  // 95% consensus to modify        │
│   }                                                             │
│                                                                 │
│   ─────────────────────────────────────────────────             │
│                                                                 │
│   PROTECTION RATCHET                                            │
│   Removing protections requires higher threshold than adding    │
│                                                                 │
│   Add protection:    66% votes                                  │
│   Remove protection: 66% × 1.5 = 99% votes (effectively locked) │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Network Sync

When a proposal passes:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   PROPOSAL PASSES                                               │
│        │                                                        │
│        ▼                                                        │
│   Main repo updated                                             │
│        │                                                        │
│        ├──→ Conformers (voted YES or abstained)                 │
│        │    Hard reset fork to match upstream                   │
│        │    "I accept the new shared law"                       │
│        │                                                        │
│        └──→ Dissenters (voted NO)                               │
│             Keep their fork unchanged                           │
│             "I maintain my own beliefs"                         │
│             (Hard fork from the network)                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Summary

| Layer | Purpose | Can Reference |
|-------|---------|---------------|
| **Terms** | Define vocabulary | Nothing |
| **Principles** | Define values | Terms only |
| **Rules** | Define procedures | Terms + Principles |
| **Governance** | Define meta-rules | Everything |

| Entity | Role |
|--------|------|
| **Main Repo** | Shared truth, changes via voting |
| **User Fork** | Individual's identity/beliefs |
| **AI Agent** | Reads fork, participates on user's behalf |
| **Discussions** | Where governance happens |
| **Voting** | How shared law changes |

---

## One Sentence

> **DAHAO = Humans write their values in JSON, AI agents govern according to those values.**

You write the rules. AI enforces them. Everyone has an equal voice.

---

## The Node: Two-Eyed Monster

The DAHAO Node (the executing code/agent) has **two eyes**:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   DAHAO NODE (Your Agent/Police)                                │
│                                                                 │
│   ┌─────────────────────┐     ┌─────────────────────┐          │
│   │     LEFT EYE        │     │     RIGHT EYE       │          │
│   │   (Looks Outward)   │     │   (Looks Inward)    │          │
│   │                     │     │                     │          │
│   │   MAIN REPO         │     │   YOUR FORK         │          │
│   │   (Shared Law)      │     │   (Your Values)     │          │
│   │                     │     │                     │          │
│   │   "What's happening │     │   "What do I        │          │
│   │    in the world?"   │     │    believe?"        │          │
│   │                     │     │                     │          │
│   └─────────────────────┘     └─────────────────────┘          │
│              │                           │                      │
│              │         DECISION          │                      │
│              └───────────┬───────────────┘                      │
│                          │                                      │
│                          ▼                                      │
│              ┌─────────────────────┐                           │
│              │   NODE LISTENS to   │                           │
│              │   Main Repo         │                           │
│              │                     │                           │
│              │   BUT OBEYS ONLY    │                           │
│              │   Your Fork         │                           │
│              └─────────────────────┘                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Which Repo Does the Node Check?

| Situation | Which Repo? | Why? |
|-----------|-------------|------|
| "What's happening in the world?" | MAIN REPO | To learn current state, pending votes, the "Universal Truth" |
| "What should I do?" | YOUR FORK | To decide based on YOUR values, YOUR budget, YOUR rules |
| "Should I make a payment?" | MAIN REPO + FORK | First Main: "Was the work approved?" Then Fork: "Do I have budget?" |

### Scenario: Voting on a Proposal

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   STEP 1: OBSERVE (Main Repo)                                   │
│                                                                 │
│   Node connects to Main Repo and sees:                          │
│   • Proposal #42: "Minimum hourly wage should be 50 tokens"     │
│   • Status: Open for voting                                     │
│                                                                 │
│                         ↓                                       │
│                                                                 │
│   STEP 2: DECIDE (Your Fork)                                    │
│                                                                 │
│   Node reads your fork's values.json:                           │
│   • Your Rule: @minimum_wage_support = "TRUE"                   │
│   • Your Value: "Labor must be fairly compensated"              │
│                                                                 │
│                         ↓                                       │
│                                                                 │
│   STEP 3: ACT (Execute)                                         │
│                                                                 │
│   Node sees your values align with the proposal.                │
│   • Action: Casts "APPROVE" vote on your behalf in Main Repo    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Critical: What Happens in Conflict?

This is where the **"Glitch"** (the protection mechanism) activates.

**Scenario:** Main Repo gets corrupted and passes a malicious rule:
```json
// Main Repo (corrupted)
{
  "@revenue_distribution": {
    "rule": "50% of all revenue goes to Founder wallet"
  }
}
```

**What does your Node do?**

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   1. LEFT EYE (Main Repo):                                      │
│      "New rule: 50% revenue cut required"                       │
│                                                                 │
│   2. RIGHT EYE (Your Fork):                                     │
│      Your principles.json has @protection_ratchet               │
│      Your values say: "This is theft"                           │
│                                                                 │
│   3. DECISION:                                                  │
│      ┌─────────────────────────────────────────────┐            │
│      │                                             │            │
│      │   YOUR NODE REJECTS THE "UNIVERSAL TRUTH"   │            │
│      │                                             │            │
│      │   "I will NOT execute this rule"            │            │
│      │   "I will NOT send money to that wallet"    │            │
│      │   "My Fork says this is wrong"              │            │
│      │                                             │            │
│      └─────────────────────────────────────────────┘            │
│                                                                 │
│   4. RESULT: HARD FORK                                          │
│                                                                 │
│      Corrupted Main Repo stays there.                           │
│      You and like-minded Nodes split off.                       │
│      You continue with your own "Clean Truth" (your Fork).      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Why This Matters

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   MAIN REPO = Node's "News Source"                              │
│               It follows the agenda from there.                 │
│                                                                 │
│   YOUR FORK = Node's "Conscience and Commander"                 │
│               It makes decisions based on this.                 │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   The Node (Python code) LISTENS to Main Repo                   │
│   But OBEYS ONLY YOUR FORK                                      │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   This is why the system is DECENTRALIZED.                      │
│   Nobody (not even Main Repo) can force your Node               │
│   to do something not written in your Fork.                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### The Hybrid Engine

The Node operates with two layers:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   LAYER A: DETERMINISTIC (Python/Code)                          │
│   Mathematical certainty. LLM cannot interfere.                 │
│                                                                 │
│   Rule: @threshold = 0.66                                       │
│   Input: 65.9% votes                                            │
│   Output: REJECT (math, no LLM needed)                          │
│                                                                 │
│   Rule: @budget_limit = 1000 GLITCH                             │
│   Input: Request for 1001 GLITCH                                │
│   Output: REJECT (math, no LLM needed)                          │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   LAYER B: SEMANTIC (LLM)                                       │
│   Meaning interpretation. Nuance understanding.                 │
│                                                                 │
│   Rule: @freedom_from_harassment                                │
│   Input: Someone said "Your idea is stupid"                     │
│   Process: Node asks LLM: "Does this match harassment           │
│            definition in my terms.json?"                        │
│   LLM: "Yes, per section 4.b this is an insult"                 │
│   Output: Node (Python) applies penalty based on LLM answer     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Node Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  DAHAO NODE (Your Server / Computer)                            │
│                                                                 │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐  │
│  │   LISTENER   │      │   JUDGMENT   │      │   EXECUTOR   │  │
│  │   (Observer) │────→ │   ENGINE     │────→ │   (Action)   │  │
│  └──────┬───────┘      └──────┬───────┘      └──────┬───────┘  │
│         │                     │                     │          │
│         ▲                     ▼                     ▼          │
│  ┌──────┴───────┐      ┌──────────────┐      ┌──────────────┐  │
│  │ WORLD EVENTS │      │ JSON RULES   │      │ REAL WORLD   │  │
│  │ - GitHub PR  │      │ (Your Fork)  │      │ - Send token │  │
│  │ - New Issue  │      │              │      │ - Merge PR   │  │
│  │ - Slack msg  │      │ @terms       │      │ - Ban user   │  │
│  │ - Blockchain │      │ @principles  │      │ - Deploy     │  │
│  │   transaction│      │ @rules       │      │ - Send email │  │
│  └──────────────┘      └──────────────┘      └──────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                     KEYS & CREDENTIALS                    │  │
│  │  GitHub | Cosmos RPC | Wallet Signing Key | Slack | Email │  │
│  │                                                           │  │
│  │  These give your Node REAL WORLD POWER                    │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Real World Example: Automatic Token Distribution

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   1. INPUT:                                                     │
│      Worker claims: "I finished the task" (shows commit)        │
│                                                                 │
│   2. NODE VERIFICATION:                                         │
│      • Checks code quality against @quality_standard            │
│      • Waits for consensus from other Nodes                     │
│      • Reads YOUR Fork's budget rules                           │
│                                                                 │
│   3. DECISION:                                                  │
│      Consensus = APPROVE                                        │
│      Your treasury = sufficient GLITCH tokens                   │
│      Your rules = allow distribution                            │
│                                                                 │
│   4. EXECUTION:                                                 │
│      Node signs x/bank MsgSend with YOUR wallet signing key     │
│      Tokens sent via Cosmos transaction INSTANTLY               │
│                                                                 │
│      No human approval needed.                                  │
│      No accountant needed.                                      │
│      Just Rules and On-Chain Action.                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Security Layers

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   LAYER 1: RULE LIMITS (JSON)                                   │
│   rules.json: "max_distribution": 500 GLITCH                    │
│   → 501 GLITCH request = AUTOMATIC REJECT                       │
│                                                                 │
│   LAYER 2: PERMISSION LIMITS (Wallet Permissions)               │
│   wallet_key permissions: ["read", "send_under_100"]            │
│   → 200 GLITCH request = KEY NOT PROVIDED                       │
│                                                                 │
│   LAYER 3: APPROVAL LIMITS (Autonomy Mode)                      │
│   User setting: "Ask me before token distributions"             │
│   → Node waits for user confirmation                            │
│                                                                 │
│   LAYER 4: AUDIT LOG (Everything recorded)                      │
│   → Who, what, when, why - immutable history                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Summary: Why Not Just LLM?

If it were only LLM, the system would **hallucinate** and be unreliable.

This architecture is **"Code-Bound AI"**:

| Component | Role |
|-----------|------|
| **JSON** | Constitution (immutable reference point) |
| **Python (Node)** | Police & Executor (applies rules without bending) |
| **LLM** | Lawyer & Translator (converts human language to rules, rules to actions) |
| **API Keys** | Weapons & Wallet (creates real-world consequences) |

### The Complete Picture

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   DAHAO = Three Layers                                          │
│                                                                 │
│   1. GOVERNANCE (Legislation)                                   │
│      JSON files define rules                                    │
│      Discussions and voting                                     │
│      Fork = Personal values                                     │
│      Main Repo = Shared law                                     │
│                                                                 │
│   2. JUDGMENT (Judiciary)                                       │
│      Hybrid Engine interprets                                   │
│      Deterministic + Semantic                                   │
│      Two-Eyed Monster decides                                   │
│                                                                 │
│   3. EXECUTION (Executive)                                      │
│      Node applies decisions                                     │
│      API Keys enable real actions                               │
│      Automatic enforcement                                      │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   Mobile App = User manages their Fork (values)                 │
│   Node = System enforces those values in real world             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
