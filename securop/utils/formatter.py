import sys
from typing import List, Dict

# ANSI background colors for output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def format_status(name: str, passed: bool, issues_count: int = 0) -> str:
    """Format the scanner status for display."""
    if passed:
        return f"{Colors.OKGREEN}✅ {name}: Passed{Colors.ENDC}"
    else:
        status = f"❌ {name}: Failed" if issues_count == 0 else f"⚠️ {name}: {issues_count} issues"
        return f"{Colors.FAIL}{status}{Colors.ENDC}"

def print_result(results: Dict[str, Dict]):
    """Print the formatted results of all scanners."""
    print("\n--- SecurOps Scan Results ---")
    all_passed = True
    for name, result in results.items():
        print(format_status(name, result['passed'], result.get('issues', 0)))
        if not result['passed']:
            all_passed = False
            if result.get('output') and result.get('verbose'):
                print(f"{Colors.BOLD}Details for {name}:{Colors.ENDC}")
                print(result['output'])
    
    if all_passed:
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}✅ Scan passed!{Colors.ENDC}")
    else:
        print(f"\n{Colors.FAIL}{Colors.BOLD}❌ Scan failed!{Colors.ENDC}")
        sys.exit(1)
