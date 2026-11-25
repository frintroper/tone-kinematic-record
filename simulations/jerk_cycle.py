import numpy as np
import matplotlib.pyplot as plt

def iterate(j0, steps=15):
    traj = [j0]
    j = j0
    for _ in range(steps):
        j = 1.0 / j
        traj.append(j)
    return traj

starts = [3.0, 0.5, -1.5, 2.0, -0.25]
plt.figure(figsize=(9,5))
for s in starts:
    plt.plot(iterate(s), marker='o', label=f'start {s}')
plt.axhline(1, color='green', ls='--', label='+1')
plt.axhline(-1, color='red', ls='--', label='-1')
plt.xlabel('iteration')
plt.ylabel('j')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('../figures/jerk_cycle.png')
print("jerk_cycle.png written")
