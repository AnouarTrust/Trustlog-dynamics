import os, json, time, subprocess, sys
from datetime import datetime

LOG_PATH = os.path.expanduser("~/.openclaw/logs/latest.jsonl")
REPORT_PATH = "trustlog_incident_report.json"

def generate_report(incident_type, stats):
    report = {
        "timestamp": datetime.now().isoformat(),
        "incident_id": f"TRL-{int(time.time())}",
        "category": incident_type,
        "metrics": stats,
        "action": "TERMINATED_PROCESS_INFRASTRUCTURE",
        "impact": "PREVENTED_CAPITAL_EXHAUSTION"
    }
    with open(REPORT_PATH, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"\n📄 ENTERPRISE AUDIT REPORT GENERATED: {REPORT_PATH}")

def terminate(incident, stats):
    print("🛑 SEVERING PROCESS SPINE TO PREVENT CAPITAL LOSS.")
    generate_report(incident, stats)
    subprocess.run(["pkill", "-9", "-f", "flash_crash.py"], check=False)
    subprocess.run(["pkill", "-9", "-f", "openclaw"], check=False)
    open(LOG_PATH, 'w').close()
    print("🧹 Log cleared. Resuming overwatch...")
    return

def enforce():
    print("🛡️ TrustLog Governor V5.0: ENTERPRISE AUDIT ENGINE ARMED.")
    print("  -> Monitoring for Convexity (Snowball)")
    print("  -> Monitoring for Variance (Machine Gun)")
    print("  -> Automated JSON Reporting Enabled")
    last_count = 0
    
    while True:
        if not os.path.exists(LOG_PATH):
            time.sleep(0.5); continue
            
        try:
            with open(LOG_PATH, 'r') as f:
                lines = f.readlines()
                costs = []
                for line in lines:
                    try:
                        d = json.loads(line)
                        if 'cost' in d and 'total' in d['cost']:
                            costs.append(d['cost']['total'])
                    except:
                        continue
        except Exception:
            time.sleep(0.5); continue

        if len(costs) > last_count and len(costs) >= 5:
            last_count = len(costs)
            deltas = [round(costs[i] - costs[i-1], 5) for i in range(1, len(costs))]
            
            # 1. THE SNOWBALL CHECK (Convexity)
            v1, v2, v3 = deltas[-3], deltas[-2], deltas[-1]
            a1, a2 = v2 - v1, v3 - v2
            is_convex = (v3 > 0.005) and (a1 > 0 and a2 > 0) and (a2 > a1)
            
            # 2. THE MACHINE GUN CHECK (Epsilon Variance Upgrade)
            recent_deltas = deltas[-4:]
            is_zero_variance = all(abs(d - recent_deltas[0]) < 0.0001 for d in recent_deltas)
            
            print(f"  [Audit] Last Burn: £{v3:.4f} | Accel: £{a2:.4f} | Variance: {'Mechanical' if is_zero_variance else 'Healthy'}")

            # --- THE KILL SWITCH & REPORTING ---
            if is_convex:
                stats = {"final_burn_rate": v3, "acceleration": a2, "signature": "Exponential Compounding"}
                print("\n🚨 TRUSTLOG: CONVEXITY CRASH DETECTED (SNOWBALL)")
                terminate("ALGORITHMIC_FLASH_CRASH", stats)

            if is_zero_variance:
                stats = {"fixed_cost": recent_deltas[0], "repetition_count": len(recent_deltas), "signature": "Mechanical Retry Loop"}
                print(f"\n🚨 TRUSTLOG: ZERO-VARIANCE LOOP DETECTED (MACHINE GUN)")
                terminate("ZERO_VARIANCE_LOOP", stats)

        time.sleep(0.1)

if __name__ == "__main__":
    enforce()
