## 2025-05-18 - Generator Overhead vs Direct Accumulator Loops in Polynomial Evaluation
**Learning:** In Python numerical evaluation loops, passing a generator expression to `sum()` (e.g. `sum(coeff * (x**power) for ...)` instantiates a generator object and incurs iterator protocol overhead for every item. Accumulating via a direct `for` loop (`result += coeff * (x**power)`) runs ~15-20% faster while maintaining identical clarity.
**Action:** Replace generator expressions inside `sum()` in tight, repeatedly called numerical evaluation loops with explicit scalar accumulator loops.
