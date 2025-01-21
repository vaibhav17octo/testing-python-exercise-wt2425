import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()

    w, h, dx, dy = 10., 6., 0.33, 0.35
    d, T_cold, T_hot = 4., 300., 700.
    expected_dt = (dx * dx * dy * dy) / (2 * d * (dx * dx + dy * dy))

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    assert np.allclose(expected_dt, solver.dt), f"Returned {solver.dt}, but must be {expected_dt}"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()

    u = np.full((5, 5), 300.)

    solver.initialize_domain(1., 1., 0.2, 0.2)
    solver.initialize_physical_parameters(2., 300., 700.)
    solver_u = solver.set_initial_condition()

    assert np.allclose(solver_u, u), f"Returned initial condition is incorrect: is {solver_u}, should be {u}"