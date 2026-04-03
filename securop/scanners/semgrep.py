from ..utils.runner import run_command

def scan(fast: bool = False, ci: bool = False) -> dict:
    """Run Semgrep scan."""
    # Use local .semgrep.yml if it exists, otherwise fallback to auto
    import os
    config_path = ".semgrep.yml"
    config_arg = f"--config={config_path}" if os.path.exists(config_path) else "--config=auto"
    
    command = f"semgrep {config_arg} --error --exclude venv --exclude .git --exclude node_modules --exclude vendor"
    
    if fast:
        # Limited rules and smaller files
        command += " --max-target-bytes=1000000 --timeout=5"
        
    if ci:
        # Full scan
        pass # semgrep config handles this

    result = run_command(command)
    
    # Semgrep exit codes: 0 for no matches, 1 for matches (when --error is used)
    passed = result.returncode == 0
    
    return {
        "name": "🔍 Code Scan",
        "passed": passed,
        "output": result.stdout if not passed else "",
        "issues": result.stdout.count("Findings:") if not passed else 0,
        "exit_code": result.returncode
    }
