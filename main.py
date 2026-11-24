"""Everyday Wonder — make.fun entry.

Writes one sentence (119 characters) about a small everyday wonder to /output/entry.txt.
An ordinary low-sun shadow arriving at the corner first turns a daily walk
strange and new — a small moment of wonder in something seen every day.
"""

import os

MAX_LEN = 200

# Chosen sentence (119 characters): a small everyday wonder.
# The image: a low sun stretches the speaker's shadow ahead of them,
# so it reaches the corner first, impatient, like it can't wait to arrive.
LINE = "My shadow arrived at the corner before I did, stretched long by the low sun, as if it couldn't wait to get there first."

assert 1 <= len(LINE) <= MAX_LEN, "line out of gate"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE
