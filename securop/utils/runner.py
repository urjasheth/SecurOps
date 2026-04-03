import subprocess
import shlex
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class CommandResult:
    command: str
    stdout: str
    stderr: str
    returncode: int
    success: bool

def run_command(command: str, cwd: Optional[str] = None) -> CommandResult:
    """Run a shell command and return the result."""
    try:
        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=cwd
        )
        stdout, stderr = process.communicate()
        return CommandResult(
            command=command,
            stdout=stdout.strip(),
            stderr=stderr.strip(),
            returncode=process.returncode,
            success=process.returncode == 0
        )
    except Exception as e:
        return CommandResult(
            command=command,
            stdout="",
            stderr=str(e),
            returncode=1,
            success=False
        )
