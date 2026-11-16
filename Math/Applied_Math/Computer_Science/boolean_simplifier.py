"""Boolean expression minimizer using the Quine-McCluskey algorithm."""
# pylint: disable=too-many-locals
from typing import Dict, List, Optional, Sequence, Set, Tuple


def _validate_qm_inputs(
    num_vars: int,
    minterms: Sequence[int],
    dont_cares: Optional[Sequence[int]],
) -> Tuple[Set[int], Set[int]]:
    """Validate inputs for Quine-McCluskey minimization."""
    if isinstance(num_vars, bool) or not isinstance(num_vars, int):
        raise TypeError("num_vars must be an integer.")
    if num_vars < 1 or num_vars > 8:
        raise ValueError("num_vars must be between 1 and 8.")

    max_term = (1 << num_vars) - 1
    if not isinstance(minterms, (list, tuple, set)):
        raise TypeError("minterms must be a list, tuple, or set of ints.")
    m_set: Set[int] = set()
    for m in minterms:
        if isinstance(m, bool) or not isinstance(m, int):
            raise TypeError("Each minterm must be an integer.")
        if m < 0 or m > max_term:
            raise ValueError(f"Minterm {m} out of range [0, {max_term}].")
        m_set.add(m)

    dc_set: Set[int] = set()
    if dont_cares is not None:
        if not isinstance(dont_cares, (list, tuple, set)):
            raise TypeError("dont_cares must be a list, tuple, or set.")
        for d in dont_cares:
            if isinstance(d, bool) or not isinstance(d, int):
                raise TypeError("Each don't-care must be an integer.")
            if d < 0 or d > max_term:
                raise ValueError(
                    f"Don't-care {d} out of range [0, {max_term}]."
                )
            dc_set.add(d)

    if m_set & dc_set:
        raise ValueError("minterms and dont_cares must be disjoint.")
    return m_set, dc_set


def _combine_terms(a: str, b: str) -> Optional[str]:
    """Combine two binary implicant strings if they differ in exactly 1 bit."""
    diff_idx = -1
    for i, (ca, cb) in enumerate(zip(a, b)):
        if ca != cb:
            if diff_idx != -1:
                return None
            diff_idx = i
    if diff_idx == -1:
        return None
    return a[:diff_idx] + "-" + a[diff_idx + 1 :]


def _covers(implicant: str, minterm_bin: str) -> bool:
    """Return True if implicant pattern covers the given binary minterm."""
    return all(ic in ("-", mc) for ic, mc in zip(implicant, minterm_bin))


def prime_implicants(
    num_vars: int,
    minterms: Sequence[int],
    dont_cares: Optional[Sequence[int]] = None,
) -> List[str]:
    """
    Compute all prime implicants via the Quine-McCluskey method.

    Parameters:
    num_vars (int): Number of boolean variables (1 to 8).
    minterms (Sequence[int]): Minterm indices where function is 1.
    dont_cares (Optional[Sequence[int]]): Optional don't-care indices.

    Returns:
    List[str]: Sorted list of prime implicants in '0'/'1'/'-' notation.
    """
    m_set, dc_set = _validate_qm_inputs(num_vars, minterms, dont_cares)
    all_terms = sorted(m_set | dc_set)
    if not all_terms:
        return []

    current: Set[str] = {format(t, f"0{num_vars}b") for t in all_terms}
    primes: Set[str] = set()

    while current:
        groups: Dict[int, List[str]] = {}
        for term in current:
            groups.setdefault(term.count("1"), []).append(term)

        next_level: Set[str] = set()
        used: Set[str] = set()
        sorted_keys = sorted(groups.keys())
        for k in sorted_keys:
            if k + 1 not in groups:
                continue
            for t1 in groups[k]:
                for t2 in groups[k + 1]:
                    combined = _combine_terms(t1, t2)
                    if combined is not None:
                        next_level.add(combined)
                        used.add(t1)
                        used.add(t2)

        primes.update(current - used)
        current = next_level

    return sorted(primes)


def _implicant_to_expr(implicant: str, var_names: Sequence[str]) -> str:
    """Convert a '0'/'1'/'-' implicant string into a product term."""
    parts: List[str] = []
    for ch, var in zip(implicant, var_names):
        if ch == "1":
            parts.append(var)
        elif ch == "0":
            parts.append(f"{var}'")
    return "".join(parts) if parts else "1"


def simplify_boolean_sop(
    num_vars: int,
    minterms: Sequence[int],
    dont_cares: Optional[Sequence[int]] = None,
    var_names: Optional[Sequence[str]] = None,
) -> str:
    """
    Minimize a boolean Sum-of-Products expression using Quine-McCluskey.

    Parameters:
    num_vars (int): Number of boolean variables (1 to 8).
    minterms (Sequence[int]): Minterm indices where function is 1.
    dont_cares (Optional[Sequence[int]]): Optional don't-care indices.
    var_names (Optional[Sequence[str]]): Custom variable names (default A..H).

    Returns:
    str: Minimized Sum-of-Products expression (e.g., "A'B + BC", "0", "1").
    """
    m_set, dc_set = _validate_qm_inputs(num_vars, minterms, dont_cares)
    if var_names is None:
        names = [chr(ord("A") + i) for i in range(num_vars)]
    else:
        if len(var_names) != num_vars:
            raise ValueError("var_names length must match num_vars.")
        names = list(var_names)

    if not m_set:
        return "0"

    primes = prime_implicants(num_vars, sorted(m_set), sorted(dc_set))
    m_bins = {m: format(m, f"0{num_vars}b") for m in sorted(m_set)}

    # Build coverage map: minterm -> covering prime implicants
    coverage: Dict[int, List[str]] = {
        m: [p for p in primes if _covers(p, b)] for m, b in m_bins.items()
    }

    selected: List[str] = []
    uncovered: Set[int] = set(m_set)

    # 1. Select essential prime implicants
    for m in sorted(m_set):
        if m in uncovered and len(coverage[m]) == 1:
            epi = coverage[m][0]
            if epi not in selected:
                selected.append(epi)
            uncovered -= {u for u in m_set if _covers(epi, m_bins[u])}

    # 2. Greedy cover for any remaining minterms
    while uncovered:
        best_p = max(
            primes,
            key=lambda p: sum(
                1 for u in uncovered if _covers(p, m_bins[u])
            ),
        )
        selected.append(best_p)
        uncovered -= {u for u in list(uncovered) if _covers(best_p, m_bins[u])}

    terms = [_implicant_to_expr(p, names) for p in selected]
    if "1" in terms:
        return "1"
    return " + ".join(terms)
