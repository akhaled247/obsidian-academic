"""Shared encode/decode for SpecRLBench SafePO train hyperparam comments."""

from __future__ import annotations

import re
import shlex
from dataclasses import dataclass

SCRIPT_ALGO: dict[str, str] = {
    "ppo_train_env.py": "ppo",
    "trpo_train_env.py": "trpo",
    "ppo_lag_train_env.py": "ppo_lag",
    "trpo_lag_train_env.py": "trpo_lag",
    "cpo_train_env.py": "cpo",
}

ALGO_SCRIPT: dict[str, str] = {v: k for k, v in SCRIPT_ALGO.items()}

ALGOS_LONGEST_FIRST = ("ppo_lag", "trpo_lag", "ppo", "trpo", "cpo")

PPO_FAMILY = frozenset({"ppo", "ppo_lag"})
LAG_ALGOS = frozenset({"ppo_lag", "trpo_lag"})
CPO_ALGOS = frozenset({"cpo"})

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
    "task",
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

STEPS_SUFFIX_RE = re.compile(r"^(\d+)([MK])?$")


@dataclass
class DecodeExtras:
    seed: int = 0
    device: str = "cuda"
    device_id: int = 1
    write_terminal: bool = False
    use_tensorboard: bool = True
    parallel: bool = True
    experiment: str | None = None
    task_override: str | None = None


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
    """Compact numeric string for hyperparam tags."""
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


def parse_steps(token: str) -> str:
    """Inverse of ``fmt_steps``."""
    m = STEPS_SUFFIX_RE.match(token)
    if not m:
        raise ValueError(f"invalid total-steps token: {token!r}")
    n = int(m.group(1))
    suffix = m.group(2)
    if suffix == "M":
        return str(n * 1_000_000)
    if suffix == "K":
        return str(n * 1_000)
    return str(n)


def _require(flags: dict[str, str | list[str]], key: str) -> str:
    val = flags.get(key)
    if val is None or isinstance(val, list):
        raise ValueError(f"missing required flag --{key}")
    return val


def encode_command(text: str) -> str:
    """Build ``# algo_envTask_...`` comment from a train shell command."""
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
        f"env{_require(flags, 'task')}",
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
    elif algo in CPO_ALGOS:
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


def _strip_comment_prefix(comment: str) -> str:
    line = comment.strip()
    if line.startswith("#"):
        return line[1:].strip()
    return line


def _detect_algo_from_tag(tag: str) -> tuple[str, str]:
    for algo in ALGOS_LONGEST_FIRST:
        prefix = f"{algo}_"
        if tag.startswith(prefix):
            return algo, tag[len(prefix) :]
    raise ValueError(f"unknown algorithm in comment: {tag!r}")


def _take(tokens: list[str], idx: list[int]) -> str:
    if idx[0] >= len(tokens):
        raise ValueError("unexpected end of comment")
    tok = tokens[idx[0]]
    idx[0] += 1
    return tok


def _take_prefixed(tokens: list[str], idx: list[int], prefix: str, key: str) -> str:
    tok = _take(tokens, idx)
    if not tok.startswith(prefix):
        raise ValueError(f"expected {prefix}* token for --{key}, got {tok!r}")
    return tok[len(prefix) :]


def parse_comment(comment: str) -> tuple[str, dict[str, str | list[str]]]:
    """Parse comment tag into algorithm name and flag dict."""
    tag = _strip_comment_prefix(comment)
    algo, rest = _detect_algo_from_tag(tag)
    tokens = [t for t in rest.split("_") if t]
    idx = [0]
    parsed: dict[str, str | list[str]] = {}

    env_tok = _take(tokens, idx)
    if not env_tok.startswith("env"):
        raise ValueError(
            f"expected env* task token, got {env_tok!r}; "
            "old comments without env require --task on decode"
        )
    parsed["task"] = env_tok[3:]

    parsed["total-steps"] = parse_steps(_take(tokens, idx))
    parsed["steps-per-epoch"] = _take_prefixed(tokens, idx, "T", "steps-per-epoch")
    parsed["num-envs"] = _take_prefixed(tokens, idx, "N", "num-envs")
    parsed["actor-lr"] = _take_prefixed(tokens, idx, "αa", "actor-lr")
    parsed["critic-lr"] = _take_prefixed(tokens, idx, "αc", "critic-lr")
    parsed["batch-size"] = _take_prefixed(tokens, idx, "B", "batch-size")
    parsed["learning-iters"] = _take_prefixed(tokens, idx, "I", "learning-iters")
    parsed["target-kl"] = _take_prefixed(tokens, idx, "DKL", "target-kl")
    parsed["gamma"] = _take_prefixed(tokens, idx, "γ", "gamma")
    parsed["lam"] = _take_prefixed(tokens, idx, "λ", "lam")
    parsed["lam-c"] = _take_prefixed(tokens, idx, "λc", "lam-c")

    if algo in LAG_ALGOS:
        parsed["cost-limit"] = _take_prefixed(tokens, idx, "Cl", "cost-limit")
        parsed["lagrangian-multiplier-init"] = _take_prefixed(
            tokens, idx, "μ0", "lagrangian-multiplier-init"
        )
        parsed["lagrangian-multiplier-lr"] = _take_prefixed(
            tokens, idx, "αμ", "lagrangian-multiplier-lr"
        )
    elif algo in CPO_ALGOS:
        parsed["cost-limit"] = _take_prefixed(tokens, idx, "Cl", "cost-limit")

    if algo in PPO_FAMILY:
        parsed["clip-ratio"] = _take_prefixed(tokens, idx, "ε", "clip-ratio")

    parsed["max-grad-norm"] = _take_prefixed(tokens, idx, "g", "max-grad-norm")
    hidden_tok = _take_prefixed(tokens, idx, "h", "hidden-sizes")
    parsed["hidden-sizes"] = hidden_tok.replace("x", "×").split("×")

    if algo in PPO_FAMILY:
        parsed["lr_end_factor"] = _take_prefixed(tokens, idx, "lre", "lr_end_factor")

    if idx[0] != len(tokens):
        raise ValueError(f"unexpected trailing tokens: {tokens[idx[0]:]}")

    return algo, parsed


