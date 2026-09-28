## 2026-09-28 - Divide-and-Conquer Tree Multiplication Base Case Threshold

**Learning:** In `_product_tree` (`Math/utils/math_utils.py`), recursing all the way down to base case ranges of length 1 or 2 incurs significant Python function call and stack allocation overhead. Increasing the base case threshold to length <= 16 using a simple iterative loop eliminates recursive call overhead while maintaining balanced divide-and-conquer tree products for larger ranges, achieving a ~17-20% speedup on `factorial`, `nCr`, and `n_permute_r`.

**Action:** When implementing divide-and-conquer recursive algorithms, always use a small iterative base case threshold (e.g. 16 to 32 elements) to bypass recursion overhead for small sub-problems.
