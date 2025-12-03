import subprocess
import sys
import pytest

# Path to the cli.py script
CLI_PATH = "src/cli.py"

def run_cli(expression):
    """Helper function to run the CLI script and capture output."""
    cmd = [sys.executable, CLI_PATH, expression]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return result

def test_us2_cli_operator_precedence_multiplication_addition():
    # Expected to fail initially until precedence is implemented in evaluate.py
    result = run_cli("2+3*4")
    assert "14.0" in result.stdout.strip()
    assert result.returncode == 0

def test_us2_cli_operator_precedence_division_subtraction():
    # Expected to fail initially until precedence is implemented in evaluate.py
    result = run_cli("10-4/2")
    assert "8.0" in result.stdout.strip()
    assert result.returncode == 0

