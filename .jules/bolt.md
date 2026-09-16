# Bolt Performance Journal

## 2025-05-18 - Slice-based Pascal's Triangle Symmetry Construction
**Learning:** In CPython, computing only the first half of a symmetric list via list comprehension and concatenating reversed slices (`half + half[::-1]` or `half + half[-2::-1]`) is significantly faster than executing explicit Python element assignment loops (`row[j] = val; row[i - j] = val`).
**Action:** Use list comprehensions and C-level slice operations when building symmetric sequences/matrices instead of manual index assignment loops.
