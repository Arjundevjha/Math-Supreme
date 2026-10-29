## 2026-03-31 - Single-pass list comprehension for second derivatives

**Learning:** Computing polynomial second derivatives by chaining two derivative function calls (`compute_polynomial_derivative`) creates unnecessary intermediate list and tuple allocations and function invocation overhead. Applying the second derivative power rule directly in a single pass using list comprehension `[(c * p * (p - 1), p - 2) for c, p in zip(coeffs, powers) if p != 0 and p != 1]` yields a ~33-50% speedup.

**Action:** Directly apply mathematical power rules in single-pass comprehensions for derivative calculations rather than chaining intermediate differentiation calls.
