# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
============================================================== test session starts ==============================================================
platform darwin -- Python 3.9.6, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/vaibhavgil/Documents/Stuttgart/sem 2/SSE/exercise/testing-python-exercise-wt2425
collected 3 items                                                                                                                               

tests/unit/test_diffusion2d_functions copy.py F..                                                                                         [100%]

=================================================================== FAILURES ====================================================================
____________________________________________________________ test_initialize_domain _____________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        dx = 0.33
        dy = 0.35
        w = 17.0
        h = 10.0
        nx = int(w / dx)
        ny = int(h / dy)
    
        # Act
        solver.initialize_domain(w, h, dx, dy)
>       assert solver.nx == nx, f"Returned nx is incorrect: is {solver.nx}, should be {nx}"
E       AssertionError: Returned nx is incorrect: is 30, should be 51
E       assert 30 == 51
E        +  where 30 = <diffusion2d.SolveDiffusion2D object at 0x102a884f0>.nx

tests/unit/test_diffusion2d_functions copy.py:19: AssertionError
============================================================ short test summary info ============================================================
FAILED tests/unit/test_diffusion2d_functions copy.py::test_initialize_domain - AssertionError: Returned nx is incorrect: is 30, should be 51
========================================================== 1 failed, 2 passed in 0.31s ==========================================================
============================================================== test session starts ==============================================================
platform darwin -- Python 3.9.6, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/vaibhavgil/Documents/Stuttgart/sem 2/SSE/exercise/testing-python-exercise-wt2425
collected 3 items                                                                                                                               

tests/unit/test_diffusion2d_functions copy.py .F.                                                                                         [100%]

=================================================================== FAILURES ====================================================================
______________________________________________________ test_initialize_physical_parameters ______________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        dx = 0.33
        dy = 0.35
        d = 10.0
    
        dx2 = dx * dx
        dy2 = dy * dy
        dt = dx2 * dy2 / (2 * d * (dx2 + dy2))
        # Setting the values as the function assumes that dx and dy are already set
        solver.dx = dx
        solver.dy = dy
    
        solver.initialize_physical_parameters(d)
    
        # Checking with almost equality as floating calculation might create a slight difference
>       assert solver.dt == dt, f"Expected dt = {dt}, but got {solver.dt}"
E       AssertionError: Expected dt = 0.002882508643042351, but got 0.0019216724286949005
E       assert 0.0019216724286949005 == 0.002882508643042351
E        +  where 0.0019216724286949005 = <diffusion2d.SolveDiffusion2D object at 0x1030db100>.dt

tests/unit/test_diffusion2d_functions copy.py:42: AssertionError
------------------------------------------------------------- Captured stdout call --------------------------------------------------------------
dt = 0.0019216724286949005
============================================================ short test summary info ============================================================
FAILED tests/unit/test_diffusion2d_functions copy.py::test_initialize_physical_parameters - AssertionError: Expected dt = 0.002882508643042351, but got 0.0019216724286949005
========================================================== 1 failed, 2 passed in 0.29s ==========================================================
============================================================== test session starts ==============================================================
platform darwin -- Python 3.9.6, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/vaibhavgil/Documents/Stuttgart/sem 2/SSE/exercise/testing-python-exercise-wt2425
collected 3 items                                                                                                                               

tests/unit/test_diffusion2d_functions copy.py ..F                                                                                         [100%]

=================================================================== FAILURES ====================================================================
__________________________________________________________ test_set_initial_condition ___________________________________________________________

    def test_set_initial_condition():
        solver = SolveDiffusion2D()
        T_cold = 300.
        T_hot = 700.
        dx = 0.33
        dy = 0.35
        d = 10.0
        nx = 10
        ny = 10
    
        solver.nx = nx
        solver.ny = ny
        solver.dx = dx
        solver.dy = dy
        solver.T_hot = T_hot
        solver.T_cold = T_cold
    
        u_manual = T_cold * np.ones((nx, ny))
        r = 2
        cx, cy = 5, 5
    
    
        for i in range(nx):
            for j in range(ny):
                p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
                if p2 < r ** 2:
                    u_manual[i, j] = T_hot
    
    
        u = solver.set_initial_condition()
    
>       np.testing.assert_array_equal(u, u_manual, err_msg="Initial condition field is not correct.")

