import click
import sys
import os
import shutil
import subprocess
import pkg_resources
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

@cli.command()
def init():
    """Initialize SecurOps in the current project (install binaries, setup hooks)."""
    click.echo("🚀 Initializing SecurOps...")
    
    # 1. Detect Git
    if not os.path.exists(".git"):
        click.echo("⚠️  Warning: No .git directory found. Git hooks will be skipped.")
        has_git = False
    else:
        has_git = True

    # 2. Install binaries (using bundled script)
    try:
        script_path = pkg_resources.resource_filename('securop', 'scripts/install_tools.sh')
        click.echo(f"📦 Installing security tools...")
        subprocess.run(["bash", script_path], check=True)
    except Exception as e:
        click.echo(f"❌ Error installing tools: {e}")

    # 3. Setup Git Hooks
    if has_git:
        try:
            hook_src = pkg_resources.resource_filename('securop', 'hooks/pre-commit.sh')
            hook_dst = ".git/hooks/pre-commit"
            shutil.copy(hook_src, hook_dst)
            os.chmod(hook_dst, 0o755)
            click.echo("✅ Git pre-commit hook installed at .git/hooks/pre-commit")
        except Exception as e:
            click.echo(f"❌ Error setting up hooks: {e}")

    # 4. Create default .semgrep.yml if not exists
    if not os.path.exists(".semgrep.yml"):
        try:
            template_path = pkg_resources.resource_filename('securop', 'templates/default_semgrep.yml')
            shutil.copy(template_path, ".semgrep.yml")
            click.echo("✅ Created default .semgrep.yml with standard mobile security rules.")
        except Exception as e:
            click.echo(f"❌ Error creating .semgrep.yml: {e}")
    else:
        click.echo("ℹ️  .semgrep.yml already exists, skipping.")

    click.echo("🎉 SecurOps initialization complete! You can now run 'securop scan'.")

if __name__ == '__main__':
    cli()
