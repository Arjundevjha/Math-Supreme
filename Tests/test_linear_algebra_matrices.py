import pytest

from Math.Linear_Algebra.Matrices.determinant import determinant
from Math.Linear_Algebra.Matrices.lu_decomposition import lu_decomposition
from Math.Linear_Algebra.Matrices.matrix_addition import (
    matrix_add,
    matrix_subtract,
)
from Math.Linear_Algebra.Matrices.matrix_inverse import matrix_inverse
from Math.Linear_Algebra.Matrices.matrix_multiplication import (
    matrix_multiply,
    scalar_multiply,
)
from Math.Linear_Algebra.Matrices.matrix_transpose import matrix_transpose
from Math.Linear_Algebra.Matrices.qr_decomposition import qr_decomposition
from Math.Linear_Algebra.Matrices.rank_nullity import (
    matrix_nullity,
    matrix_rank,
    rank_nullity,
)
from Math.Linear_Algebra.Matrices.singular_value_decomposition import svd


def _assert_matrix_close(a, b, tol=1e-6):
    assert len(a) == len(b)
    assert len(a[0]) == len(b[0])
    for row_a, row_b in zip(a, b):
        for va, vb in zip(row_a, row_b):
            assert va == pytest.approx(vb, abs=tol)


class TestMatrices:
    def test_add_subtract_scalar_transpose(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        assert matrix_add(a, b) == [[6.0, 8.0], [10.0, 12.0]]
        assert matrix_subtract(b, a) == [[4.0, 4.0], [4.0, 4.0]]
        assert scalar_multiply(a, 2) == [[2.0, 4.0], [6.0, 8.0]]
        assert matrix_transpose([[1, 2, 3], [4, 5, 6]]) == [
            [1.0, 4.0],
            [2.0, 5.0],
            [3.0, 6.0],
        ]

    def test_multiply_determinant_inverse(self):
        a = [[4, 7], [2, 6]]
        assert determinant(a) == pytest.approx(10.0)
        assert determinant([[1, 2], [2, 4]]) == pytest.approx(0.0)
        inv_a = matrix_inverse(a)
        _assert_matrix_close(
            matrix_multiply(a, inv_a), [[1.0, 0.0], [0.0, 1.0]]
        )
        with pytest.raises(ValueError):
            matrix_inverse([[1, 2], [2, 4]])

    def test_rank_nullity(self):
        m = [[1, 2, 3], [2, 4, 6], [1, 1, 1]]
        assert matrix_rank(m) == 2
        assert matrix_nullity(m) == 1
        assert rank_nullity(m) == (2, 1)

    def test_lu_decomposition(self):
        a = [[2, 1, 1], [4, -6, 0], [-2, 7, 2]]
        p, l_mat, u_mat = lu_decomposition(a)
        _assert_matrix_close(
            matrix_multiply(p, a), matrix_multiply(l_mat, u_mat)
        )

    def test_qr_decomposition(self):
        a = [[1, 1], [1, 0], [0, 1]]
        q, r = qr_decomposition(a)
        _assert_matrix_close(matrix_multiply(q, r), a)
        qtq = matrix_multiply(matrix_transpose(q), q)
        _assert_matrix_close(qtq, [[1.0, 0.0], [0.0, 1.0]])

    def test_svd(self):
        a = [[3, 1], [1, 3]]
        u, sigmas, v_t = svd(a)
        assert sigmas[0] == pytest.approx(4.0, abs=1e-6)
        assert sigmas[1] == pytest.approx(2.0, abs=1e-6)
        s_diag = [[sigmas[0], 0.0], [0.0, sigmas[1]]]
        reconstructed = matrix_multiply(matrix_multiply(u, s_diag), v_t)
        _assert_matrix_close(reconstructed, a)

        u1, s1, vt1 = svd([[3.0], [4.0]])
        assert s1 == [pytest.approx(5.0)]
        _assert_matrix_close(
            matrix_multiply(matrix_multiply(u1, [[s1[0]]]), vt1),
            [[3.0], [4.0]],
        )

    def test_matrix_validation(self):
        with pytest.raises(TypeError):
            matrix_add("bad", [[1]])
        with pytest.raises(ValueError):
            matrix_add([[1, 2]], [[1]])
        with pytest.raises(ValueError):
            matrix_multiply([[1, 2]], [[1, 2]])
        with pytest.raises(ValueError):
            determinant([[1, 2, 3], [4, 5, 6]])
