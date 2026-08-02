# Factorial calculation
from Math.math_utils import factorial


# Alias for backward compatibility if anyone imports factorial from this specific file
# though they should use the shared utility.
# We will just expose the imported function.
__all__ = ['factorial']
