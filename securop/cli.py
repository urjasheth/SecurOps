import click
import sys
from .scanners import gitleaks, semgrep, trivy
from .utils.formatter import print_result

@click.group()
def cli():
    """SecurOps: A developer-friendly local security toolkit."""
    pass

@cli.command()
@click.option('--fast/--no-fast', default=True, help="Run in fast mode (default: staged/high/critical only)")
@click.option('--ci/--no-ci', default=False, help="Run in CI mode (full scan, strict exit codes)")
@click.option('--verbose', is_flag=True, help="Display raw logs from scanners")
def scan(fast, ci, verbose):
    """Run security scans (Gitleaks, Semgrep, Trivy)."""
    results = {}
    
    # Run Gitleaks
    results["Gitleaks"] = gitleaks.scan(fast=fast, ci=ci)
    results["Gitleaks"]["verbose"] = verbose
    
    # Run Semgrep
    results["Semgrep"] = semgrep.scan(fast=fast, ci=ci)
    results["Semgrep"]["verbose"] = verbose
    
    # Run Trivy
    results["Trivy"] = trivy.scan(fast=fast, ci=ci)
    results["Trivy"]["verbose"] = verbose
    
    # Print results and handle exit code
    print_result(results)

if __name__ == '__main__':
    cli()
