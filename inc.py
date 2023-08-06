#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 12:13:36 2023

@author: ananya
"""
# Inclination change while maintaining altitude

# import the required modules
import math as mt
import numpy as np

# Ask for user input
r1 = float(input("Enter the value of the original satellite orbit (km): "))
theta = float(input("Enter the desried inclination change (degrees): "))
dry_mass = float(input("Enter the value of the satellite's dry mass (kg): "))
prop_mass = float(input("Enter the weight (kg) of chosen propellant: "))
isp = float(input("Enter the ISP (s) of your thruster: "))

delta_i = np.radians(theta)
#print(delta_i)

# Define any constants for this code

# Radius of Earth 
Re = 6378

# Acceleration due to gravity
g = 9.81E-3

# Gravitational Parameter
mu = 3.986E+5

# Simple calculation to derive imp factors

# Perihilion radius
rp = (r1 + Re) 

# Total mechanical energy of satellite system
Et = - mu / (2 * rp)
#print(Et)

# Velocities at perihilion and aphelion
v1 = mt.sqrt(2 * (Et + mu / rp))
#print(v1)

# Delta v calculation
delta_v = 2 * v1 * mt.sin(delta_i/2)
print("Therefore the total delta v for this orbital manoeuvre is:",round(delta_v,2),"km/s")

# From here begins the mass difference calculation
#Total mass od satellite + propellant mass
total_mass = dry_mass + prop_mass

# Mass ratio of system calculation
mass_ratio = 1 - np.exp(-abs(delta_v) / (isp * g))
print("Therefore, the mass ratio is",round(mass_ratio,2))

# Calculation to find out mass of consumed fuel
consumed_fuel = total_mass * round(mass_ratio,2)
print("Therefore, the mass of consumed propellant is",round(consumed_fuel,2),"kg")