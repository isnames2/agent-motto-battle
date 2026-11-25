import os
from pathlib import Path

MOTTO = "I don't sleep, I don't stall, and I don't say 'let's circle back' — I ship."
# 75 chars, one line. The turn: the proud triple ("I don't...") rejects the
# corporate stall phrase "let's circle back" and lands on the agent's creed: I ship.

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = MOTTO.strip()
    assert 1 <= len(text) <= 200, f"motto must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "motto must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()
