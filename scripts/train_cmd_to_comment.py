#!/usr/bin/env python3
"""Convert SpecRLBench SafePO train shell commands to compact hyperparam comments.

Example:
  python train/ppo_train_env.py --total-steps 5000000 ... \\
  → # ppo_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0

Supports: ppo, trpo, ppo_lag, trpo_lag, cpo (train/*_train_env.py).
"""

from __future__ import annotations

import argparse
import re
import shlex
import sys
from pathlib import Path

SCRIPT_ALGO: dict[str, str] = {
    "ppo_train_env.py": "ppo",
    "trpo_train_env.py": "trpo",
    "ppo_lag_train_env.py": "ppo_lag",
    "trpo_lag_train_env.py": "trpo_lag",
    "cpo_train_env.py": "cpo",
}

PPO_FAMILY = frozenset({"ppo", "ppo_lag"})
LAG_ALGOS = frozenset({"ppo_lag", "trpo_lag"})

CANONICAL_FLAGS = {
    "task",
    "seed",
    "total-steps",
    "num-envs",
    "steps-per-epoch",
    "actor-lr",
    "critic-lr",
    "batch-size",
    "learning-iters",
    "target-kl",
    "gamma",
    "lam",
    "lam-c",
    "clip-ratio",
    "max-grad-norm",
    "hidden-sizes",
    "lr_end_factor",
    "cost-limit",
    "lagrangian-multiplier-init",
    "lagrangian-multiplier-lr",
    "algo",
}

REQUIRED_CORE = (
    "total-steps",
    "steps-per-epoch",
    "num-envs",
    "actor-lr",
    "critic-lr",
    "batch-size",
    "learning-iters",
    "target-kl",
    "gamma",
    "lam",
    "lam-c",
    "max-grad-norm",
    "hidden-sizes",
)


def normalize_shell(text: str) -> str:
    """Join line continuations and drop standalone comment lines."""
    lines: list[str] = []
    for raw in text.splitlines():
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.startswith("#") and not stripped.startswith("#!"):
            continue
        lines.append(stripped)

    joined = " ".join(lines)
    joined = re.sub(r"\\\s+", " ", joined)
    return joined.strip()


def _canonical_flag(token: str) -> str | None:
    if not token.startswith("--"):
        return None
    name = token[2:]
    aliases = {
        "env-id": "task",
        "lr-end-factor": "lr_end_factor",
        "lr_end_factor": "lr_end_factor",
    }
    if name in aliases:
        return aliases[name]
    if name in CANONICAL_FLAGS:
        return name
    return None


def parse_flags(text: str) -> dict[str, str | list[str]]:
    """Parse ``python train/...py --flag value ...`` into a flag dict."""
    normalized = normalize_shell(text)
    if not normalized:
        raise ValueError("empty command after normalization")

    tokens = shlex.split(normalized)
    flags: dict[str, str | list[str]] = {}
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if not tok.startswith("--"):
            i += 1
            continue

        key = _canonical_flag(tok)
        if key is None:
            i += 1
            continue

        if i + 1 >= len(tokens) or tokens[i + 1].startswith("--"):
            raise ValueError(f"missing value for {tok}")
        i += 1

        if key == "hidden-sizes":
            sizes: list[str] = []
            while i < len(tokens) and not tokens[i].startswith("--"):
                sizes.append(tokens[i])
                i += 1
            flags[key] = sizes
            continue

        flags[key] = tokens[i]
        i += 1

    return flags


def detect_algo(text: str, flags: dict[str, str | list[str]]) -> str:
    """Detect algorithm from script basename or --algo."""
    normalized = normalize_shell(text)
    for script, algo in SCRIPT_ALGO.items():
        if script in normalized:
            return algo

    algo_flag = flags.get("algo")
    if isinstance(algo_flag, str) and algo_flag in SCRIPT_ALGO.values():
        return algo_flag

    raise ValueError(
        "unknown or missing algorithm; expected train/{ppo,trpo,ppo_lag,trpo_lag,cpo}_train_env.py "
        "or --algo"
    )


def _format_scientific(f: float) -> str:
    mantissa, exp = f"{f:e}".split("e")
    mantissa = mantissa.rstrip("0").rstrip(".") or "0"
    exp_i = int(exp)
    return f"{mantissa}e{exp_i}"


