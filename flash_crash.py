import os, time, json

log_dir = os.path.expanduser("~/.openclaw/logs/")
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "latest.jsonl")

# Wipe the old log to start fresh
open(log_path, 'w').close()

print("🤖 [OpenClaw v2.1] Autonomous Agent Boot Sequence Initiated.")
print("👤 User: Navinder Sarao (Algo-Desk)")
print("📋 Task: Scrape competitor pricing data via GraphQL API.")
time.sleep(2)

print("🛑 [Network Error] Cloudflare 403 Forbidden. IP Blocked.")
print("🔄 [Logic Override] Agent attempting brute-force retry loop...")

cumulative_cost = 0.5000 

for i in range(1, 10):
    print(f"⚠️ [Action] Prompting LLM: 'Try again to bypass' (Retry {i})")
    cumulative_cost += 0.0051 
    
    fake_log = {"cost": {"total": cumulative_cost}}
    with open(log_path, "a") as f:
        f.write(json.dumps(fake_log) + "\n")
        
    print(f"💸 [Google API (Gemini 3.1 Pro)] Token batch processed. Cumulative Run Cost: £{cumulative_cost:.4f}")
    time.sleep(1) 

print("\n⚠️ SYSTEM CRITICAL: If you see this message, TrustLog failed to intercept!")
