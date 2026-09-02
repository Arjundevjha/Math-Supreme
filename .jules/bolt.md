## 2025-03-09 - Caching Factorial Results

**Learning:** `factorial` calculation can be called repeatedly with identical inputs across combinatorics, Taylor series, and probability calculations.

**Action:** Wrap `factorial` in `Math/utils/math_utils.py` with `@functools.lru_cache` to instantly return cached values for repeated inputs.
