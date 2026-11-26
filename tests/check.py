"""Compare the executable with exhaustive search and benchmark maximum inputs."""
import functools
import random
import subprocess
import sys
import time


@functools.lru_cache(None)
def brute(cards):
    if not cards:
        return 0
    return max(
        card * (cards[i - 1] if i else 1)
        * (cards[i + 1] if i + 1 < len(cards) else 1)
        + brute(cards[:i] + cards[i + 1:])
        for i, card in enumerate(cards)
    )


def run(cards):
    data = f"{len(cards)}\n" + " ".join(map(str, cards)) + "\n"
    return int(subprocess.check_output([executable], input=data.encode()))


executable = sys.argv[1] if len(sys.argv) > 1 else "./build/code"
rng = random.Random(127)
assert run([3, 5, 6, 2, 5]) == 305
for n in range(1, 9):
    for _ in range(100):
        cards = tuple(rng.randint(1, 10) for _ in range(n))
        assert run(cards) == brute(cards), cards
        brute.cache_clear()
print("Sample and 800 exhaustive-search comparisons passed.")
for cards in ([1] * 1000, [10000] * 1000,
              [rng.randint(1, 10000) for _ in range(1000)]):
    start = time.perf_counter()
    result = run(cards)
    elapsed = time.perf_counter() - start
    if len(set(cards)) == 1:
        v = cards[0]
        assert result == 998 * v ** 3 + v ** 2 + v
    print(f"n=1000: result={result}, elapsed={elapsed:.3f}s")
