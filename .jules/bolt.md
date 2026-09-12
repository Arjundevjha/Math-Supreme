## 2025-05-15 - Replacing Pure Python Combination Product Loops with math.comb

**Learning:** Replacing pure Python iterative loops for combination calculations $C(n, r)$ with Python 3.8+'s built-in C-accelerated `math.comb` yields up to ~3x performance improvements without losing numerical precision for large integers.
**Action:** When calculating combinations $nCr$, delegate calculation to `math.comb(n, r)` while preserving custom input type checks and explicit exception messages required by existing test suites.
