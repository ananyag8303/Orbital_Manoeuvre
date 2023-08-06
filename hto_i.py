#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:55:32 2023

@author: ananya
"""

# Orbit Transfer with inclination change followed by altitude change

# import the required modules
import numpy as np

# Ask for user input
r1 = float(input("Enter the value of the original satellite orbit (km): "))
r2 = float(input("Enter the value of the desired satellite orbit (km): "))
theta = float(input("Enter the desried inclination change (degrees): "))
dry_mass = float(input("Enter the value of the satellite's dry mass (kg): "))
prop_mass = float(input("Enter the weight (kg) of chosen propellant: "))
isp = float(input("Enter the ISP (s) of your thruster: "))

# 300 and 35785.9
delta_i = np.radians(theta)
#print(delta_i)

# Define any constants for this code

#Radius of Earth 
Re = 6378.1

#Acceleration due to gravity
g = 9.81E-3

# Gravitational Parameter
mu = 3.986E+5

# Simple calculation to derive imp factors

# Perihilion radius
rp = (r1 + Re) 

# Aphelion radius
ra = (r2 + Re) 

# Semi major axis
a = (rp + ra) / 2

# Conversion to radians
delta_i = np.radians(theta)

# Total mechnical energy
Et = - mu / (2 * a)

# Calculations in 1st orbit
v1 = np.sqrt(mu / rp)  
#E1 = v1**2 / 2 - mu / rp  
vt1 = np.sqrt(2 * (Et + mu / rp))

# Calculations in 2nd orbit
v2 = np.sqrt(mu / ra)  
#E2 = v2**2 / 2 - mu / ra  
vt2 = np.sqrt(2 * (Et + mu / ra))

# Delta v calculations
delv_1 = np.sqrt(v1**2 + vt1**2 - 2 * v1 * vt1 * np.cos(delta_i))
delv_2 = abs(vt2 - v2)
delta_v = delv_1 + delv_2
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