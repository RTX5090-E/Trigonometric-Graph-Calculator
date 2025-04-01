# Main file for the trigonometric calculator with GUI
# This will allow the user to choose from 2 modes: 1. Normal Mode, 2. Graph Mode
# 1. Normal Mode - This will allow the user to calculate either cosine, sine, or tangent
# 2. Graph Mode - This will allow the user to view the graph of the trigonometric functions

# Importing the necessary libraries
import math
import mpmath as mp
from matplotlib import pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *

# Importing libraries to handle paths
import os
import sys

# Adding directories to sys.path
sys.path.append(r'C:\Users\Prashant\OneDrive\Documents\Python\Trigonometry Graph Calculator\Graph Mode')

# Now you can import files from the specified directories
from sine_graph import plot_sine_graph
from cosine_graph import plot_cosine_graph
from tangent_graph import plot_tangent_graph

# Input
input1 = input("Welcome!, Choose a mode for your trigonometric calculations(1. Normal Mode, 2. Graph Mode): ")

# Function to calculate trigonometric values
def main():
    if input1 == "1":
        input2 = input("Choose a function(sin, cos, tan, asin, acos, atan, cosec, sec, cot, sinh, cosh, tanh, asinh, acosh, atanh): ")

        if input2 == "sin":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.sin(rad)
            print(f"The sin of angle {angle} degrees is {angle2}")

        elif input2 == "cos":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.cos(rad)
            print(f"The cos of angle {angle} degrees is {angle2}")

        elif input2 == "tan":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.tan(rad)
            print(f"The tan of angle {angle} degrees is {angle2}")

        elif input2 == "asin":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.asin(rad)
            print(f"The asin of angle {angle} degrees is {angle2}")

        elif input2 == "acos":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.acos(rad)
            print(f"The acos of angle {angle} degrees is {angle2}")

        elif input2 == "atan":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.atan(rad)
            print(f"The atan of angle {angle} degrees is {angle2}")

        elif input2 == "cosec":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.csc(rad)
            print(f"The cosec of angle {angle} degrees is {angle2}")

        elif input2 == "sec":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.sec(rad)
            print(f"The sec of angle {angle} degrees is {angle2}")

        elif input2 == "cot":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.cot(rad)
            print(f"The cot of angle {angle} degrees is {angle2}")

        elif input2 == "sinh":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.sinh(rad)
            print(f"The sinh of angle {angle} degrees is {angle2}")

        elif input2 == "cosh":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.cosh(rad)
            print(f"The cosh of angle {angle} degrees is {angle2}")

        elif input2 == "tanh":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.tanh(rad)
            print(f"The tanh of angle {angle} degrees is {angle2}")

        elif input2 == "asinh":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.asinh(rad)
            print(f"The asinh of angle {angle} degrees is {angle2}")

        elif input2 == "acosh":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.acosh(rad)
            print(f"The acosh of angle {angle} degrees is {angle2}")

        elif input2 == "atanh":
            angle = float(input("Enter the angle in degrees: "))
            rad = mp.radians(angle)
            angle2 = mp.atanh(rad)
            print(f"The atanh of angle {angle} degrees is {angle2}")

    elif input1 == "2":
        mode = input("Choose what Graph to plot(Sine, Cosine, Tangent): ")

        if mode == "Sine":
            plot_sine_graph()

        elif mode == "Cosine":
            plot_cosine_graph()
        
        elif mode == "Tangent":
            plot_tangent_graph()
    
if __name__ == "__main__":
    main()