from ..utils.runner import run_command

def scan(fast: bool = False, ci: bool = False) -> dict:
    """Run Gitleaks scan."""
    command = "gitleaks protect --staged" if fast else "gitleaks detect"
    
    # In CI, we want to run a full detect scan
    if ci:
        command = "gitleaks detect"
        
    result = run_command(command)
    
    # Gitleaks exit codes: 0 for no leaks, 1 for leaks, 126 and others for errors.
    passed = result.returncode == 0
    
    return {
        "name": "🔐 Secrets Scan",
        "passed": passed,
        "output": result.stdout if not passed else "",
        "issues": result.stdout.count("leak") if not passed else 0,
        "exit_code": result.returncode
    }
