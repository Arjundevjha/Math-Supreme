## 2025-05-18 - Precompute Negated Terms in Taylor Series Loops
**Learning:** In float Taylor series loops (`sine_taylor`, `cosine_taylor`), computing `-radians_sq` inside the loop causes redundant unary negation on every term evaluation. Precomputing `neg_radians_sq = -x * x` outside the loop eliminates unary negation operations per iteration.
**Action:** Always precompute negative powers/constants outside Taylor series loop iterations when signs alternate per step.
