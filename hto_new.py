#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 23:39:58 2023

@author: ananya
"""
# Hohmann's Transfer Orbit (Just to change orbit/altitude)

# import the required modules
import math as mt
import numpy as np

#Ask the user for the required inputs
r1 = float(input("Enter the value of the original satellite orbit (km): "))
r2 = float(input("Enter the value of the desired satellite orbit (km): "))
dry_mass = float(input("Enter the value of the satellite's dry mass (kg): "))
prop_mass = float(input("Enter the weight (kg) of chosen propellant: "))
isp = float(input("Enter the ISP (s) of your thruster: "))

# 35,782 and 192 (Test Numbers)
# 35786 and 250 (Test Numbers)
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

# Aphelion radius
ra = (r2 + Re) 

# Semi major axis
a = (rp + ra) / 2
#print(a)

# Total mechanical energy of transfer orbit
Et = - mu / (2 * a)
#print(Et)

# Calculations for 1st orbit
Et_1 = - mu / (2 * rp)
#print(Et_1)
v1 = mt.sqrt(2 * (Et_1 + mu / rp))
#print(v1)
vt1 = mt.sqrt(2 * (Et + mu / rp))
#print(vt1)
delv_1 = abs(vt1 - v1)
#print(delv_1)
 
# Calculations for 2nd orbit
Et_2 = - mu / (2 * ra)
#print(Et_2)
v2 = mt.sqrt(2 * (Et_2 + mu / ra))
#print(v2)
vt2 = mt.sqrt(2 * (Et + mu / ra))
#print(vt2)
delv_2 = abs(v2 - vt2)
#print(delv_2)

# Final delta v calculation
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

