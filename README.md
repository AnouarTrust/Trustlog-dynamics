TrustLog DynamicsOpen-source cost monitor and kill switch for autonomous AI agents.Your agents burn tokens while you sleep. TrustLog watches them so you don't wake up to a surprise bill. Works with Claude, GPT, Gemini — any LLM, any provider.Why This ExistsHere's the scenario. You spin up an AI agent to do research, generate content, or run some analysis overnight. You go to bed. The agent gets stuck in a retry loop — or worse, its context window starts ballooning. By morning you've got a £150 bill for absolutely nothing useful.Nobody's watching the meter. That's the problem.TrustLog Dynamics sits between your agent and your wallet. It monitors API spend in real-time and kills any process the moment something looks off. No human needed. It just runs.How It WorksTrustLog runs as a background daemon on your server. It reads your agent's logs and applies two detection algorithms — both borrowed from quantitative finance risk management:Convexity Detection — spots exponential cost acceleration. If your agent's spend rate is accelerating ($d^2C/dt^2>0$), it's snowballing. TrustLog kills it before the curve goes vertical.Zero-Variance Detection — spots stuck loops. If your agent keeps making the same API call at the same cost with near-zero variance ($\sigma^2<\epsilon$), it's brainless and burning cash on repeat. TrustLog cuts it off.When either trigger fires:The rogue process gets killed immediately.A JSON incident report is generated with full forensic data.Everything is logged so you can see exactly what happened.Proved It LiveWe ran TrustLog against real LLM agents. Two different providers. Two different failure modes. Caught both.InterceptAgentWhat Went WrongOutcomeEvidenceSnowballClaude 4.6 SonnetContext window expanding exponentially✅ Killed at the inflection point[Watch Intercept]([INSERT YOUTUBE LINK 1 HERE])Machine GunGemini 3.1 ProStuck in a £0.0051 retry loop✅ Killed when variance hit zero[Watch Intercept]([INSERT YOUTUBE LINK 2 HERE])Model-agnostic by design. We proved on camera that TrustLog works across providers. It governs the cost layer, not the compute layer — doesn't matter who wins the LLM race, your spend is protected.Get StartedThree commands. That's it.Bash# Clone the repo
git clone https://github.com/AnouarTrust/trustlog-dynamics.git
cd trustlog-dynamics

# Install
chmod +x install_trustlog.sh
./install_trustlog.sh

# Run
python3 trustlog_governor.py
Runs as a systemd daemon in the background. Once it's up, it's watching your agent logs automatically.Configure ItOpen trustlog_governor.py and set your own thresholds:PythonCONVEXITY_THRESHOLD = 0.0    # Second derivative trigger 
VARIANCE_EPSILON = 0.001     # Zero-variance trigger 
MAX_COST_PER_MINUTE = 0.50   # Hard cost ceiling (£/min)
Tighter thresholds = more aggressive protection. Adjust to your risk appetite.The MathsThis isn't arbitrary threshold logic. It's built on the same frameworks used in financial risk management — applied to AI spend instead of bond portfolios.Convexity trigger — borrowed from fixed-income risk:$$\frac{d^2C}{dt^2}>0 \implies \text{cost is accelerating} \implies \text{KILL}$$Zero-variance trigger — borrowed from statistical process control:$$\sigma^2<\epsilon \implies \text{agent is stuck in a loop} \implies \text{KILL}$$Where $C$ = cumulative API cost, $t$ = time, $\sigma^2$ = rolling variance of cost per call, $\epsilon$ = minimum variance threshold.Incident ReportsEvery intercept generates a detailed JSON autopsy:JSON{
  "timestamp": "2026-03-18T02:14:33Z",
  "trigger": "convexity_breach",
  "agent": "claude-4-sonnet",
  "cost_at_kill": 0.847,
  "acceleration": 0.0023,
  "action": "SIGKILL",
  "status": "terminated"
}
See trustlog_incident_report.json for real data from our live tests.Built ByAnouar — MSc Finance, University of Manchester.I built TrustLog Dynamics because I kept seeing the same problem — AI agents running up costs with nobody watching. The finance world has had circuit breakers and risk limits for decades. The AI world doesn't. So I brought the maths across.Twitter: @Anouarbf2Comptex Labs: comptexlabs.comLicenceMIT — use it, fork it, build on it.Your AI agents work while you sleep. TrustLog Dynamics makes sure they don't rob you while you dream
