'''This is the second module of the UiBdoc intro to Python for
researchers. It covers the basics of scientific computing in Python.

To get comfortable with numpy, start by completing some of the
problems at this link:
https://www.machinelearningplus.com/python/101-numpy-exercises-python/

Once you feel comfortable, solve the last problem from the basic
module using numpy arrays and functions. Instead of creating a dict at
the end, use pyplot to plot a histogram of the data. The method you
need is plt.hist(). See this link for its API:
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html

'''

import numpy as np # allows calling function with np.f() instead of numpy.f()
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

'''

task: create a beautiful plot of x against x^2 for 0 <= x < 10. Use
numpy.linspace to find values of x and numpy.power to compute the
square of x. Save this figure to disk.

task: Use scipy.optimize.curve_fit to fit a curve of the form
 "y=a+bx", where a and b are coefficients to this data:
x = [1, 2, 3, 4]
y = [13.46688604, 18.58857204, 20.51804834, 27.6660338]

First, plot the given x and y data. Second, fit parameters (a, b) to
the data, third plot the given x and y together with the fit curve.

task: use pandas.read_csv to read the csv file "scatter.csv", print it
to terminal, and then plot its "x" column against its "y" column using
pyplot.

'''
