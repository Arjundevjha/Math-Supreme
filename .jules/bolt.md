## 2026-03-31 - Chudnovsky Pi Algorithm Loop Upper Bound

**Learning:** `calculate_pi_chudnovsky` previously defaulted to `precision` iterations in its series summation loop. However, each term in the Chudnovsky series produces ~14.18 decimal digits of precision. Running loop bounds up to `precision` (e.g., 1000 iterations for precision 1000) causes redundant, high-precision `Decimal` arithmetic operations. Computing `num_terms = max(1, math.ceil((precision + 20) / 14.181647462725477))` drastically reduces iterations (e.g. from 1000 to 72) and yields over 10x speedup while preserving full accuracy.

**Action:** When working with rapidly converging series algorithms (e.g., Chudnovsky, Ramanujan), calculate the mathematically required number of terms based on the term convergence rate instead of defaulting to `range(1, precision)`.
