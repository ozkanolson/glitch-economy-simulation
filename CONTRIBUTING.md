# Contributing to DAHAO Glitch Economy

Thank you for your interest in contributing to the Glitch Economy governance framework. This document explains how to participate in the evolution of this domain.

## Contribution Types

### 1. Stakeholder Profiles

Document new types of contributors who deserve protection.

**Required fields:**
- `stakeholder_type` - Name of the stakeholder class
- `contribution_evidence` - How their contribution is verified
- `contribution_capacity_confidence` - HIGH/MEDIUM/LOW/UNKNOWN
- `compensation_requirements` - Mapped to Five Labor Rights
- `sources` - Minimum 1 source, Tier C or better

**Example:** Adding "Content Creator" as a stakeholder type:
```json
{
  "stakeholder_type": "Content Creator",
  "contribution_evidence": {
    "creative_output": ["Articles published", "Videos produced", "Designs delivered"],
    "engagement_metrics": ["Views", "Shares", "Conversions"]
  },
  "compensation_requirements": {
    "freedom_from_token_theft": {
      "requirement": "Fair GLITCH token compensation for all creative work",
      "note": "Includes streaming payments for ongoing value creation"
    }
  }
}
```

### 2. Practice Assessments

Document economic practices that affect contributor welfare.

**Required fields:**
- `name` - Practice name
- `description` - What the practice involves
- `target_stakeholders` - Who is affected
- `economic_impacts` - Documented effects with evidence
- `five_rights_assessment` - Impact on each right
- `economic_verdict` - ETHICAL/EXPLOITATIVE/COMPLEX/UNKNOWN
- `sources` - Minimum 1 source, Tier C or better

**Verdict Guidelines:**
- **EXPLOITATIVE**: Violates 2+ rights OR severe harm for trivial benefit
- **COMPLEX**: Violates 1 right OR mixed impacts with significant benefit
- **ETHICAL**: No rights violated AND no exploitation evidence
- **UNKNOWN**: Insufficient evidence (apply precautionary principle)

### 3. Term Proposals

Add or modify vocabulary used in governance.

**Process:**
1. Identify gap in current terminology
2. Draft definition with clear operational meaning
3. Include evidence tier requirements where applicable
4. Reference related terms and principles

### 4. Principle/Rule Changes

**For unlocked principles/rules:**
- Consensus threshold: 66%
- Discussion minimum: 0.5-1 day depending on type

**For locked principles (99% consensus required):**
- Must demonstrate exceptional circumstance
- Include impact analysis on all stakeholders
- Consider unintended consequences

## Evidence Requirements

| Claim Type | Minimum Tier | Notes |
|------------|--------------|-------|
| Contribution claim | B | On-chain or signed preferred |
| Exploitation claim | B | Documented compensation analysis |
| No exploitation claim | **A** | Higher bar for removing protection |
| Practice impact | C | Comparative studies preferred |

### Evidence Tiers

- **Tier A (On-Chain)**: Cryptographically verifiable
- **Tier A (Academic)**: Peer-reviewed research
- **Tier B**: Institutional reports, signed attestations
- **Tier C**: Expert opinion, preprints, community attestation
- **Tier D**: Anecdotal (insufficient for most claims)

## Proposal Process

### 1. [THESIS] - Initial Proposal

Create a proposal file in `data/enactments/` with:
- Clear objective
- Rationale
- Specific changes (JSON diffs)
- Evidence and sources
- Alignment with principles

### 2. Discussion Phase

- Minimum discussion period applies
- Community can raise concerns
- Proposer addresses feedback

### 3. [SYNTHESIS] - Revised Proposal

If needed, revise proposal based on discussion.

### 4. Voting

- Proposal goes to vote
- Threshold depends on type (66%, 75%, or 99%)
- Quorum requirements apply

### 5. Enactment

If approved:
- Changes merged to data files
- If on-chain enabled: Cosmos module execution via x/gov or x/bank MsgSend
- History recorded in `data/enactments/`

## Governance Constraints

Remember these immutable constraints:

1. **Protection Ratchet**: Adding protection requires 66%, removing requires 99%
2. **Labor Primacy**: Contribution evidence trumps tradition/convenience
3. **Contribution Axiom**: All contributors deserve fair compensation
4. **Asymmetry**: Claims removing protection need stronger evidence

## Cosmos On-Chain Proposals

Some proposals can trigger on-chain execution via Cosmos SDK modules:

- `@reward_allocation` - Token distribution via x/bank MsgSend
- `@treasury_distribution` - Collective fund allocation via x/distribution
- `@stake_adjustment` - Governance weight changes via x/staking

Include execution details in on-chain proposals:
```json
{
  "enactment_mode": "cosmos_tx",
  "cosmos_module": "x/bank",
  "message_type": "MsgSend",
  "parameters": {
    "from_address": "glitch1treasury...",
    "to_address": "glitch1contributor...",
    "amount": [{"denom": "uglitch", "amount": "1000000"}]
  }
}
```

For governance proposals requiring vote:
```json
{
  "enactment_mode": "cosmos_tx",
  "cosmos_module": "x/gov",
  "message_type": "MsgSubmitProposal",
  "proposal_type": "CommunityPoolSpendProposal"
}
```

## Code of Conduct

- Argue positions with evidence, not authority
- Respect all stakeholder perspectives
- Accept that 66-99% consensus is required, not 100%
- Focus on systemic improvement, not personal attacks

## Questions?

Open an issue or propose a clarification to this document.

---

*"The code says 'yes' if the rules say yes. No human can override."*
