## 2025-05-18 - Eliminating Custom Iterative Root Solvers in Analytical Formulas

**Learning:** Closed-form algebraic solvers (e.g. `cubic_formula`) should not invoke custom iterative Newton-Raphson routines (`nth_root`) for fixed algebraic constants (like $\sqrt{3}$) or intermediate float terms, as running 100-iteration loops on every call creates a massive bottleneck. Precomputing constants at module level (`SQRT_3 = 3.0 ** 0.5`) and using IEEE 754 exponentiation (`** 0.5`) along with single-evaluation cube root caching (`cb1`, `cb2`) and reciprocal factor precomputation (`inv_3a`, `inv_6a`) yields ~2x faster execution.
**Action:** Audit analytical solvers for redundant custom numerical approximation calls and replace them with precomputed constants and native float operations.
