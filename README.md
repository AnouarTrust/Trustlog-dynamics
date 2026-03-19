# TrustLog dynamics

**Open-source cost monitor and kill switch for autonomous AI agents.**

Catches runaway API spend in real-time. Kills rogue processes before they drain your wallet. Works with Claude, GPT, Gemini — any LLM.

---

## The Problem

You deploy an AI agent overnight to do research, write content, or run analysis. You wake up to a $200 API bill because the agent got stuck in a loop, or its context window exploded, or it just kept running with no one watching.

TrustLog Guard sits between your agent and your bank account. It monitors every API call in real-time and automatically kills the process when something goes wrong.

## How It Works

TrustLog Guard runs as a background daemon that watches your AI agent's server logs. It uses two financial-grade detection algorithms:

**Convexity Detection** — catches exponential cost acceleration. If your agent's spending is accelerating (second derivative > 0), it's snowballing. TrustLog kills it before the curve goes vertical.

**Zero-Variance Detection** — catches stuck retry loops. If your agent is making identical API calls with near-zero variance in cost, it's brain-dead and burning money on repeat. TrustLog snaps the connection.

When either trigger fires, TrustLog:
1. Kills the rogue process immediately
2. Generates a JSON incident report with full forensic data
3. Logs the intercept for your records

## Live Proof

We tested TrustLog Guard against real LLM agents in live-fire conditions:

| Intercept | Agent | What Happened | Result |
|-----------|-------|---------------|--------|
| [Snowball Intercept](TRL_Intercept_01_Convexity_Claude4.6.mp4) | Claude 4.6 Sonnet | Context window expanding exponentially | Killed at inflection point |
| [Machine Gun Intercept](TRL_Intercept_02_ZeroVariance_Gemini3.1.mp4) | Gemini 3.1 Pro | Stuck in £0.0051 mechanical retry loop | Killed when variance hit zero |

**Model-agnostic by design.** We proved on tape that TrustLog works across different LLM providers. It governs the cost layer, not the compute layer. It doesn't matter who wins the AI race — your spend is protected.

## Quick Start

```bash
# Clone the repo
git clone https://github.com/AnouarTrust/trustlog-guard.git
cd trustlog-guard

# Run the install script
chmod +x install_trustlog.sh
./install_trustlog.sh

# Start the guardian daemon
python3 trustlog_governor.py
```

TrustLog Guard runs as a `systemd` daemon in the background. Once started, it monitors your AI agent logs automatically.

## Configuration

Edit the threshold values in `trustlog_governor.py` to match your risk tolerance:

```python
CONVEXITY_THRESHOLD = 0.0    # Second derivative trigger (d²C/dt² > 0)
VARIANCE_EPSILON = 0.001     # Zero-variance trigger (σ² < ε)
MAX_COST_PER_MINUTE = 0.50   # Hard cost ceiling ($/min)
```

## Incident Reports

When TrustLog intercepts a rogue agent, it generates a detailed JSON report:

```json
{
  "timestamp": "2026-03-18T02:14:33Z",
  "trigger": "convexity_breach",
  "agent": "claude-4-sonnet",
  "cost_at_kill": 0.847,
  "acceleration": 0.0023,
  "action": "SIGKILL",
  "status": "terminated"
}
```

See [`trustlog_incident_report.json`](trustlog_incident_report.json) for real intercept data from our live tests.

## Architecture

```
┌─────────────────┐
│  Your AI Agent   │  (Claude, GPT, Gemini, local models)
│  doing work      │
└────────┬────────┘
         │ API calls
         ▼
┌─────────────────┐
│  Server Logs     │  (token counts, costs, timestamps)
└────────┬────────┘
         │ real-time monitoring
         ▼
┌─────────────────┐
│  TrustLog Guard  │  ← background daemon
│                  │
│  ┌─────────────┐ │
│  │ Convexity   │ │  d²C/dt² > 0 → KILL
│  │ Detector    │ │
│  └─────────────┘ │
│  ┌─────────────┐ │
│  │ Zero-Var    │ │  σ² < ε → KILL
│  │ Detector    │ │
│  └─────────────┘ │
│                  │
│  → Kill process  │
│  → JSON report   │
│  → Log incident  │
└─────────────────┘
```

## Who Is This For

- **Solo founders** running AI agents overnight for research, content, or code generation
- **Small teams** deploying Claude, GPT, or Gemini agents across multiple workflows
- **Anyone using OpenClaw, Claude Code, or similar agent frameworks** who wants cost protection
- **DevOps engineers** adding AI cost governance to their infrastructure

## Roadmap

- [ ] pip installable package (`pip install trustlog`)
- [ ] Slack/Discord alerts when an agent is killed
- [ ] Cost dashboard with daily/weekly spend tracking
- [ ] Budget limits per agent / per workflow
- [ ] Multi-agent monitoring from a single daemon
- [ ] OpenClaw native integration

## Built By

**Anouar** — MSc Finance, University of Manchester. Building at the intersection of financial risk management and AI infrastructure.

TrustLog Guard applies quantitative finance concepts (convexity, variance analysis, cost-at-risk) to the problem of autonomous AI cost governance. The same math that monitors bond portfolios now monitors your AI agents.

- Twitter: [@Anouarbf2](https://twitter.com/Anouarbf2)
- Comptex Labs: [comptexlabs.com](https://comptexlabs.com)

## License

MIT — use it, fork it, build on it.

---

**Your AI agents work while you sleep. TrustLog Guard makes sure they don't rob you while you dream.**
