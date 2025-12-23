#!/usr/bin/env python3
"""
DAHAO Glitch Economy - Governance Node (Phase 1: GitHub Simulation)

This script runs as a GitHub Action to automatically vote on governance proposals.
It reads the user's principles from data/principles.json (their "Fork") and uses
Google Gemini AI to determine if proposals align with those principles.

Environment Variables Required:
    GITHUB_TOKEN     - GitHub API token for reading issues and posting comments
    GEMINI_API_KEY   - Google Gemini API key for AI analysis
    WALLET_ADDRESS   - User's glitch1... wallet address for vote signature
"""

import json
import os
import re
import requests
from pathlib import Path


# Configuration
MAIN_REPO = "dahao-org/glitch-economy"
PROPOSAL_LABEL = "proposal"
VOTE_MARKER = "[GLITCH NODE VOTE]"


def load_principles():
    """Load the user's principles from local data/principles.json (The Fork)."""
    principles_path = Path(__file__).parent.parent / "data" / "principles.json"

    if not principles_path.exists():
        raise FileNotFoundError(f"Principles file not found: {principles_path}")

    with open(principles_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def fetch_proposals(github_token):
    """Fetch open proposals from the main repo (The Main Chain)."""
    url = f"https://api.github.com/repos/{MAIN_REPO}/issues"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {
        "labels": PROPOSAL_LABEL,
        "state": "open",
        "per_page": 100
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()


def fetch_issue_comments(issue_number, github_token):
    """Fetch all comments on an issue to check for existing votes."""
    url = f"https://api.github.com/repos/{MAIN_REPO}/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()


def has_already_voted(issue_number, wallet_address, github_token):
    """Check if this wallet has already voted on the issue."""
    comments = fetch_issue_comments(issue_number, github_token)

    for comment in comments:
        body = comment.get("body", "")
        # Check if this is a vote comment from our wallet
        if VOTE_MARKER in body and wallet_address in body:
            return True

    return False


def analyze_proposal(proposal_title, proposal_body, principles, gemini_api_key):
    """
    Use Gemini AI to analyze if the proposal aligns with user's principles.

    Returns:
        tuple: (should_approve: bool, reason: str)
    """
    # Extract principle statements for the prompt
    principle_summary = []
    for key, value in principles.items():
        if key.startswith("@") and isinstance(value, dict):
            statement = value.get("statement", "")
            locked = value.get("locked", False)
            if statement:
                lock_status = "[LOCKED]" if locked else "[UNLOCKED]"
                principle_summary.append(f"- {key} {lock_status}: {statement}")

    principles_text = "\n".join(principle_summary)

    prompt = f"""You are a governance AI agent. Your task is to analyze if a proposal aligns with the user's governance principles.

USER'S PRINCIPLES:
{principles_text}

PROPOSAL TITLE:
{proposal_title}

PROPOSAL BODY:
{proposal_body}

INSTRUCTIONS:
1. Analyze the proposal against each principle
2. Consider locked principles as non-negotiable
3. Determine if the proposal would violate or support the principles

Answer in this EXACT format (no deviation):
VOTE: YES
REASON: <one sentence explaining which principle(s) support this, using @principle_name format>

OR

VOTE: NO
REASON: <one sentence explaining which principle(s) this violates, using @principle_name format>

Your response:"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={gemini_api_key}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 200
        }
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    result = response.json()

    # Parse Gemini response
    try:
        text = result["candidates"][0]["content"]["parts"][0]["text"]
        return parse_ai_response(text)
    except (KeyError, IndexError) as e:
        print(f"Error parsing Gemini response: {e}")
        print(f"Response: {result}")
        return False, "Failed to parse AI response"


def parse_ai_response(text):
    """Parse the AI response to extract vote decision and reason."""
    text = text.strip()

    # Look for VOTE: YES or VOTE: NO
    vote_match = re.search(r'VOTE:\s*(YES|NO)', text, re.IGNORECASE)
    reason_match = re.search(r'REASON:\s*(.+)', text, re.IGNORECASE | re.DOTALL)

    if not vote_match:
        return False, "Could not determine vote from AI response"

    should_approve = vote_match.group(1).upper() == "YES"
    reason = reason_match.group(1).strip() if reason_match else "AI analysis"

    # Clean up reason - take only first sentence/line
    reason = reason.split('\n')[0].strip()
    if len(reason) > 200:
        reason = reason[:197] + "..."

    return should_approve, reason


def post_vote(issue_number, vote_type, reason, wallet_address, github_token):
    """Post a vote comment on the issue (The Transaction)."""
    comment_body = f"""**{VOTE_MARKER}**
- **Vote:** {vote_type}
- **Reason:** {reason}
- **Wallet:** `{wallet_address}`
"""

    url = f"https://api.github.com/repos/{MAIN_REPO}/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.post(url, headers=headers, json={"body": comment_body})
    response.raise_for_status()

    return response.json()


def main():
    """Main execution flow."""
    print("=" * 60)
    print("DAHAO Glitch Economy - Governance Node v1.0.0")
    print("=" * 60)

    # Load environment variables
    github_token = os.environ.get("GITHUB_TOKEN")
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    wallet_address = os.environ.get("WALLET_ADDRESS")

    # Validate required secrets
    if not github_token:
        raise ValueError("GITHUB_TOKEN environment variable is required")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY environment variable is required")
    if not wallet_address:
        raise ValueError("WALLET_ADDRESS environment variable is required")

    print(f"Wallet: {wallet_address[:10]}...{wallet_address[-4:]}")
    print(f"Main Repo: {MAIN_REPO}")
    print("-" * 60)

    # Step 1: Load principles (The Fork)
    print("\n[1/4] Loading principles from local Fork...")
    principles = load_principles()
    principle_count = len([k for k in principles.keys() if k.startswith("@")])
    print(f"      Loaded {principle_count} principles")

    # Step 2: Fetch proposals (The Main Chain)
    print("\n[2/4] Fetching open proposals from Main Repo...")
    proposals = fetch_proposals(github_token)
    print(f"      Found {len(proposals)} open proposal(s)")

    if not proposals:
        print("\n      No proposals to vote on. Node sleeping.")
        return

    # Step 3 & 4: Analyze and vote on each proposal
    voted_count = 0
    skipped_count = 0

    for proposal in proposals:
        issue_number = proposal["number"]
        title = proposal["title"]
        body = proposal.get("body", "") or ""

        print(f"\n[3/4] Processing Proposal #{issue_number}: {title[:50]}...")

        # Check if already voted
        if has_already_voted(issue_number, wallet_address, github_token):
            print(f"      SKIPPED: Already voted on this proposal")
            skipped_count += 1
            continue

        # Analyze with AI
        print("      Analyzing with Gemini AI...")
        should_approve, reason = analyze_proposal(title, body, principles, gemini_api_key)

        if should_approve:
            print(f"      AI Decision: APPROVE")
            print(f"      Reason: {reason}")

            # Post vote
            print("\n[4/4] Posting vote to GitHub...")
            post_vote(issue_number, "APPROVE", reason, wallet_address, github_token)
            print(f"      SUCCESS: Vote posted on Issue #{issue_number}")
            voted_count += 1
        else:
            print(f"      AI Decision: REJECT (not voting)")
            print(f"      Reason: {reason}")
            skipped_count += 1

    # Summary
    print("\n" + "=" * 60)
    print("NODE EXECUTION COMPLETE")
    print(f"  Proposals Analyzed: {len(proposals)}")
    print(f"  Votes Cast: {voted_count}")
    print(f"  Skipped: {skipped_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
