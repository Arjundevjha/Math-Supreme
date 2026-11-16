"""Binary logic gates and basic binary arithmetic adders."""
from typing import Tuple, Union

BitInput = Union[bool, int]


def _to_bool(name: str, value: BitInput) -> bool:
    """Validate and convert a bool or 0/1 integer to bool."""
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in (0, 1):
        return bool(value)
    raise TypeError(f"{name} must be a bool or integer 0/1.")


def logic_and(a: BitInput, b: BitInput) -> bool:
    """Return logical AND of two binary inputs."""
    return _to_bool("a", a) and _to_bool("b", b)


def logic_or(a: BitInput, b: BitInput) -> bool:
    """Return logical OR of two binary inputs."""
    return _to_bool("a", a) or _to_bool("b", b)


def logic_not(a: BitInput) -> bool:
    """Return logical NOT of a binary input."""
    return not _to_bool("a", a)


def logic_xor(a: BitInput, b: BitInput) -> bool:
    """Return logical XOR of two binary inputs."""
    return _to_bool("a", a) != _to_bool("b", b)


def logic_nand(a: BitInput, b: BitInput) -> bool:
    """Return logical NAND of two binary inputs."""
    return not (_to_bool("a", a) and _to_bool("b", b))


def logic_nor(a: BitInput, b: BitInput) -> bool:
    """Return logical NOR of two binary inputs."""
    return not (_to_bool("a", a) or _to_bool("b", b))


def logic_xnor(a: BitInput, b: BitInput) -> bool:
    """Return logical XNOR of two binary inputs."""
    return _to_bool("a", a) == _to_bool("b", b)


def logic_implies(a: BitInput, b: BitInput) -> bool:
    """Return logical implication (a -> b)."""
    return (not _to_bool("a", a)) or _to_bool("b", b)


def logic_iff(a: BitInput, b: BitInput) -> bool:
    """Return logical biconditional (a <-> b)."""
    return _to_bool("a", a) == _to_bool("b", b)


def half_adder(a: BitInput, b: BitInput) -> Tuple[int, int]:
    """
    Compute sum and carry of a binary half adder.

    Parameters:
    a (BitInput): First binary bit (0/1 or bool).
    b (BitInput): Second binary bit (0/1 or bool).

    Returns:
    Tuple[int, int]: (sum_bit, carry_bit) each as 0 or 1.
    """
    bit_a = _to_bool("a", a)
    bit_b = _to_bool("b", b)
    sum_bit = int(bit_a != bit_b)
    carry_bit = int(bit_a and bit_b)
    return sum_bit, carry_bit


def full_adder(
    a: BitInput, b: BitInput, carry_in: BitInput
) -> Tuple[int, int]:
    """
    Compute sum and carry-out of a binary full adder.

    Parameters:
    a (BitInput): First binary bit (0/1 or bool).
    b (BitInput): Second binary bit (0/1 or bool).
    carry_in (BitInput): Carry-in bit (0/1 or bool).

    Returns:
    Tuple[int, int]: (sum_bit, carry_out) each as 0 or 1.
    """
    bit_a = _to_bool("a", a)
    bit_b = _to_bool("b", b)
    bit_c = _to_bool("carry_in", carry_in)
    sum_bit = int((bit_a != bit_b) != bit_c)
    carry_out = int((bit_a and bit_b) or (bit_c and (bit_a != bit_b)))
    return sum_bit, carry_out
