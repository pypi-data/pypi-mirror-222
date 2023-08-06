# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:17:30 2023

@author: atrasias
"""

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

