import json
import sys

def check_zap_report(report_path):
    print(f"🔍 SecurOps: Analyzing ZAP report at {report_path}...")
    
    try:
        with open(report_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ Error: ZAP report JSON not found.")
        sys.exit(1)

    high_count = 0
    medium_count = 0

    for site in data.get('site', []):
        for alert in site.get('alerts', []):
            risk = alert.get('riskcode') # 3=High, 2=Medium, 1=Low, 0=Info
            if risk == "3":
                high_count += 1
                print(f"🔴 HIGH RISK: {alert.get('alert')} in {alert.get('name')}")
            elif risk == "2":
                medium_count += 1
                print(f"🟡 MEDIUM RISK: {alert.get('alert')}")

    print(f"\nSummary: Found {high_count} High and {medium_count} Medium issues.")

    if high_count > 0:
        print("❌ BLOCK: High severity vulnerabilities detected. Fix before merging!")
        sys.exit(1)
    elif medium_count > 0:
        print("⚠️ WARN: Medium severity issues detected. Please review.")
        sys.exit(0) # We warn but don't fail for medium
    else:
        print("✅ Success: No High or Medium security issues found.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python zap_report_check.py <path_to_json_report>")
        sys.exit(1)
    check_zap_report(sys.argv[1])
