## 2026-03-31 - String Precomputation in Trinomial Expansion Loops
**Learning:** In `expand_trinomial`, computing `a^{i}` string formatting inside the inner loop over `j` causes redundant string formatting and memory allocation across `(n+1)(n+2)/2` inner loop iterations. Precomputing `a_i = f"{a}^{i}"` outside the inner loop reduces redundant allocations and yields an ~11-13% speedup.
**Action:** When working with multi-variable expansion algorithms in nested loops, precompute term string representations at the highest outer loop scope where they remain invariant.
