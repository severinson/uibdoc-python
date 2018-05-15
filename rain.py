import pandas as pd

df = pd.read_csv("./bergen_weather.csv")
df.dropna(inplace=True)
df['date'] = pd.to_datetime(df['date'])
df['index'] = list(range(len(df)))
print(df.head())

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (6, 6)
plt.rcParams['figure.dpi'] = 200

plt.figure()
# plt.plot(df['date'], df['rain'])
plt.plot(df['index'], df['rain'], '.')

from scipy.optimize import curve_fit
f = lambda x, a, b, c: a*pow(x, 2) + b*x + c
x, y = df['index'], df['rain']
p, _ = curve_fit(f, x, y)
plt.plot(x, [f(i, *p) for i in x])

plt.title('Sophisticated Bergen weather predictions')
plt.xlim(0, len(df))
plt.ylim(0, 90)
plt.xlabel('Day')
plt.ylabel('Rain [mm]')
plt.show()
