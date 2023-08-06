# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:17:30 2023

@author: atrasias
"""
import numpy as np
from scipy.integrate import solve_ivp

def final_velocity(initial_velocity, acceleration, time):
    """
    Calculate the final velocity of an object given the initial velocity,
    acceleration, and time.
    """
    return initial_velocity + acceleration * time

def displacement(initial_velocity, time, acceleration):
    """
    Calculate the displacement of an object given the initial velocity,
    time, and acceleration.
    """
    return initial_velocity * time + 0.5 * acceleration * time ** 2

def force(mass, acceleration):
    """
    Calculate the force exerted on an object given the mass and acceleration.
    """
    return mass * acceleration

def kinetic_energy(mass, velocity):
    """
    Calculate the kinetic energy of an object given the mass and velocity.
    """
    return 0.5 * mass * velocity ** 2

def pendulum_period(length, gravity):
    """
    Calculate the period of a simple pendulum given the length and gravity.
    """
    import math
    return 2 * math.pi * math.sqrt(length / gravity)

def solve_ode(f, t_span, y0, t_eval=None):
    """
    Solve a first-order ordinary differential equation (ODE).
    
    Parameters
    ----------
    f : callable
        The function that describes the ODE, dy/dt = f(t, y).
    t_span : array-like, shape (2,)
        The interval of integration, [t_min, t_max].
    y0 : array-like
        The initial condition(s).
    t_eval : array-like, optional
        Times at which to store the computed solution. If not given, the solver determines these times automatically.
    
    Returns
    -------
    result : Bunch object with the following fields defined:
        t : ndarray, shape (n_points,)
            Time points.
        y : ndarray, shape (n, n_points)
            Values of the solution at `t`.
    """
    result = solve_ivp(f, t_span, y0, t_eval=t_eval, method='RK45')
    return result

