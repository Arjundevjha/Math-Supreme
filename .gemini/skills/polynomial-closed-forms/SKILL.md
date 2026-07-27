---
name: polynomial-closed-forms
description: Best practices for implementing closed-form algebraic polynomial solvers (quadratic, cubic, quartic) using Landesman's formula and complex root branch selection.
---

# Polynomial Closed-Form Solvers Skill

Best practices for closed-form polynomial solvers (quadratic, cubic, quartic):

1. **Landesman's Quartic Formulation**:
   - Extract invariant terms $p_1 = c^2 - 3bd + 12ae$ and $p_2 = 2c^3 - 9bcd - 72ace + 27ad^2 + 27b^2e$.
   - Calculate core cube root $U = \sqrt[3]{p_2 + \sqrt{p_2^2 - 4p_1^3}}$.
   - Form resolvent radical $R$, polynomial cross-term $V$, and base expression $Q$.
   - Roots: $x = -\frac{b}{4a} \pm \frac{1}{2}R \pm \frac{1}{2}\sqrt{Q \mp V}$.

2. **Branch Cut Resolution**:
   - Closed-form radicals involving $\sqrt[3]{z}$ in floating point complex arithmetic can land on degenerate branches where $R = 0$.
   - Evaluate all 3 cube-root branches $U \cdot \omega^k$ where $\omega = e^{i 2\pi / 3} = -\frac{1}{2} + i \frac{\sqrt{3}}{2}$ for $k \in \{0, 1, 2\}$.
   - Select the branch $k$ minimizing residual error $\sum_{i} |P(x_i)|$.