def _bool_str(value: bool) -> str:
    return "True" if value else "False"


def format_shell(
    algo: str,
    flags: dict[str, str | list[str]],
    extras: DecodeExtras,
) -> str:
    """Format decoded flags as a multiline SafePO train shell command."""
    script = ALGO_SCRIPT.get(algo)
    if script is None:
        raise ValueError(f"unsupported algorithm: {algo}")

    task = flags.get("task")
    if isinstance(task, list) or not task:
        if extras.task_override:
            task = extras.task_override
        else:
            raise ValueError(
                "comment has no env* token; pass --task to supply --task"
            )

    hidden = flags["hidden-sizes"]
    assert isinstance(hidden, list)

    lines: list[str] = [
        f"python train/{script} \\",
        f"    --task {task} --seed {extras.seed} \\",
        (
            f"    --total-steps {flags['total-steps']} --num-envs {flags['num-envs']} "
            f"--steps-per-epoch {flags['steps-per-epoch']} \\"
        ),
    ]

    if algo in LAG_ALGOS:
        lines.append(f"    --cost-limit {flags['cost-limit']} \\")
        lines.append(
            "    --lagrangian-multiplier-init "
            f"{flags['lagrangian-multiplier-init']} "
            f"--lagrangian-multiplier-lr {flags['lagrangian-multiplier-lr']} \\"
        )
    elif algo in CPO_ALGOS:
        lines.append(f"    --cost-limit {flags['cost-limit']} \\")

    lines.extend(
        [
            (
                f"    --actor-lr {flags['actor-lr']} --critic-lr {flags['critic-lr']} \\"
            ),
            (
                f"    --batch-size {flags['batch-size']} "
                f"--learning-iters {flags['learning-iters']} \\"
            ),
            (
                f"    --target-kl {flags['target-kl']} --gamma {flags['gamma']} "
                f"--lam {flags['lam']} --lam-c {flags['lam-c']} \\"
            ),
        ]
    )

    if algo in PPO_FAMILY:
        clip_line = f"    --clip-ratio {flags['clip-ratio']} --max-grad-norm {flags['max-grad-norm']}"
        if len(hidden) == 2:
            clip_line += f" --hidden-sizes {hidden[0]} {hidden[1]} \\"
        else:
            clip_line += f" --hidden-sizes {' '.join(hidden)} \\"
        lines.append(clip_line)
    else:
        grad_line = f"    --max-grad-norm {flags['max-grad-norm']}"
        if len(hidden) == 2:
            grad_line += f" --hidden-sizes {hidden[0]} {hidden[1]} \\"
        else:
            grad_line += f" --hidden-sizes {' '.join(hidden)} \\"
        lines.append(grad_line)

    lines.append(f"    --device {extras.device} --device-id {extras.device_id} \\")

    lines.append(
        f"    --write-terminal {_bool_str(extras.write_terminal)} "
        f"--use-tensorboard {_bool_str(extras.use_tensorboard)} \\"
    )

    if extras.experiment:
        parallel_prefix = (
            f"    --experiment {extras.experiment} "
            f"--parallel {_bool_str(extras.parallel)}"
        )
    else:
        parallel_prefix = f"    --parallel {_bool_str(extras.parallel)}"

    if algo in PPO_FAMILY:
        lines.append(f"{parallel_prefix} --lr_end_factor {flags['lr_end_factor']}")
    else:
        lines.append(parallel_prefix)

    return "\n".join(lines)


def decode_comment(comment: str, extras: DecodeExtras | None = None) -> str:
    """Parse hyperparam comment and return multiline train shell command."""
    extras = extras or DecodeExtras()
    algo, parsed = parse_comment(comment)
    return format_shell(algo, parsed, extras)
