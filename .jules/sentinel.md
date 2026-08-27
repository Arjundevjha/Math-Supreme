## 2025-02-23 - Pascals Triangle DoS via Unbounded Input
**Vulnerability:** `generate_pascals_triangle(num_rows)` generated nested lists of size O(num_rows^2) without checking input type or an upper bound, allowing denial-of-service (DoS) attacks via memory exhaustion or high CPU usage when passed huge values or non-integer types like `True` or strings.
**Learning:** Functions allocating memory proportional to input parameter size must strictly validate parameter types and enforce hard upper bounds.
**Prevention:** Always validate `isinstance(val, int) and not isinstance(val, bool)` and check upper bounds before performing list allocation/iteration loops based on user inputs.
