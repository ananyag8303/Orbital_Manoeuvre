#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 13:05:22 2023

@author: ananya
"""

# De orbital burn delta v calculations (Single Impulse orbital manoeuvre)

# Import the required modules
import math as mt
import numpy as np

# Ask the user for the required inputs
r1 = float(input("Enter the value of the original satellite orbit (km): "))
theta = float(input("Enter the impact angle you are aiming for (degrees): "))
dry_mass = float(input("Enter the value of the satellite's dry mass (kg): "))
prop_mass = float(input("Enter the weight (kg) of chosen propellant: "))
isp = float(input("Enter the ISP (s) of your thruster: "))

# Define the constants for this code

# Radius of Earth (km)
Re = 6378

# Acceleration due to gravity (km/s^-2)
g = 9.81E-3

# Gravitational Parameter
mu = 3.986E+5

# Delta v calculations (main)

# Convert to radians
delta_i = np.radians(theta)

total_angle = np.pi + delta_i

# velocity of object in initial orbit
ra = Re + r1
v1 = mt.sqrt(mu/ra)

# Orbit eccentricity calculation
e = r1 / (r1 + Re * (1 + np.cos(total_angle)))

# Specific angular momentum calculation
h = np.sqrt(ra * mu * (1 - e))

# velocity of object in final orbit
v2 = h / ra

#Final delta v calculation
delta_v = v2 - v1
print("Therefore the total delta v for this orbital manoeuvre is:",round(delta_v,2),"km/s")

# Mass difference calculations

#Total mass od satellite + propellant mass
total_mass = dry_mass + prop_mass

# Mass ratio of system calculation
mass_ratio = 1 - np.exp(-abs(delta_v) / (isp * g))
print("Therefore, the mass ratio is",round(mass_ratio,2))

# Calculation to find out mass of consumed fuel
consumed_fuel = total_mass * round(mass_ratio,2)
print("Therefore, the mass of consumed propellant is",round(consumed_fuel,2),"kg")

