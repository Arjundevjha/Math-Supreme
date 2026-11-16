"""Huffman coding compression and decompression."""
import heapq
from typing import Dict, List, Optional, Tuple, Union


class _HuffmanNode:  # pylint: disable=too-few-public-methods
    """Internal node for Huffman binary tree construction."""

    def __init__(
        self,
        freq: int,
        symbol: Optional[str] = None,
        left: Optional["_HuffmanNode"] = None,
        right: Optional["_HuffmanNode"] = None,
    ) -> None:
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other: "_HuffmanNode") -> bool:
        return self.freq < other.freq


def _assign_codes(
    node: Optional[_HuffmanNode], prefix: str, codes: Dict[str, str]
) -> None:
    """Traverse Huffman tree to assign prefix-free binary codes."""
    if node is None:
        return
    if node.symbol is not None:
        codes[node.symbol] = prefix or "0"
        return
    _assign_codes(node.left, prefix + "0", codes)
    _assign_codes(node.right, prefix + "1", codes)


def huffman_codes(
    data: Union[str, Dict[str, int]],
) -> Dict[str, str]:
    """
    Generate prefix-free Huffman codes from a string or frequency dictionary.

    Parameters:
    data (Union[str, Dict[str, int]]): Input text or {symbol: frequency}.

    Returns:
    Dict[str, str]: Mapping from each symbol to its Huffman bitstring.
    """
    if isinstance(data, str):
        if not data:
            return {}
        freqs: Dict[str, int] = {}
        for ch in data:
            freqs[ch] = freqs.get(ch, 0) + 1
    elif isinstance(data, dict):
        if not data:
            return {}
        freqs = {}
        for sym, freq in data.items():
            if not isinstance(sym, str) or not sym:
                raise TypeError("All symbols must be non-empty strings.")
            if isinstance(freq, bool) or not isinstance(freq, int) or freq <= 0:
                raise ValueError("All frequencies must be positive integers.")
            freqs[sym] = freq
    else:
        raise TypeError("data must be a string or a frequency dictionary.")

    heap: List[_HuffmanNode] = [
        _HuffmanNode(freq, symbol=sym) for sym, freq in freqs.items()
    ]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = _HuffmanNode(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    codes: Dict[str, str] = {}
    _assign_codes(heap[0], "", codes)
    return codes


def huffman_encode(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Encode a string using Huffman coding.

    Parameters:
    text (str): Input string to compress.

    Returns:
    Tuple[str, Dict[str, str]]: (encoded_bitstring, code_table).
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    if not text:
        return "", {}
    codes = huffman_codes(text)
    encoded = "".join(codes[ch] for ch in text)
    return encoded, codes


def huffman_decode(encoded_bits: str, codes: Dict[str, str]) -> str:
    """
    Decode a Huffman-encoded bitstring using the given code table.

    Parameters:
    encoded_bits (str): Bitstring of '0' and '1' characters.
    codes (Dict[str, str]): Symbol-to-bitstring mapping.

    Returns:
    str: Decoded original string.
    """
    if not isinstance(encoded_bits, str):
        raise TypeError("encoded_bits must be a string.")
    if not isinstance(codes, dict):
        raise TypeError("codes must be a dictionary.")
    if not encoded_bits:
        return ""
    if not codes:
        raise ValueError("codes must not be empty for non-empty bitstring.")
    if any(ch not in ("0", "1") for ch in encoded_bits):
        raise ValueError("encoded_bits must contain only '0' and '1'.")

    reverse_codes = {bitstr: sym for sym, bitstr in codes.items()}
    decoded: List[str] = []
    buffer = ""
    for bit in encoded_bits:
        buffer += bit
        if buffer in reverse_codes:
            decoded.append(reverse_codes[buffer])
            buffer = ""
    if buffer:
        raise ValueError("Invalid or truncated Huffman bitstring.")
    return "".join(decoded)
