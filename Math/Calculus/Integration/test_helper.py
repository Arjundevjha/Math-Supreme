from Math.Geometry.Trigonometry.Trig_Functions.sine import sine
from Math.Geometry.Trigonometry.Trig_Functions.cosine import cosine
import math

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
