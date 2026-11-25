import numpy as np
import matplotlib.pyplot as plt

def step(r, j, mode):
    if mode == "tone":
        j = 1.0 / j
        r *= 0.6 * abs(j - 1.0) + 0.05
        r = max(r, 0.0)
    else:
        r = max(r + 0.02 * np.random.randn(), 0.5)
    return r, j

def run(mode, steps=40):
    r, j = 1.0, 2.0
    hist = [r]
    for _ in range(steps):
        r, j = step(r, j, mode)
        hist.append(r)
    return hist

np.random.seed(42)
plt.figure(figsize=(9,5))
plt.plot(run("zfc"), label='ZFC/Lean residual', color='orange', ls='--')
plt.plot(run("tone"), label='TONE inversion', color='blue')
plt.axhline(0, color='green', ls=':', label='O(1)')
plt.xlabel('steps')
plt.ylabel('residual debt')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('../figures/lean_truncation.png')
print("lean_truncation.png written")
