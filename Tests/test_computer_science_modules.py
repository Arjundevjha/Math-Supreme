import pytest

from Math.Applied_Math.Computer_Science.binary_logic import (
    full_adder,
    half_adder,
    logic_and,
    logic_iff,
    logic_implies,
    logic_nand,
    logic_nor,
    logic_not,
    logic_or,
    logic_xnor,
    logic_xor,
)
from Math.Applied_Math.Computer_Science.boolean_simplifier import (
    prime_implicants,
    simplify_boolean_sop,
)
from Math.Applied_Math.Computer_Science.fast_fourier_transform_fft import (
    fft,
    ifft,
)
from Math.Applied_Math.Computer_Science.floating_point_representation import (
    float_to_ieee754,
    ieee754_to_float,
)
from Math.Applied_Math.Computer_Science.huffman_coding import (
    huffman_codes,
    huffman_decode,
    huffman_encode,
)
from Math.Applied_Math.Computer_Science.truth_table_generator import (
    format_truth_table,
    generate_truth_table,
)


class TestBinaryLogic:
    def test_gates(self):
        assert logic_and(1, 1) is True
        assert logic_and(1, 0) is False
        assert logic_or(0, 1) is True
        assert logic_not(0) is True
        assert logic_xor(1, 0) is True
        assert logic_xor(1, 1) is False
        assert logic_nand(1, 1) is False
        assert logic_nor(0, 0) is True
        assert logic_xnor(1, 1) is True
        assert logic_implies(1, 0) is False
        assert logic_implies(0, 0) is True
        assert logic_iff(0, 0) is True

    def test_adders(self):
        assert half_adder(1, 1) == (0, 1)
        assert half_adder(1, 0) == (1, 0)
        assert full_adder(1, 1, 1) == (1, 1)
        assert full_adder(1, 0, 1) == (0, 1)

    def test_validation(self):
        with pytest.raises(TypeError):
            logic_and(2, 1)
        with pytest.raises(TypeError):
            logic_not("1")


class TestTruthTableGenerator:
    def test_generate_and_format(self):
        rows = generate_truth_table(["A", "B"], lambda a, b: a and b)
        assert len(rows) == 4
        assert rows[0] == {"A": False, "B": False, "result": False}
        assert rows[3] == {"A": True, "B": True, "result": True}

        table = format_truth_table(["A", "B"], lambda a, b: a or b)
        assert "A | B | result" in table
        assert "1 | 1 | 1" in table

    def test_validation(self):
        with pytest.raises(ValueError):
            generate_truth_table([], lambda: True)
        with pytest.raises(ValueError):
            generate_truth_table(["A", "A"], lambda a, b: a)
        with pytest.raises(TypeError):
            generate_truth_table(["A"], "not_callable")


class TestBooleanSimplifier:
    def test_quine_mccluskey_simplification(self):
        # f(A, B) = sum(1, 2, 3) = A + B
        assert prime_implicants(2, [1, 2, 3]) == ["-1", "1-"]
        expr = simplify_boolean_sop(2, [1, 2, 3])
        assert "A" in expr and "B" in expr

    def test_dont_cares_and_constants(self):
        # f(A, B) = sum(1, 3) with dc(0, 2) -> 1
        assert simplify_boolean_sop(2, [1, 3], dont_cares=[0, 2]) == "1"
        assert simplify_boolean_sop(2, []) == "0"
        # f(A, B, C) = sum(4, 5, 6, 7) = A
        assert simplify_boolean_sop(3, [4, 5, 6, 7]) == "A"

    def test_validation(self):
        with pytest.raises(ValueError):
            simplify_boolean_sop(2, [1], dont_cares=[1])
        with pytest.raises(ValueError):
            simplify_boolean_sop(2, [4])
        with pytest.raises(ValueError):
            simplify_boolean_sop(9, [0])


class TestFloatingPointRepresentation:
    def test_32bit_and_64bit_roundtrip(self):
        enc32 = float_to_ieee754(-3.5, precision=32)
        assert enc32["sign"] == 1
        assert len(enc32["binary"]) == 32
        assert enc32["hex"] == "0xC0600000"
        assert ieee754_to_float(enc32["binary"]) == pytest.approx(-3.5)

        enc64 = float_to_ieee754(0.125, precision=64)
        assert len(enc64["binary"]) == 64
        assert ieee754_to_float(enc64["binary"]) == pytest.approx(0.125)

    def test_validation(self):
        with pytest.raises(TypeError):
            float_to_ieee754(True)
        with pytest.raises(ValueError):
            float_to_ieee754(1.0, precision=16)
        with pytest.raises(ValueError):
            ieee754_to_float("10101")


class TestHuffmanCoding:
    def test_encode_decode_roundtrip(self):
        text = "abracadabra"
        encoded, codes = huffman_encode(text)
        assert huffman_decode(encoded, codes) == text
        # Verify prefix-free property
        code_list = list(codes.values())
        for i, c1 in enumerate(code_list):
            for j, c2 in enumerate(code_list):
                if i != j:
                    assert not c2.startswith(c1)

    def test_single_symbol_and_empty(self):
        assert huffman_codes("") == {}
        enc, codes = huffman_encode("aaaa")
        assert codes == {"a": "0"}
        assert enc == "0000"
        assert huffman_decode(enc, codes) == "aaaa"

    def test_validation(self):
        with pytest.raises(ValueError):
            huffman_codes({"a": 0})
        with pytest.raises(ValueError):
            huffman_decode("012", {"a": "0"})


class TestFFT:
    def test_fft_and_ifft_roundtrip(self):
        signal = [1.0, 2.0, 3.0, 4.0]
        spec = fft(signal)
        assert spec[0].real == pytest.approx(10.0, abs=1e-6)
        reconstructed = ifft(spec)
        for orig, rec in zip(signal, reconstructed):
            assert rec.real == pytest.approx(orig, abs=1e-6)
            assert rec.imag == pytest.approx(0.0, abs=1e-6)

    def test_fft_zero_padding(self):
        spec = fft([1, 2, 3], pad=True)
        assert len(spec) == 4
        assert spec[0].real == pytest.approx(6.0, abs=1e-6)

    def test_validation(self):
        with pytest.raises(ValueError):
            fft([1, 2, 3])
        with pytest.raises(ValueError):
            ifft([1, 2, 3])
        with pytest.raises(TypeError):
            fft([1, True])
