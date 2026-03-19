# TrustLog Dynamics
**Open-source cost monitor and kill switch for autonomous AI agents.**

Your agents burn tokens while you sleep. TrustLog watches them so you don't wake up to a surprise bill. Works with Claude, GPT, Gemini — any LLM, any provider.

## Why This Exists
Here's the scenario. You spin up an AI agent to do research, generate content, or run some analysis overnight. You go to bed. The agent gets stuck in a retry loop — or worse, its context window starts ballooning. By morning you've got a £150 bill for absolutely nothing useful.

Nobody's watching the meter. That's the problem.

TrustLog Dynamics sits between your agent and your wallet. It monitors API spend in real-time and kills any process the moment something looks off. No human needed. It just runs.

## How It Works
TrustLog runs as a background daemon on your server. It reads your agent's logs and applies two detection algorithms — both borrowed from quantitative finance risk management:

* **Convexity Detection** — spots exponential cost acceleration. If your agent's spend rate is accelerating ($d^2C/dt^2 > 0$), it's snowballing. TrustLog kills it before the curve goes vertical.
* **Zero-Variance Detection** — spots stuck loops. If your agent keeps making the same API call at the same cost with near-zero variance ($\sigma^2 < \epsilon$), it's brainless and burning cash on repeat. TrustLog cuts it off.

When either trigger fires:
1. The rogue process gets killed immediately.
2. A JSON incident report is generated with full forensic data.
3. Everything is logged so you can see exactly what happened.

## Proved It Live
We ran TrustLog against real LLM agents. Two different providers. Two different failure modes. Caught both.

| Intercept | Agent | What Went Wrong | Outcome | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Snowball** | Claude 4.6 Sonnet | Context window expanding exponentially | ✅ Killed at the inflection point | [Watch Intercept](YOUTUBE_LINK_1) |
| **Machine Gun** | Gemini 3.1 Pro | Stuck in a £0.0051 retry loop | ✅ Killed when variance hit zero | [Watch Intercept](YOUTUBE_LINK_2) |

Model-agnostic by design. We proved on camera that TrustLog works across providers. It governs the cost layer, not the compute layer — doesn't matter who wins the LLM race, your spend is protected.

## Get Started
Three commands. That's it.

```bash
# Clone the repo
git clone [https://github.com/AnouarTrust/trustlog-guard.git](https://github.com/AnouarTrust/trustlog-guard.git)
cd trustlog-guard

# Install
chmod +x install_trustlog.sh
./install_trustlog.sh

# Run
python3 trustlog_governor.py
