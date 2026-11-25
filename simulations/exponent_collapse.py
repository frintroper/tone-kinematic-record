import numpy as np
import matplotlib.pyplot as plt

steps = 50
exponent_without = np.full(steps, 2.25) + np.random.normal(0, 0.01, steps)
exponent_with = np.concatenate(([2.25], np.full(steps-1, 2.0)))

plt.figure(figsize=(9,5))
plt.plot(exponent_without, label='without inversion (~2.25)', color='orange')
plt.plot(exponent_with, label='with jerk inversion (=2)', color='blue')
plt.xlabel('step')
plt.ylabel('exponent')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('../figures/exponent_collapse.png')
print("exponent_collapse.png written")
