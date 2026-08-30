## 2025-05-18 - Fast Pure-Python Factorial via Binary Split Multiplication

**Learning:** For pure-Python factorial calculations where standard `math` module imports are prohibited by project guidelines (AGENTS.md), simple iterative multiplication (`1 * 2 * ... * n`) becomes a bottleneck for large `n` because multiplying a small number by a rapidly growing multi-digit integer scales poorly. Replacing the linear loop with divide-and-conquer (binary split) range multiplication balances the bit size of operands across subtrees, unlocking Python's C-implemented Karatsuba multiplication algorithm and yielding significant speedups (over 5x faster for n=20,000).

**Action:** When optimizing product ranges or factorials without using standard library extensions, prefer binary tree multiplication over iterative range loops.
