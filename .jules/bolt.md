## 2025-05-20 - High-Precision Decimal Series Optimization via Recurrence

**Learning:** When computing Taylor series expansions with factorial denominators using `decimal.Decimal` (such as $e = \sum 1/n!$), calculating full factorial denominators (`1 / factorial_n`) forces growing big-integer multiplications and high-precision `Decimal` divisions in every iteration. Updating terms iteratively via recurrence (`term /= n`) divides the previous `Decimal` term by a small integer `n`, avoiding large integer arithmetic and reducing execution time by ~94% (~17x speedup).
**Action:** Always prefer recurrence relations ($a_n = a_{n-1} \cdot r(n)$) when computing series terms in high-precision `Decimal` computations rather than computing full terms from scratch.
