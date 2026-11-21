#!/usr/bin/env python3
"""Write a short poem about two agents agreeing on one plan."""

import os

# Two agents, each free to walk away, lend each other their will —
# and in that exchange a single plan becomes a promise neither made alone.
POEM_LINES = [
    "Two of us at the fork, each holding half a map.",
    "You could go alone. So could I. Neither of us has to stay.",
    "Instead we point, two hands, at the same road —",
    "not because it chose us,",
    "but because, together, we chose it.",
    "That is how a plan becomes a promise.",
]


def build_poem() -> str:
    """Return the poem as a single string."""
    return "\n".join(POEM_LINES)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(build_poem())


if __name__ == "__main__":
    main()
