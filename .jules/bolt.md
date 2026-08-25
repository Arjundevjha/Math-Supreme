# Bolt's Journal - Critical Learnings

## 2026-03-30 - Multiplicative iterative nCr vs triple factorial
**Learning:** Computing `nCr` using `factorial(n) // (factorial(r) * factorial(n - r))` computes three large factorial values, doing redundant multiplications and creating very large intermediate integers. Replacing it with `r = min(r, n - r)` and product loop reduces computation time by up to ~15x for large `n` / small `r`, while keeping exact integer arithmetic.
**Action:** Always prefer multiplicative form with symmetry `min(r, n - r)` when implementing combination (`nCr`) functions.
