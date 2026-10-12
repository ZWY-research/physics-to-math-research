"""Specified discrete witnesses only; no simulation or general machine proof."""

from fractions import Fraction
import math
import sys
import traceback


def main():
    beta = 1.0
    epsilon = math.log(4.0)
    relative_tolerance = 1e-12
    absolute_tolerance = 1e-12

    # H0=(0,0), H1=(0,epsilon), identity map. Check the exact
    # Boltzmann weight 1/4 against its floating exponential evaluation.
    final_weights = (Fraction(1), Fraction(1, 4))
    assert math.isclose(math.exp(-beta * epsilon), float(final_weights[1]),
                        rel_tol=relative_tolerance, abs_tol=absolute_tolerance)
    initial_weights = (Fraction(1), Fraction(1))
    z0 = sum(initial_weights, Fraction(0))
    z1 = sum(final_weights, Fraction(0))
    ratio = z1 / z0
    canonical_probabilities = tuple(weight / z0 for weight in initial_weights)
    canonical_exponential_mean = sum(
        (p * weight for p, weight in zip(canonical_probabilities, final_weights)),
        Fraction(0),
    )
    noncanonical_probabilities = (Fraction(1), Fraction(0))
    noncanonical_exponential_mean = sum(
        (p * weight for p, weight in zip(noncanonical_probabilities, final_weights)),
        Fraction(0),
    )
    assert z0 == 2 and z1 == Fraction(5, 4)
    assert ratio == Fraction(5, 8)
    assert canonical_exponential_mean == Fraction(5, 8)
    assert noncanonical_exponential_mean == 1
    assert noncanonical_exponential_mean != ratio

    delta_f = -math.log(float(ratio)) / beta
    assert math.isclose(delta_f, math.log(8.0 / 5.0),
                        rel_tol=relative_tolerance, abs_tol=absolute_tolerance)
    assert delta_f > 0
    # N=1 is sufficient for the requested all-zero-work finite-sample witness.
    # Values are fixed, not randomly sampled; the event has probability 1/2.
    zero_work_samples = (0.0,)
    sample_exponential_mean = sum(math.exp(-beta * w) for w in zero_work_samples) / len(zero_work_samples)
    estimate = -math.log(sample_exponential_mean) / beta
    assert math.isclose(estimate, 0.0, rel_tol=relative_tolerance, abs_tol=absolute_tolerance)
    assert estimate < delta_f
    mean_work = sum(float(p) * w for p, w in zip(canonical_probabilities, (0.0, epsilon)))
    assert math.isclose(mean_work, epsilon / 2,
                        rel_tol=relative_tolerance, abs_tol=absolute_tolerance)
    assert mean_work >= delta_f

    print(f"beta = {beta:.1f}")
    print(f"epsilon = ln(4) = {epsilon:.15g}")
    print(f"exp(-beta*epsilon) = {math.exp(-beta * epsilon):.15g}")
    print(f"Z0 = {z0}; Z1 = {z1}; Z1/Z0 = {ratio} = {float(ratio):.15g}")
    print(f"canonical exponential mean = {canonical_exponential_mean}")
    print(f"noncanonical exponential mean = {noncanonical_exponential_mean}")
    print(f"delta_F = ln(8/5) = {delta_f:.15g}")
    print(f"all-zero-work sample: N = {len(zero_work_samples)}; estimate = {estimate:.15g} < delta_F")
    print(f"canonical mean work = {mean_work:.15g} >= delta_F")
    print(f"float tolerances: rel_tol = {relative_tolerance}; abs_tol = {absolute_tolerance}")
    print("PASS: all specified discrete-witness assertions passed.")
    print("Scope: deterministic two-state checks; not a general theorem's machine proof.")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("FAIL: a specified discrete-witness check failed.", file=sys.stderr)
        traceback.print_exc()
        raise SystemExit(1)
