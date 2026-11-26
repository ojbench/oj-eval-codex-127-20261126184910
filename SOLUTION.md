# Card Master

Add permanent boundary cards of value 1. Let `dp[l][r]` be the maximum
reward from burning all cards strictly between surviving boundaries `l` and `r`.
If `k` is the last interior card burned, its reward is `a[l]*a[k]*a[r]`.
The two sides are independent while `k` survives, giving

```
dp[l][r] = max(dp[l][k] + dp[k][r] + a[l]*a[k]*a[r])
           for l < k < r.
```

Empty intervals have reward zero. Every burning order has a last card, so the
recurrence covers every possible order; conversely, optimal orders on the two
sides followed by `k` attain each candidate. Induction on interval length proves
the result `dp[0][n+1]` is optimal.

Process right boundaries in increasing order and left boundaries in decreasing
order so both subintervals are available. Two transposed copies of the DP table
make both reads in the innermost loop contiguous. Time is O(n^3), with about
167 million candidates at n=1000; space is O(n^2), about 16 MB. Rewards are at
most n*10^12, so signed 64-bit arithmetic suffices.

Build with `cmake -S . -B build && cmake --build build`.
Run local verification with `python3 tests/check.py ./build/code`.
