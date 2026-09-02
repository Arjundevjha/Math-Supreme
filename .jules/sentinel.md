## 2025-05-10 - Unbounded Input in Factorial Functions

**Vulnerability:** Unbounded input `n` in `factorial` and `factorial_decimal` functions causing potential CPU and memory exhaustion (Denial of Service).
**Learning:** Functions accepting parameters used as iteration counts or arbitrary-precision arithmetic bounds must validate parameter types (disallowing booleans and non-integers) and enforce reasonable upper bounds (e.g. `n <= 10000`).
**Prevention:** Always validate integer types with `isinstance(n, int) and not isinstance(n, bool)` and check upper/lower boundaries before executing computational loops.
