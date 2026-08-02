# Trigonometric integration formulas
import os
import sys
# Add Math to path to fix imports inside Math
math_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)
from Geometry.Trigonometry.Trig_Functions.sine import sine
from Geometry.Trigonometry.Trig_Functions.cosine import cosine
from typing import Union


def integrate_sin(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Calculate the definite integral of sin(x) from a to b.

    Parameters:
    a (Union[int, float]): The lower bound of integration.
    b (Union[int, float]): The upper bound of integration.

    Returns:
    float: The value of the integral.
    """
    # ∫sin(x)dx = -cos(x) + C
    return -cosine(b) + cosine(a)


def integrate_cos(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Calculate the definite integral of cos(x) from a to b.

    Parameters:
    a (Union[int, float]): The lower bound of integration.
    b (Union[int, float]): The upper bound of integration.

    Returns:
    float: The value of the integral.
    """
    # ∫cos(x)dx = sin(x) + C
    return sine(b) - sine(a)
