import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

plt.figure(1)
plt.subplot(211)

# Plot the histograms
plt.hist(
  flights, range = (0, 365), bins = 365, color='purple', edgecolor='blue'
)
plt.title('Voos por dia')
plt.xlabel('dias')
plt.ylabel('voos')


plt.subplot(212)

plt.hist(
  in_bloom, range = (0, 365), bins = 365, edgecolor='red'
)
plt.title('desabrochar das flores')
plt.xlabel('dias')
plt.ylabel('horas')
plt.tight_layout()
plt.show()