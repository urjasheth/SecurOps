from ..utils.runner import run_command

def scan(fast: bool = False, ci: bool = False) -> dict:
    """Run Trivy scan."""
    command = "trivy fs . --skip-dirs venv,.git,node_modules,vendor"
    
    if fast:
        # Only HIGH and CRITICAL vulnerabilities
        command += " --severity HIGH,CRITICAL"
        
    if ci:
        # Full scan
        command += " --severity LOW,MEDIUM,HIGH,CRITICAL"

    # Trivy exit codes: 0 for no matches, 1 for matches (when --exit-code 1 is used)
    command += " --exit-code 1 --quiet"

    result = run_command(command)
    
    passed = result.returncode == 0
    
    return {
        "name": "📦 Dependencies",
        "passed": passed,
        "output": result.stdout if not passed else "",
        "issues": result.stdout.count("Total:") if not passed else 0,
        "exit_code": result.returncode
    }
