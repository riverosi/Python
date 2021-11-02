import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data-2021-11-02-1959.csv')
gain_poncho = 24.0
counts_to_volts = 2.4858e-5 / gain_poncho
df.head()
df[df.select_dtypes(include=['number']).columns] *= counts_to_volts
df.head()
df.plot(y=['chn1','chn2'])
# Plot
plt.grid(True)
plt.show()