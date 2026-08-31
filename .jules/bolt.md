## 2025-02-18 - Combinatorial range multiplication optimization
**Learning:** Calculating permutations using full factorials (`n! / (n - r)!`) causes $O(n)$ large integer multiplications and division overhead. Computing range product over `[n - r + 1, n]` using `_product_tree` reduces complexity to $O(r)$ balanced tree multiplications, giving ~3x-12x performance improvements.
**Action:** When computing partial factorial or permutation products, always use `_product_tree(start, end)` from `Math.utils.math_utils` instead of full factorial division.
