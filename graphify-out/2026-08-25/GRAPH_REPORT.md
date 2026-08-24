# Graph Report - .  (2026-07-26)

## Corpus Check
- Corpus is ~31,666 words - fits in a single context window. You may not need a graph.

## Summary
- 1152 nodes · 1814 edges · 85 communities (67 shown, 18 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 23 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Newton-Raphson & Root Finding
- Binomial Theorem
- Differentiation Chain & Second Derivative Rules
- Test Algebra Testevaluatepolynomial Module
- Trigonometric Integration
- Factor Theorem Testing
- Linear Equation Solvers
- Factor Theorem Testing
- Test Calculus Testformatpolynomialchainrule Module
- Calculus Quotient Rule
- Trigonometry Cosine Rule
- Euler's Number Constants
- Remainder Theorem Algebra
- Simple Polynomial Differentiation
- Pascal's Triangle Combinatorics
- Trigonometric Tangent Functions
- Remainder Theorem Algebra
- Test Quadratic Testsolvequadratic Module
- Factorial Discrete Module
- Greatest Common Divisor (GCD)
- Calculus Chain Rule
- Least Common Multiple (LCM)
- Descriptive Statistics (Mode)
- Descriptive Statistics (Mean)
- Calculus Chain Rule
- Partition Test Discretetest Module
- Trigonometric Tangent Functions
- Binomial Theorem
- Test Slope Testcalculateslope Module
- Euclidean Area (Triangle)
- Euclidean Volume (Cone)
- Euclidean Volume (Cylinder)
- Calculus Quotient Rule
- Simple Interest Math
- Integration Format Module
- Euclidean Area (Rectangle)
- Euclidean Volume (Sphere)
- Descriptive Statistics (Median)
- Test Calculus Testcalculusdifferentiation Module
- Integrate Polynomial Module
- Trigonometric Integration
- Approximation Partition Module
- Trigonometric Tangent Functions
- Test Intersection Intersection Module
- From Points Module
- Test Midpoint Testmidpointformula Module
- Polynomial Format Module
- Euclidean Area (Circle)
- Euclidean Area (Square)
- Euclidean Area (Square)
- Euclidean Volume (Cuboid)
- Inverse Trigonometry (Arctan)
- Trigonometric Sine Functions
- Trigonometric Tangent Functions
- Compound Interest Math
- Trinomial General Module
- Euclidean Area (Triangle)
- Trigonometric Sine Functions
- Trigonometric Sine Functions
- Test Calculus Testchainruleformatpolynomial Module
- Inverse Trigonometry (Arctan)
- Inverse Trigonometry (Arctan)
- Inverse Trigonometry (Arcsin)
- Trigonometric Tangent Functions
- Test Algebra Testevaluatepolynomial Module
- Trigonometric Tangent Functions
- Geometry Area Module
- Geometry Volume Module
- Linear Equation Solvers
- Project Documentation & Guidelines
- Project Documentation & Guidelines
- Project Documentation & Guidelines
- Project Documentation & Guidelines
- Project Documentation & Guidelines
- Style Guide Module
- Style Guide Module
- Style Guide Module
- Style Guide Module
- Style Guide Module

## God Nodes (most connected - your core abstractions)
1. `evaluate_polynomial()` - 76 edges
2. `check_factor()` - 36 edges
3. `TestFormatPolynomialChainRule` - 30 edges
4. `format_polynomial()` - 25 edges
5. `TestEvaluatePolynomial` - 24 edges
6. `quotient_rule_derivative()` - 22 edges
7. `second_derivative()` - 22 edges
8. `differentiate_polynomial()` - 21 edges
9. `integrate_cos()` - 20 edges
10. `chain_rule_derivative()` - 19 edges

## Surprising Connections (you probably didn't know these)
- `No Standard Math Module Rule` --semantically_similar_to--> `Number One Principle`  [INFERRED] [semantically similar]
  AGENTS.md → Style_Guide.MD
- `linear_eqn (Example Template)` --semantically_similar_to--> `linear_eqn (Style Guide Example)`  [INFERRED] [semantically similar]
  AGENTS.md → Style_Guide.MD
- `nth_root()` --implements--> `Newton-Raphson method`  [EXTRACTED]
  Math/Numerical_Methods/Functions/nth_root/nth_root.py → handoff.md
- `nth_root()` --implements--> `Precision Modes`  [EXTRACTED]
  Math/Numerical_Methods/Functions/nth_root/nth_root.py → handoff.md
- `cubic_formula()` --implements--> `Dependency Elimination`  [EXTRACTED]
  Math/Algebra/Polynomials/cubic_formula.py → handoff.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Coding Restrictions and Dependency Policies** — agents_no_standard_math_module_usage, agents_internal_imports_first, style_guide_number_one_principle [EXTRACTED 1.00]
- **Standard Math Dependency Elimination** — math_numerical_methods_functions_nth_root_nth_root_nth_root, math_algebra_polynomials_cubic_formula_cubic_formula, math_algebra_polynomials_factor_theorem_factor_theorem, handoff_dependency_elimination [EXTRACTED 1.00]

## Communities (85 total, 18 thin omitted)

### Community 0 - "Newton-Raphson & Root Finding"
Cohesion: 0.06
Nodes (50): Dependency Elimination, Newton-Raphson method, Precision Modes, cubic_formula(), Solve cubic equations of the form ax³ + bx² + cx + d = 0 using the cubic formula, factor_theorem, quartic_formula(), Solve quartic equations of the form ax⁴ + bx³ + cx² + dx + e = 0 using the quart (+42 more)

### Community 1 - "Binomial Theorem"
Cohesion: 0.07
Nodes (36): binomial_coefficient(), expand_binomial(), Expand the binomial (a + b)^n using the binomial theorem.      Parameters:     a, Calculate the binomial coefficient C(n, r).      Parameters:     n (int): The po, nCr(), Calculate combinations (nCr) using the formula: nCr = n! / (r! * (n - r)!)., expand_trinomial(), Expand the trinomial (a + b + c)^n using the trinomial theorem.      Parameters: (+28 more)

### Community 2 - "Differentiation Chain & Second Derivative Rules"
Cohesion: 0.08
Nodes (44): format_polynomial(), Format a polynomial as a string.      Parameters:     coefficients (List[Union[i, Calculate the second derivative of a polynomial.      Parameters:     coeffs (Li, second_derivative(), test_format_polynomial_chain_rule_2_basic(), test_format_polynomial_chain_rule_2_floats(), test_format_polynomial_chain_rule_2_negative_coeffs(), test_format_polynomial_chain_rule_2_negative_powers() (+36 more)

### Community 3 - "Test Algebra Testevaluatepolynomial Module"
Cohesion: 0.05
Nodes (22): Test that zip handles mismatched list lengths by truncating to the shortest, Test with floating point values that might cause precision issues, Test with a simple quadratic polynomial: x^2 + 2x + 1 at x=2, Test polynomial at x=0, Test polynomial at x=-1, Test with fractional powers (square root), Test with float coefficients and float x, Test with empty coefficients and powers (+14 more)

### Community 4 - "Trigonometric Integration"
Cohesion: 0.07
Nodes (24): integrate_cos(), integrate_sin(), Calculate the definite integral of sin(x) from a to b.      Parameters:     a (U, Test integral of sin(x) from 0 to pi = 2, Test integral of sin(x) from 0 to 0 = 0, Test integral of sin(x) from 0 to 2pi = 0, Test integral of sin(x) from -pi to 0 = -2, Test integral of sin(x) from 0 to pi/3 = 0.5 (+16 more)

### Community 5 - "Factor Theorem Testing"
Cohesion: 0.09
Nodes (20): check_factor(), Check if (x - a) is a factor of a polynomial using the Factor Theorem.      Para, test_check_factor_empty(), test_check_factor_float(), test_check_factor_irrational(), test_check_factor_negative_powers(), test_check_factor_precision(), test_check_factor_true() (+12 more)

### Community 6 - "Linear Equation Solvers"
Cohesion: 0.11
Nodes (32): linear_eqn(), Calculate the equation of a line given two points (x1, y1) and (x2, y2)., evaluate_polynomial(), Evaluate a polynomial at a given value of x.      Parameters:     coefficients (, test_evaluate_polynomial_all_zero_coeffs(), test_evaluate_polynomial_basic(), test_evaluate_polynomial_empty(), test_evaluate_polynomial_floating_point() (+24 more)

### Community 7 - "Factor Theorem Testing"
Cohesion: 0.07
Nodes (11): Test with a simple quadratic polynomial: x^2 + 2x + 1 at x=2, Test floating-point precision evaluation., Test evaluation with very large numbers., Test polynomial at x=0, Test polynomial at x=-1, Test with fractional powers (square root), Test with float coefficients and float x, Test with empty coefficients and powers (+3 more)

### Community 8 - "Test Calculus Testformatpolynomialchainrule Module"
Cohesion: 0.07
Nodes (4): Test integral of cos(x) from pi/6 to pi/3 = (sqrt(3)/2 - 1/2), Test integral of cos(x) from 0 to pi = 0, Test integral of cos(x) over multiple periods, TestFormatPolynomialChainRule

### Community 9 - "Calculus Quotient Rule"
Cohesion: 0.08
Nodes (27): compute_polynomial_derivative_str(), format_polynomial(), quotient_rule_derivative(), Compute the derivative of a polynomial and return as string.      Parameters:, Apply the quotient rule to find the derivative of u(x) / v(x).      Parameters:, Format a polynomial as a string.      Parameters:     coefficients (List[Union[i, test_format_polynomial_basic(), test_format_polynomial_empty() (+19 more)

### Community 10 - "Trigonometry Cosine Rule"
Cohesion: 0.14
Nodes (25): arccos_series(), cosine_rule_for_angle(), cosine_rule_for_side(), cosine_taylor(), factorial(), Calculate cosine using Taylor series., Calculate square root using Newton's method., Calculate arccos using series approximation. (+17 more)

### Community 11 - "Euler's Number Constants"
Cohesion: 0.11
Nodes (16): compute_eulers_number(), factorial_decimal(), Decimal, Compute Euler's number (e) using the series expansion: e = Σ(1/n!) for n=0 to in, Calculate factorial as Decimal for high precision.      Parameters:     n (int):, Test factorial of zero is 1., Test factorial of one is 1., Test factorial for positive integers. (+8 more)

### Community 12 - "Remainder Theorem Algebra"
Cohesion: 0.12
Nodes (12): Find the remainder when a polynomial is divided by (x - a) using the Remainder T, remainder_theorem(), Test remainder theorem with large numbers, Test with mismatched lengths of coefficients and powers, Test with zero x and negative power, Test P(x) = x^2 - 3x + 2 divided by (x - 3). Remainder = P(3)., Test division by exact factor where remainder should be 0., Test dividing by (x - a) where a is negative, i.e., (x + 2) -> a = -2. (+4 more)

### Community 13 - "Simple Polynomial Differentiation"
Cohesion: 0.15
Nodes (4): differentiate_polynomial(), Differentiate a polynomial using the power rule.      Parameters:     coeffs (Li, TestDifferentiatePolynomial, TestDifferentiatePolynomial

### Community 14 - "Pascal's Triangle Combinatorics"
Cohesion: 0.13
Nodes (13): generate_pascals_triangle(), print_pascals_triangle(), Print Pascal's triangle in a formatted way.      Parameters:     triangle (List[, Generate Pascal's triangle with num_rows rows.      Parameters:     num_rows (in, Test printing a normal Pascal's triangle., Test printing an empty Pascal's triangle., Test generating a valid Pascal's triangle., TestPascalsTriangle (+5 more)

### Community 15 - "Trigonometric Tangent Functions"
Cohesion: 0.10
Nodes (21): compute_polynomial_derivative_str(), format_polynomial(), product_rule_derivative(), Compute the derivative of a polynomial and return as string.      Parameters:, Apply the product rule to find the derivative of u(x) * v(x).      Parameters:, Format a polynomial as a string.      Parameters:     coefficients (List[Union[i, test_compute_polynomial_derivative_str_constant_term(), test_compute_polynomial_derivative_str_empty() (+13 more)

### Community 16 - "Remainder Theorem Algebra"
Cohesion: 0.10
Nodes (11): Test with a simple quadratic polynomial: P(x) = x^2 + 2x + 1 at x=2, Test polynomial at x=0, Test polynomial at x=-1, Test with fractional powers, Test with float coefficients and float x, Test with empty coefficients and powers, Test with negative powers, Test dividing by zero raises an exception when power is negative (+3 more)

### Community 17 - "Test Quadratic Testsolvequadratic Module"
Cohesion: 0.15
Nodes (10): Return the real roots of ax² + bx + c = 0.      Parameters:     a (Union[int, fl, solve_quadratic(), Test with an equation that has two distinct real roots: x^2 - 3x + 2 = 0, Test with an equation that has one repeated real root: x^2 - 4x + 4 = 0, Test with an equation that has no real roots: x^2 + x + 1 = 0, Test that a=0 raises ValueError, Test with float coefficients: 0.5x^2 - 1.5x + 1 = 0, Test with b=0: x^2 - 4 = 0 (+2 more)

### Community 18 - "Factorial Discrete Module"
Cohesion: 0.12
Nodes (15): factorial(), n_permute_r(), Calculate permutations (nPr) using the formula: nPr = n! / (n - r)!.      Parame, Calculate factorial of n using recursion.      Parameters:     n (int): The numb, Test that factorial of 0 is 1., Test that factorial of 1 is 1., Test factorial calculation for positive integers., Test factorial calculation for a slightly larger number. (+7 more)

### Community 19 - "Greatest Common Divisor (GCD)"
Cohesion: 0.20
Nodes (16): compute_gcd(), prime_factorization_for_gcd(), Compute the Greatest Common Divisor (GCD) of two numbers using prime factorizati, Get prime factors of a number for GCD calculation.      Parameters:     n (int):, Test compute_gcd against Python's built-in math.gcd with a wide range     of ran, Test that the product of prime factors equals the original number., test_compute_gcd_against_math_gcd(), test_compute_gcd_common_factors() (+8 more)

### Community 20 - "Calculus Chain Rule"
Cohesion: 0.12
Nodes (16): chain_rule_derivative(), Apply the chain rule to find the derivative of [g(x)]^n.      Parameters:     in, test_chain_rule_derivative_basic(), test_chain_rule_derivative_constant_inner(), test_chain_rule_derivative_empty(), test_chain_rule_derivative_empty_inner(), test_chain_rule_derivative_exponent_one(), test_chain_rule_derivative_float_coefficients() (+8 more)

### Community 21 - "Least Common Multiple (LCM)"
Cohesion: 0.21
Nodes (7): compute_lcm(), prime_factorization_simple(), Compute the Least Common Multiple (LCM) of two numbers.      Parameters:     a (, Get prime factors of a number.      Parameters:     n (int): The number to facto, Test compute_lcm against Python's built-in math.lcm with random numbers., test_prime_factorization_simple(), TestLCM

### Community 22 - "Descriptive Statistics (Mode)"
Cohesion: 0.17
Nodes (9): mode(), Calculate the mode of a list of numbers.      Parameters:     data (List[Union[i, Test mode with an empty list., Test mode with a single mode., Test mode with multiple modes., Test mode when all elements have the same frequency., Test mode with float values., Test mode with mixed int and float values. (+1 more)

### Community 23 - "Descriptive Statistics (Mean)"
Cohesion: 0.24
Nodes (3): mean(), Calculate the mean (average) of a list of numbers.      Parameters:     data (Li, TestMean

### Community 24 - "Calculus Chain Rule"
Cohesion: 0.25
Nodes (3): compute_polynomial_derivative(), Compute the derivative of a polynomial.      Parameters:     coefficients (List[, TestComputePolynomialDerivative

### Community 25 - "Partition Test Discretetest Module"
Cohesion: 0.20
Nodes (12): partition(), Calculate the number of partitions of a positive integer n.      Parameters:, test_partition_exceeds_limit(), test_partition_large_number(), test_partition_negative(), test_partition_positive(), test_partition_too_large(), test_partition_zero() (+4 more)

### Community 26 - "Trigonometric Tangent Functions"
Cohesion: 0.25
Nodes (8): calculate_pi_ramanujan(), factorial_decimal(), Decimal, Calculate Pi using S. Ramanujan's formula.          Formula: 1/π = (2√2/9801) ×, Calculate factorial as a Decimal for high precision.      Parameters:     n (int, test_factorial_decimal_basic(), test_factorial_decimal_negative(), TestRamanujanAlgorithm

### Community 27 - "Binomial Theorem"
Cohesion: 0.26
Nodes (11): binomial_general_term(), Calculate the general term in the binomial expansion of (a + b)^n.      Paramete, prime_factorization(), Find the prime factorization of a number.      Parameters:     number (int): The, test_binomial_general_term(), test_binomial_general_term_edge_cases(), test_binomial_general_term_powers(), test_prime_factorization_composite_numbers() (+3 more)

### Community 28 - "Test Slope Testcalculateslope Module"
Cohesion: 0.27
Nodes (3): calculate_slope(), Calculate the slope of the line connecting two points.      Parameters:     x1 (, TestCalculateSlope

### Community 29 - "Euclidean Area (Triangle)"
Cohesion: 0.27
Nodes (3): area_of_triangle(), Calculate the area of a triangle given its base and height.      Parameters:, TestAreaOfTriangle

### Community 30 - "Euclidean Volume (Cone)"
Cohesion: 0.24
Nodes (3): Calculate the volume of a cone given its radius and height.      Parameters:, volume_of_cone(), TestVolumeOfCone

### Community 31 - "Euclidean Volume (Cylinder)"
Cohesion: 0.27
Nodes (3): Calculate the volume of a cylinder given its radius and height.      Parameters:, volume_of_cylinder(), TestVolumeOfCylinder

### Community 33 - "Simple Interest Math"
Cohesion: 0.30
Nodes (10): Calculate the total amount after applying simple interest.      Parameters:, simple_interest(), test_simple_interest_basic(), test_simple_interest_floats(), test_simple_interest_negative_principal(), test_simple_interest_negative_rate(), test_simple_interest_negative_time(), test_simple_interest_zero_principal() (+2 more)

### Community 34 - "Integration Format Module"
Cohesion: 0.17
Nodes (12): format_polynomial_integration(), Format an integrated polynomial as a string.      Parameters:     coefficients (, test_format_polynomial_integration_basic(), test_format_polynomial_integration_empty(), test_format_polynomial_integration_multiple_terms(), test_format_polynomial_integration_negative_coefficients(), test_format_polynomial_integration_negative_powers(), test_format_polynomial_integration_single_term_power_gt_one() (+4 more)

### Community 35 - "Euclidean Area (Rectangle)"
Cohesion: 0.29
Nodes (3): area_of_rectangle(), Calculate the area of a rectangle given its length and width.      Parameters:, TestAreaOfRectangle

### Community 36 - "Euclidean Volume (Sphere)"
Cohesion: 0.26
Nodes (6): Calculate the volume of a sphere given its radius.      Parameters:     radius (, volume_of_sphere(), Test volume with zero radius., Test volume with a positive integer radius., Test that negative radius raises ValueError., TestVolumeOfSphere

### Community 37 - "Descriptive Statistics (Median)"
Cohesion: 0.29
Nodes (3): median(), Calculate the median of a list of numbers.      Parameters:     data (List[Union, TestMedian

### Community 39 - "Integrate Polynomial Module"
Cohesion: 0.18
Nodes (10): integrate_polynomial(), Integrate a polynomial term by term.      Parameters:     coefficients (List[Uni, test_integrate_polynomial_basic(), test_integrate_polynomial_empty(), test_integrate_polynomial_fractional_powers(), test_integrate_polynomial_mixed_terms(), test_integrate_polynomial_negative_powers(), test_integrate_polynomial_power_minus_one() (+2 more)

### Community 40 - "Trigonometric Integration"
Cohesion: 0.24
Nodes (8): cosine(), factorial(), Calculate the cosine of an angle using Taylor series expansion.      Parameters:, Calculate factorial of n., factorial(), Calculate the sine of an angle using Taylor series expansion.      Parameters:, Calculate factorial of n., sine()

### Community 41 - "Approximation Partition Module"
Cohesion: 0.18
Nodes (10): partition_approximation(), Calculate an approximation of the number of partitions p(n) using Ramanujan's fo, Test edge cases for partition approximation., Test small values to ensure the formula computes successfully., Test larger values to ensure the formula produces expected output., Test that the approximation improves relative to the exact partition function., test_partition_approximation_edge_cases(), test_partition_approximation_large_values() (+2 more)

### Community 42 - "Trigonometric Tangent Functions"
Cohesion: 0.31
Nodes (3): distance_formula(), Calculate the distance between two points (x1, y1) and (x2, y2) using the distan, TestDistanceFormula

### Community 43 - "Test Intersection Intersection Module"
Cohesion: 0.31
Nodes (3): find_intersection(), Find the intersection point of two lines given their equations in the form y = m, TestFindIntersection

### Community 44 - "From Points Module"
Cohesion: 0.27
Nodes (3): line_from_points(), Return the equation of the line passing through two points in slope-intercept fo, TestLineFromPoints

### Community 45 - "Test Midpoint Testmidpointformula Module"
Cohesion: 0.31
Nodes (3): midpoint_formula(), Calculate the midpoint of a line segment in a 2D plane.      Parameters:     x1, TestMidpointFormula

### Community 46 - "Polynomial Format Module"
Cohesion: 0.20
Nodes (10): format_polynomial(), Format a polynomial as a string.      Parameters:     coefficients (List[Union[i, test_format_polynomial_all_ones_powers(), test_format_polynomial_all_zero_powers(), test_format_polynomial_basic(), test_format_polynomial_empty(), test_format_polynomial_floats(), test_format_polynomial_negative_and_zero() (+2 more)

### Community 47 - "Euclidean Area (Circle)"
Cohesion: 0.31
Nodes (3): area_of_circle(), Calculate the area of a circle given its radius.      Parameters:     radius (Un, TestAreaOfCircle

### Community 48 - "Euclidean Area (Square)"
Cohesion: 0.33
Nodes (3): area_of_square(), Calculate the area of a square given the length of its side.      Parameters:, TestAreaOfSquare

### Community 49 - "Euclidean Area (Square)"
Cohesion: 0.33
Nodes (3): pythagorean_theorem(), Calculate the length of the hypotenuse of a right triangle using the Pythagorean, TestPythagoreanTheorem

### Community 50 - "Euclidean Volume (Cuboid)"
Cohesion: 0.33
Nodes (3): Calculate the volume of a cuboid given its length, width, and height.      Param, volume_of_cuboid(), TestVolumeOfCuboid

### Community 51 - "Inverse Trigonometry (Arctan)"
Cohesion: 0.36
Nodes (4): calculate_arctan(), Decimal, Calculate the arctangent of (1/x) in radians with specified precision using Tayl, TestArcTanSecurity

### Community 52 - "Trigonometric Sine Functions"
Cohesion: 0.33
Nodes (8): cosine_taylor(), factorial(), Calculate sine using Taylor series., Calculate cosine using Taylor series., Calculate the tangent of an angle.      Parameters:     radians (Union[int, floa, Calculate factorial of n., sine_taylor(), tangent()

### Community 54 - "Compound Interest Math"
Cohesion: 0.32
Nodes (3): compound_interest(), Calculate the total amount after applying compound interest.      Parameters:, TestCompoundInterest

### Community 55 - "Trinomial General Module"
Cohesion: 0.36
Nodes (3): Calculate the general term in the trinomial expansion of (a + b + c)^n.      Par, trinomial_general_term(), TestTrinomialGeneralTerm

### Community 56 - "Euclidean Area (Triangle)"
Cohesion: 0.32
Nodes (3): herons_area_of_triangle(), Calculate the area of a triangle using Heron's formula.      Parameters:     a (, TestHeronsAreaOfTriangle

### Community 57 - "Trigonometric Sine Functions"
Cohesion: 0.38
Nodes (6): cosecant(), factorial(), Calculate sine using Taylor series., Calculate the cosecant of an angle.      Parameters:     radians (Union[int, flo, Calculate factorial of n., sine_taylor()

### Community 58 - "Trigonometric Sine Functions"
Cohesion: 0.38
Nodes (6): cosine_taylor(), factorial(), Calculate cosine using Taylor series., Calculate the secant of an angle.      Parameters:     radians (Union[int, float, Calculate factorial of n., secant()

### Community 60 - "Inverse Trigonometry (Arctan)"
Cohesion: 0.53
Nodes (5): calculate_arctan_series(), calculate_pi_machin(), Decimal, Calculate Pi using Machin's formula: π/4 = 4×arctan(1/5) - arctan(1/239).      P, Calculate arctan(1/x) using Taylor series expansion.      Parameters:     x (int

### Community 61 - "Inverse Trigonometry (Arctan)"
Cohesion: 0.53
Nodes (5): calculate_arctan_series_shanks(), calculate_pi_shanks(), Decimal, Calculate Pi using William Shanks' formula (multi-term arctan formula)., Calculate arctan(1/x) using Taylor series expansion for Shanks' formula.      Pa

### Community 62 - "Inverse Trigonometry (Arcsin)"
Cohesion: 0.50
Nodes (4): arcsin_numerical(), Calculate arcsine using numerical approximation by finding angle where sin(angle, Calculate sine using Taylor series expansion.      Parameters:     radians (Unio, sine_taylor_series()

### Community 64 - "Trigonometric Tangent Functions"
Cohesion: 0.67
Nodes (3): calculate_pi_chudnovsky(), Decimal, Calculate Pi using the Chudnovsky algorithm.          This is one of the fastest

### Community 66 - "Trigonometric Tangent Functions"
Cohesion: 0.67
Nodes (3): Internal Imports First Principle, No Standard Math Module Rule, Number One Principle

## Knowledge Gaps
- **8 isolated node(s):** `linear_eqn (Example Template)`, `Arjun Dev Jha`, `Aarav Rastogi`, `linear_eqn (Style Guide Example)`, `sigma (Style Guide Example)` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **18 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `evaluate_polynomial()` connect `Linear Equation Solvers` to `Test Algebra Testevaluatepolynomial Module`, `Test Algebra Testevaluatepolynomial Module`, `Factor Theorem Testing`, `Factor Theorem Testing`, `Remainder Theorem Algebra`, `Remainder Theorem Algebra`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Why does `TestFormatPolynomialChainRule` connect `Test Calculus Testformatpolynomialchainrule Module` to `Differentiation Chain & Second Derivative Rules`, `Trigonometric Integration`?**
  _High betweenness centrality (0.015) - this node is a cross-community bridge._
- **Why does `TestCalculusDifferentiation` connect `Test Calculus Testcalculusdifferentiation Module` to `Differentiation Chain & Second Derivative Rules`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **What connects `linear_eqn (Example Template)`, `Arjun Dev Jha`, `Aarav Rastogi` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Newton-Raphson & Root Finding` be split into smaller, more focused modules?**
  _Cohesion score 0.058469945355191254 - nodes in this community are weakly interconnected._
- **Should `Binomial Theorem` be split into smaller, more focused modules?**
  _Cohesion score 0.07092198581560284 - nodes in this community are weakly interconnected._
- **Should `Differentiation Chain & Second Derivative Rules` be split into smaller, more focused modules?**
  _Cohesion score 0.08309178743961353 - nodes in this community are weakly interconnected._