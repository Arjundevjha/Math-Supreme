"""IEEE 754 single (32-bit) and double (64-bit) floating-point encoding."""
import struct
from typing import Dict, Union


def float_to_ieee754(
    value: Union[int, float], precision: int = 32
) -> Dict[str, Union[int, str]]:
    """
    Convert a numeric value to its IEEE 754 binary and hex representation.

    Parameters:
    value (Union[int, float]): Number to encode.
    precision (int): Bit width, either 32 (single) or 64 (double).

    Returns:
    Dict[str, Union[int, str]]: Dictionary with 'sign', 'exponent_bits',
        'mantissa_bits', 'binary', and 'hex'.
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be a numeric int or float.")
    if isinstance(precision, bool) or precision not in (32, 64):
        raise ValueError("precision must be 32 or 64.")

    fmt = ">f" if precision == 32 else ">d"
    exp_len = 8 if precision == 32 else 11
    packed = struct.pack(fmt, float(value))
    bits = "".join(f"{byte:08b}" for byte in packed)

    return {
        "sign": int(bits[0]),
        "exponent_bits": bits[1 : 1 + exp_len],
        "mantissa_bits": bits[1 + exp_len :],
        "binary": bits,
        "hex": "0x" + packed.hex().upper(),
    }


def ieee754_to_float(binary_str: str) -> float:
    """
    Decode a 32-bit or 64-bit IEEE 754 binary string back into a float.

    Parameters:
    binary_str (str): 32-bit or 64-bit string of '0' and '1' characters.

    Returns:
    float: Decoded floating-point value.
    """
    if not isinstance(binary_str, str):
        raise TypeError("binary_str must be a string.")
    cleaned = binary_str.replace(" ", "")
    if len(cleaned) not in (32, 64) or any(
        ch not in ("0", "1") for ch in cleaned
    ):
        raise ValueError(
            "binary_str must be a 32-bit or 64-bit string of '0' and '1'."
        )

    raw_bytes = bytes(
        int(cleaned[i : i + 8], 2) for i in range(0, len(cleaned), 8)
    )
    fmt = ">f" if len(cleaned) == 32 else ">d"
    return float(struct.unpack(fmt, raw_bytes)[0])
