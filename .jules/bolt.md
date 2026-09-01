## 2025-05-18 - Chudnovsky Algorithm Term Count Optimization
**Learning:** In Chudnovsky series for Pi calculation, each series term yields ~14.18 digits of precision. Iterating `precision` times instead of `(precision + 13) // 14` performs redundant high-precision Decimal divisions, causing an 8x-18x performance degradation.
**Action:** When implementing or optimizing series expansions, determine exact convergence rate per term to bound loop iterations tightly based on required precision.