tests/unit/test_diffusion2d_functions copy.py:77: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.9/site-packages/numpy/_utils/__init__.py:85: in wrapper
    return fun(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

args = (<built-in function eq>, array([[700., 700., 700., 700., 700., 700., 700., 700., 700., 700.],
       [700., 700., 700....300., 300., 300., 300., 300., 300., 300., 300.],
       [300., 300., 300., 300., 300., 300., 300., 300., 300., 300.]]))
kwds = {'err_msg': 'Initial condition field is not correct.', 'header': 'Arrays are not equal', 'strict': False, 'verbose': True}

    @wraps(func)
    def inner(*args, **kwds):
        with self._recreate_cm():
>           return func(*args, **kwds)
E           AssertionError: 
E           Arrays are not equal
E           Initial condition field is not correct.
E           Mismatched elements: 91 / 100 (91%)
E           Max absolute difference among violations: 400.
E           Max relative difference among violations: 1.33333333
E            ACTUAL: array([[700., 700., 700., 700., 700., 700., 700., 700., 700., 700.],
E                  [700., 700., 700., 700., 700., 700., 700., 700., 700., 700.],
E                  [700., 700., 700., 700., 700., 700., 700., 700., 700., 700.],...
E            DESIRED: array([[300., 300., 300., 300., 300., 300., 300., 300., 300., 300.],
E                  [300., 300., 300., 300., 300., 300., 300., 300., 300., 300.],
E                  [300., 300., 300., 300., 300., 300., 300., 300., 300., 300.],...

/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/contextlib.py:79: AssertionError
============================================================ short test summary info ============================================================
FAILED tests/unit/test_diffusion2d_functions copy.py::test_set_initial_condition - AssertionError: 



### unittest log
Fdt = 0.0019216724286949005
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/vaibhavgil/Documents/Stuttgart/sem 2/SSE/exercise/testing-python-exercise-wt2425/tests/unit/test_diffusion2d_functions.py", line 27, in test_initialize_domain
    self.assertEqual(self.solver.nx, nx, f"Expected nx = {nx}, but got {self.solver.nx}")
AssertionError: 5 != 51 : Expected nx = 51, but got 5

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/vaibhavgil/Documents/Stuttgart/sem 2/SSE/exercise/testing-python-exercise-wt2425/tests/unit/test_diffusion2d_functions.py", line 42, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, dt, delta=1e-9, msg=f"Expected dt = {dt}, but got {self.solver.dt}")
AssertionError: 0.0019216724286949005 != 0.002882508643042351 within 1e-09 delta (0.0009608362143474504 difference) : Expected dt = 0.002882508643042351, but got 0.0019216724286949005

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/vaibhavgil/Documents/Stuttgart/sem 2/SSE/exercise/testing-python-exercise-wt2425/tests/unit/test_diffusion2d_functions.py", line 70, in test_set_initial_condition
    np.testing.assert_array_equal(u, u_manual, err_msg="Initial condition field is not correct.")
  File "/Users/vaibhavgil/Documents/Stuttgart/sem 2/SSE/exercise/testing-python-exercise-wt2425/.venv/lib/python3.9/site-packages/numpy/_utils/__init__.py", line 85, in wrapper
    return fun(*args, **kwargs)
  File "/Users/vaibhavgil/Documents/Stuttgart/sem 2/SSE/exercise/testing-python-exercise-wt2425/.venv/lib/python3.9/site-packages/numpy/testing/_private/utils.py", line 1021, in assert_array_equal
    assert_array_compare(operator.__eq__, actual, desired, err_msg=err_msg,
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/contextlib.py", line 79, in inner
    return func(*args, **kwds)
  File "/Users/vaibhavgil/Documents/Stuttgart/sem 2/SSE/exercise/testing-python-exercise-wt2425/.venv/lib/python3.9/site-packages/numpy/testing/_private/utils.py", line 885, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Arrays are not equal
Initial condition field is not correct.
Mismatched elements: 91 / 100 (91%)
Max absolute difference among violations: 400.
Max relative difference among violations: 1.33333333
 ACTUAL: array([[700., 700., 700., 700., 700., 700., 700., 700., 700., 700.],
       [700., 700., 700., 700., 700., 700., 700., 700., 700., 700.],
       [700., 700., 700., 700., 700., 700., 700., 700., 700., 700.],...
 DESIRED: array([[300., 300., 300., 300., 300., 300., 300., 300., 300., 300.],
       [300., 300., 300., 300., 300., 300., 300., 300., 300., 300.],
       [300., 300., 300., 300., 300., 300., 300., 300., 300., 300.],...

----------------------------------------------------------------------
Ran 3 tests in 0.011s

FAILED (failures=3)

### integration test logs
==================================================== test session starts ====================================================
platform darwin -- Python 3.9.6, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/vaibhavgil/Documents/Stuttgart/sem 2/SSE/exercise/testing-python-exercise-wt2425
collected 5 items                                                                                                           

tests/integration/test_diffusion2d.py F.                                                                              [ 40%]
tests/unit/test_diffusion2d_functions.py .FF                                                                          [100%]

========================================================= FAILURES ==========================================================
____________________________________________ test_initialize_physical_parameters ____________________________________________

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
    
>       assert np.allclose(expected_dt, solver.dt), f"Returned {solver.dt}, but must be {expected_dt}"
E       AssertionError: Returned 0.004804181071737252, but must be 0.007206271607605877
E       assert False
E        +  where False = <function allclose at 0x101e344f0>(0.007206271607605877, 0.004804181071737252)
E        +    where <function allclose at 0x101e344f0> = np.allclose
E        +    and   0.004804181071737252 = <diffusion2d.SolveDiffusion2D object at 0x103b2e700>.dt

tests/integration/test_diffusion2d.py:18: AssertionError


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