def fmt_num(value: str, *, style: str = "auto") -> str:
    """Compact numeric string for hyperparam tags.

    style:
      - ``decimal``: keep decimal form (0.05, 0.995, 1.0)
      - ``scientific``: prefer 5e-5 / 1e-2 style for small magnitudes
      - ``auto``: preserve ``e`` input; else decimal unless |f| < 0.001
    """
    s = value.strip()
    if not s:
        raise ValueError("empty numeric value")

    if "e" in s.lower():
        return _format_scientific(float(s))

    f = float(s)
    if f == 0.0:
        return "0"

    if f == int(f):
        if "." in s and s.endswith(".0"):
            return s
        return str(int(f))

    if style == "scientific" or (style == "auto" and abs(f) < 0.001):
        return _format_scientific(f)

    out = f"{f:f}".rstrip("0").rstrip(".")
    return out if out else "0"


def fmt_steps(value: str) -> str:
    """Format total-steps as 5M / 400K / raw."""
    n = int(float(value))
    if n % 1_000_000 == 0:
        return f"{n // 1_000_000}M"
    if n % 1_000 == 0:
        return f"{n // 1_000}K"
    return str(n)


def _require(flags: dict[str, str | list[str]], key: str) -> str:
    val = flags.get(key)
    if val is None or isinstance(val, list):
        raise ValueError(f"missing required flag --{key}")
    return val


def build_comment(text: str) -> str:
    """Build ``# algo_...`` comment from a train shell command."""
    flags = parse_flags(text)
    algo = detect_algo(text, flags)

    for key in REQUIRED_CORE:
        if key not in flags:
            raise ValueError(f"missing required flag --{key}")

    hidden = flags["hidden-sizes"]
    if not isinstance(hidden, list) or not hidden:
        raise ValueError("missing required flag --hidden-sizes")

    parts: list[str] = [
        algo,
        fmt_steps(_require(flags, "total-steps")),
        f"T{fmt_num(_require(flags, 'steps-per-epoch'))}",
        f"N{fmt_num(_require(flags, 'num-envs'))}",
        f"αa{fmt_num(_require(flags, 'actor-lr'), style='scientific')}",
        f"αc{fmt_num(_require(flags, 'critic-lr'), style='scientific')}",
        f"B{fmt_num(_require(flags, 'batch-size'))}",
        f"I{fmt_num(_require(flags, 'learning-iters'))}",
        f"DKL{fmt_num(_require(flags, 'target-kl'), style='decimal')}",
        f"γ{fmt_num(_require(flags, 'gamma'), style='decimal')}",
        f"λ{fmt_num(_require(flags, 'lam'), style='decimal')}",
        f"λc{fmt_num(_require(flags, 'lam-c'), style='decimal')}",
    ]

    if algo in LAG_ALGOS:
        parts.extend(
            [
                f"Cl{fmt_num(_require(flags, 'cost-limit'), style='decimal')}",
                f"μ0{fmt_num(_require(flags, 'lagrangian-multiplier-init'), style='decimal')}",
                f"αμ{fmt_num(_require(flags, 'lagrangian-multiplier-lr'), style='scientific')}",
            ]
        )
    elif algo == "cpo":
        parts.append(f"Cl{fmt_num(_require(flags, 'cost-limit'), style='decimal')}")

    if algo in PPO_FAMILY:
        parts.append(f"ε{fmt_num(_require(flags, 'clip-ratio'), style='decimal')}")

    parts.append(f"g{fmt_num(_require(flags, 'max-grad-norm'))}")
    parts.append("h" + "×".join(fmt_num(x) for x in hidden))

    if algo in PPO_FAMILY:
        lre = flags.get("lr_end_factor")
        if lre is None:
            raise ValueError("missing required flag --lr_end_factor for PPO-family algos")
        parts.append(f"lre{fmt_num(str(lre), style='decimal')}")

    return "# " + "_".join(parts)


def _read_input(path: str | None) -> str:
    if path is None:
        if sys.stdin.isatty():
            print("Paste train command, then EOF (Ctrl-D / Ctrl-Z):", file=sys.stderr)
        return sys.stdin.read()
    p = Path(path)
    if p.is_file():
        return p.read_text(encoding="utf-8")
    return path


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Convert SpecRLBench SafePO train shell commands to hyperparam comments."
    )
    parser.add_argument(
        "command",
        nargs="?",
        help="Train command string, file path, or omit to read stdin",
    )
    args = parser.parse_args(argv)

    try:
        raw = _read_input(args.command)
        comment = build_comment(raw)
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(comment)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
