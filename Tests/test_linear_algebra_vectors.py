import pytest

from Math.Linear_Algebra.Vectors.angle_between_vectors import (
    angle_between_vectors,
)
from Math.Linear_Algebra.Vectors.cross_product import cross_product
from Math.Linear_Algebra.Vectors.dot_product import dot_product
from Math.Linear_Algebra.Vectors.gram_schmidt_orthogonalization import (
    gram_schmidt,
)
from Math.Linear_Algebra.Vectors.magnitude import vector_magnitude
from Math.Linear_Algebra.Vectors.vector_projection import vector_projection
from Math.utils.math_utils import PI


class TestVectors:
    def test_magnitude(self):
        assert vector_magnitude([3, 4]) == pytest.approx(5.0)
        assert vector_magnitude([0, 0, 0]) == 0.0
        assert vector_magnitude([1, 2, 2]) == pytest.approx(3.0)

    def test_dot_product(self):
        assert dot_product([1, 2, 3], [4, -5, 6]) == pytest.approx(12.0)
        with pytest.raises(ValueError):
            dot_product([1, 2], [1, 2, 3])

    def test_cross_product(self):
        assert cross_product([1, 0, 0], [0, 1, 0]) == [0.0, 0.0, 1.0]
        assert cross_product([2, 3, 4], [5, 6, 7]) == [-3.0, 6.0, -3.0]
        with pytest.raises(ValueError):
            cross_product([1, 2], [3, 4])

    def test_vector_projection(self):
        proj = vector_projection([3, 4], [1, 0])
        assert proj == [3.0, 0.0]
        with pytest.raises(ValueError):
            vector_projection([1, 2], [0, 0])

    def test_angle_between_vectors(self):
        assert angle_between_vectors([1, 0], [0, 1]) == pytest.approx(
            PI / 2.0, rel=1e-5
        )
        assert angle_between_vectors(
            [1, 0], [0, 1], degrees=True
        ) == pytest.approx(90.0, rel=1e-5)
        assert angle_between_vectors([2, 0], [5, 0]) == pytest.approx(
            0.0, abs=1e-6
        )
        with pytest.raises(ValueError):
            angle_between_vectors([0, 0], [1, 0])

    def test_gram_schmidt(self):
        ortho = gram_schmidt([[1, 1], [1, 0]], normalize=True)
        assert len(ortho) == 2
        assert dot_product(ortho[0], ortho[1]) == pytest.approx(0.0, abs=1e-9)
        assert vector_magnitude(ortho[0]) == pytest.approx(1.0, rel=1e-9)
        assert vector_magnitude(ortho[1]) == pytest.approx(1.0, rel=1e-9)

        with pytest.raises(ValueError):
            gram_schmidt([[1, 2], [2, 4]])

    def test_vector_validation(self):
        with pytest.raises(TypeError):
            vector_magnitude("123")
        with pytest.raises(TypeError):
            vector_magnitude([True, 1])
        with pytest.raises(ValueError):
            vector_magnitude([])
        with pytest.raises(ValueError):
            vector_magnitude([float("nan")])
