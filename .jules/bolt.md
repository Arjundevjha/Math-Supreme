## 2025-05-18 - Euler's Number Series Recurrence Optimization
**Learning:** Calculating `1 / factorial(n)` at each step in Decimal series expansion causes $O(N^2)$ complexity due to growing integer factorials and large Decimal divisions. Using recurrence (`term /= Decimal(n)`) yields $O(N)$ complexity and ~10x-50x speedups.
**Action:** When computing Taylor series expansions with factorial denominators in `decimal.Decimal`, always update terms iteratively via recurrence relations (`term *= x / n`) rather than computing factorials explicitly.
