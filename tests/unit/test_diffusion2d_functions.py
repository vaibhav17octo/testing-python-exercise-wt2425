import unittest
import numpy as np
from diffusion2d import SolveDiffusion2D

class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()
        self.T_cold = 300.
        self.T_hot = 700.
        self.dx = 0.33
        self.dy = 0.35
        self.w = 17.0
        self.h = 17.0
        self.d = 10.0

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        nx = int(self.w / self.dx)
        ny = int(self.h / self.dy)
        
        # Act
        self.solver.initialize_domain(self.w, self.h, self.dx, self.dy)

        self.assertEqual(self.solver.nx, nx, f"Expected nx = {nx}, but got {self.solver.nx}")
        self.assertEqual(self.solver.ny, ny, f"Expected ny = {ny}, but got {self.solver.ny}")


    def test_initialize_physical_parameters(self):
        dx2 = self.dx * self.dx
        dy2 = self.dy * self.dy
        dt = dx2 * dy2 / (2 * self.d * (dx2 + dy2))
        # Setting the values as the function assumes that self.dx and self.dy are already set
        self.solver.dx = self.dx
        self.solver.dy = self.dy

        self.solver.initialize_physical_parameters(self.d)

        # Checking with almost equality as floating calculation might create a slight difference
        self.assertAlmostEqual(self.solver.dt, dt, delta=1e-9, msg=f"Expected dt = {dt}, but got {self.solver.dt}")


    def test_set_initial_condition(self):       
        nx = 10          
        ny = 10         

        self.solver.nx = nx
        self.solver.ny = ny
        self.solver.dx = self.dx
        self.solver.dy = self.dy
        self.solver.T_hot = self.T_hot
        self.solver.T_cold = self.T_cold

        u_manual = self.T_cold * np.ones((nx, ny)) 
        r = 2 
        cx, cy = 5, 5 
        

        for i in range(nx):
            for j in range(ny):
                p2 = (i * self.solver.dx - cx) ** 2 + (j * self.solver.dy - cy) ** 2
                if p2 < r ** 2:
                    u_manual[i, j] = self.T_hot


        u = self.solver.set_initial_condition()

        np.testing.assert_array_equal(u, u_manual, err_msg="Initial condition field is not correct.")
