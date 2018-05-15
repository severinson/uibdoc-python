import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

'''

last task from basic.

'''

import random
def flip():
    if random.random() < 0.5:
        return 0 # heads
    else:
        return 1 # tails

def sample():
    count = 0
    outcome = flip()
    while outcome == 0:
        count += 1 # equivalent to count = count + 1
        outcome = flip()
    return count

samples = np.fromiter((sample() for _ in range(100000)), dtype=int)
plt.hist(samples, bins=20)
plt.show()

'''

task: create a beautiful plot of x against x^2 for 0 <= x < 10. Use
numpy.linspace to find values of x and numpy.power to compute the
square of x. Save this figure to disk.

'''
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (6, 6)
plt.rcParams['figure.dpi'] = 200
samples = 100
x = np.linspace(0, 10, samples)
y = np.power(x, 2)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.title('dat plot')
plt.savefig('dat_plot.png', dpi='figure')
plt.show()

'''

task: Use scipy.optimize.curve_fit to fit a curve of the form
 "y=a+bx", where a and b are coefficients to this data:
x = [1, 2, 3, 4]
y = [13.46688604, 18.58857204, 20.51804834, 27.6660338]

First, plot the given x and y data. Second, fit parameters (a, b) to
the data, third plot the given x and y together with the fit
curve. Use np.linspace to find values of x.

'''



from scipy.optimize import curve_fit
x = [1, 2, 3, 4]
y = [13.46688604, 18.58857204, 20.51804834, 27.6660338]
f = lambda x, a, b: a + b*x
p, _ = curve_fit(f, x, y)
print(p)
plt.figure()
plt.plot(x, y)

t = np.linspace(1, 4, 100)
plt.plot(t, [f(x, *p) for x in t])
plt.show()

'''

task: use pandas.read_csv to read the csv file "scatter.csv", print it
to terminal, and then plot its "x" column against its "y" column using
pyplot.

'''

# code used to generate the data
# n = 100
# x = np.linspace(0, 1, n)
# y = np.log2(x) + np.random.randn(n)
# df = pd.DataFrame({'x': x, 'y': y})
# df.to_csv('scatter.csv', index=False)

# read and plot it
df = pd.read_csv('scatter.csv')
plt.scatter(df['x'], df['y'])
plt.show()
