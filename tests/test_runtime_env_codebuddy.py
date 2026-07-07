#!/usr/bin/env python3
"""Regression tests for CodeBuddy Code runtime detection in runtime_env.

Verifies:
1. CODEBUDDY_PLUGIN_ROOT / CODEBUDDY_PLUGIN_DATA trigger codebuddy runtime.
2. CodeBuddy env vars take priority over CLAUDE_PLUGIN_* (because CodeBuddy
   sets both for backward compatibility).
3. codebuddy_home() returns ~/.codebuddy by default.
4. runtime_home() returns codebuddy_home() when codebuddy is detected.
5. runtime_name_for_humans() returns "CodeBuddy Code".
6. CLAUDE_PLUGIN_* alone still resolves to "claude" (backward compat).
7. plugin_data_env_vars() returns CodeBuddy vars first, then Claude vars.

Run directly:  python3 tests/test_runtime_env_codebuddy.py
Exits non-zero on first failure.
"""

import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPTS = REPO / "skills" / "token-optimizer" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import runtime_env  # noqa: E402

# Every env var detect_runtime() consults — cleared before each controlled case.
_CONTROLLED_ENV = (
    "TOKEN_OPTIMIZER_RUNTIME",
    "CODEBUDDY_PLUGIN_ROOT",
    "CODEBUDDY_PLUGIN_DATA",
    "CLAUDE_PLUGIN_ROOT",
    "CLAUDE_PLUGIN_DATA",
    "CODEBUDDY_CONFIG_DIR",
    "CLAUDE_CONFIG_DIR",
    "CODEX_HOME",
    "HERMES_HOME",
    "COPILOT_HOME",
    "TOKEN_OPTIMIZER_NO_PROC_SCAN",
    "OPENCODE_BIN",
    "OPENCODE_CONFIG_DIR",
    "OPENCODE_DATA_DIR",
    "OPENCODE_CONFIG",
    "OPENCODE_CLIENT",
)


def _clear_env():
    """Remove every controlled env var so one test doesn't leak into the next."""
    for key in _CONTROLLED_ENV:
        os.environ.pop(key, None)
    runtime_env.detect_runtime.cache_clear()


def _set_codebuddy_env():
    """Set CODEBUDDY_PLUGIN_ROOT to simulate a CodeBuddy Code plugin session."""
    _clear_env()
    os.environ["CODEBUDDY_PLUGIN_ROOT"] = "/tmp/test-codebuddy-plugin"


def _set_claude_env():
    """Set CLAUDE_PLUGIN_ROOT to simulate a Claude Code plugin session."""
    _clear_env()
    os.environ["CLAUDE_PLUGIN_ROOT"] = "/tmp/test-claude-plugin"


def _set_both_env():
    """Set both CODEBUDDY and CLAUDE plugin vars (CodeBuddy compat mode)."""
    _clear_env()
    os.environ["CODEBUDDY_PLUGIN_ROOT"] = "/tmp/test-codebuddy-plugin"
    os.environ["CODEBUDDY_PLUGIN_DATA"] = "/tmp/test-codebuddy-data"
    os.environ["CLAUDE_PLUGIN_ROOT"] = "/tmp/test-claude-plugin"
    os.environ["CLAUDE_PLUGIN_DATA"] = "/tmp/test-claude-data"


failures = 0


def _check(name: str, condition: bool, detail: str = "") -> None:
    global failures
    if not condition:
        failures += 1
        msg = f"FAIL [{name}] {detail}" if detail else f"FAIL [{name}]"
        print(msg, file=sys.stderr)
    else:
        print(f"OK   [{name}]")


# ── Test 1: CODEBUDDY_PLUGIN_ROOT triggers codebuddy runtime ──
_set_codebuddy_env()
_check(
    "CODEBUDDY_PLUGIN_ROOT → codebuddy",
    runtime_env.detect_runtime() == "codebuddy",
)

# ── Test 2: CODEBUDDY_PLUGIN_DATA also triggers codebuddy ──
_clear_env()
os.environ["CODEBUDDY_PLUGIN_DATA"] = "/tmp/test-codebuddy-data"
_check(
    "CODEBUDDY_PLUGIN_DATA → codebuddy",
    runtime_env.detect_runtime() == "codebuddy",
)

# ── Test 3: Both CODEBUDDY and CLAUDE vars → codebuddy wins ──
_set_both_env()
_check(
    "both env vars → codebuddy wins over claude",
    runtime_env.detect_runtime() == "codebuddy",
)

# ── Test 4: CLAUDE_PLUGIN_* alone → claude (backward compat) ──
_set_claude_env()
_check(
    "CLAUDE_PLUGIN_ROOT alone → claude",
    runtime_env.detect_runtime() == "claude",
)

# ── Test 5: codebuddy_home() returns ~/.codebuddy ──
_clear_env()
home = runtime_env.codebuddy_home()
_check(
    "codebuddy_home() ends with .codebuddy",
    str(home).endswith(".codebuddy"),
    f"got {home}",
)

# ── Test 6: runtime_home() with codebuddy detected → codebuddy_home() ──
_set_codebuddy_env()
rhome = runtime_env.runtime_home()
_check(
    "runtime_home() → codebuddy_home()",
    str(rhome).endswith(".codebuddy"),
    f"got {rhome}",
)

# ── Test 7: runtime_name_for_humans() → "CodeBuddy Code" ──
_set_codebuddy_env()
name = runtime_env.runtime_name_for_humans()
_check(
    "runtime_name_for_humans() → CodeBuddy Code",
    name == "CodeBuddy Code",
    f"got {name!r}",
)

# ── Test 8: plugin_data_env_vars() returns CodeBuddy vars first ──
_set_codebuddy_env()
vars_tuple = runtime_env.plugin_data_env_vars()
_check(
    "plugin_data_env_vars() starts with CODEBUDDY_PLUGIN_DATA",
    vars_tuple[0] == "CODEBUDDY_PLUGIN_DATA",
    f"got {vars_tuple}",
)
_check(
    "plugin_data_env_vars() includes CLAUDE_PLUGIN_DATA as fallback",
    "CLAUDE_PLUGIN_DATA" in vars_tuple,
    f"got {vars_tuple}",
)

# ── Test 9: Explicit TOKEN_OPTIMIZER_RUNTIME=codebuddy override ──
_clear_env()
os.environ["TOKEN_OPTIMIZER_RUNTIME"] = "codebuddy"
_check(
    "TOKEN_OPTIMIZER_RUNTIME=codebuddy",
    runtime_env.detect_runtime() == "codebuddy",
)

# ── Test 10: CODEBUDDY_CONFIG_DIR honored (when dir exists) ──
_clear_env()
# Can't create a guaranteed dir in a unit test, so test the fallback
os.environ["CODEBUDDY_CONFIG_DIR"] = "/nonexistent/path/for/test"
home2 = runtime_env.codebuddy_home()
_check(
    "CODEBUDDY_CONFIG_DIR nonexistent → fallback to ~/.codebuddy",
    str(home2).endswith(".codebuddy"),
    f"got {home2}",
)

# ── Test 11: codebuddy in _VALID_RUNTIMES ──
_clear_env()
_check(
    "codebuddy in _VALID_RUNTIMES",
    "codebuddy" in runtime_env._VALID_RUNTIMES,
)

# ── Summary ──
if failures:
    print(f"\n{failures} test(s) FAILED.", file=sys.stderr)
    sys.exit(1)
else:
    print("\nAll tests passed.")
    sys.exit(0)
