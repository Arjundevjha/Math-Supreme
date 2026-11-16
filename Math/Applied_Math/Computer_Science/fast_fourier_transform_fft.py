"""Cooley-Tukey Radix-2 Fast Fourier Transform (FFT) and Inverse FFT."""
from typing import List, Sequence, Union

from Math.Geometry.Trigonometry.Trig_Functions.cosine import cosine
from Math.Geometry.Trigonometry.Trig_Functions.sine import sine
from Math.utils.math_utils import PI

SignalValue = Union[int, float, complex]


def _validate_signal(signal: Sequence[SignalValue]) -> List[complex]:
    """Validate input signal sequence and convert elements to complex."""
    if not isinstance(signal, (list, tuple)):
        raise TypeError("signal must be a list or tuple.")
    if len(signal) > 65536:
        raise ValueError("signal length exceeds maximum limit of 65536.")

    result: List[complex] = []
    for val in signal:
        if isinstance(val, bool) or not isinstance(val, (int, float, complex)):
            raise TypeError(
                "All signal elements must be int, float, or complex."
            )
        c_val = complex(val)
        if not (
            -float("inf") < c_val.real < float("inf")
            and -float("inf") < c_val.imag < float("inf")
        ):
            raise ValueError("Signal elements must be finite numbers.")
        result.append(c_val)
    return result


def _is_power_of_two(n: int) -> bool:
    """Return True if n is a positive power of two."""
    return n > 0 and (n & (n - 1)) == 0


def _fft_recursive(x: List[complex]) -> List[complex]:
    """Compute Radix-2 Cooley-Tukey FFT recursively."""
    n = len(x)
    if n <= 1:
        return x

    even = _fft_recursive(x[0::2])
    odd = _fft_recursive(x[1::2])

    combined = [0j] * n
    half = n // 2
    for k in range(half):
        angle = -2.0 * PI * k / n
        twiddle = complex(cosine(angle), sine(angle)) * odd[k]
        combined[k] = even[k] + twiddle
        combined[k + half] = even[k] - twiddle
    return combined


def fft(signal: Sequence[SignalValue], pad: bool = False) -> List[complex]:
    """
    Compute the Fast Fourier Transform (FFT) of a sequence.

    Parameters:
    signal (Sequence[SignalValue]): Input sequence of numbers.
    pad (bool): If True, zero-pad to the next power of two.

    Returns:
    List[complex]: Complex frequency-domain spectrum.
    """
    if not isinstance(pad, bool):
        raise TypeError("pad must be a boolean.")
    data = _validate_signal(signal)
    n = len(data)
    if n == 0:
        return []
    if not _is_power_of_two(n):
        if not pad:
            raise ValueError("signal length must be a power of 2.")
        next_pow2 = 1
        while next_pow2 < n:
            next_pow2 <<= 1
        data.extend([0j] * (next_pow2 - n))
    return _fft_recursive(data)


def ifft(spectrum: Sequence[SignalValue]) -> List[complex]:
    """
    Compute the Inverse Fast Fourier Transform (IFFT) of a spectrum.

    Parameters:
    spectrum (Sequence[SignalValue]): Frequency-domain sequence (power-of-2).

    Returns:
    List[complex]: Reconstructed time-domain complex sequence.
    """
    data = _validate_signal(spectrum)
    n = len(data)
    if n == 0:
        return []
    if not _is_power_of_two(n):
        raise ValueError("spectrum length must be a power of 2.")

    conjugated = [val.conjugate() for val in data]
    transformed = _fft_recursive(conjugated)
    return [val.conjugate() / n for val in transformed]
