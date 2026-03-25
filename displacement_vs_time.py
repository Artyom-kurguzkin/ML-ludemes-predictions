import numpy as np
import matplotlib.pyplot as plt

# Time array (0 to 10 seconds)
t = np.linspace(0, 10, 500)

# Three motion scenarios
# 1. Uniform motion: displacement = velocity * time
v = 5  # m/s
displacement_uniform = v * t

# 2. Uniformly accelerated motion: displacement = 0.5 * a * t^2
a = 2  # m/s^2
displacement_accelerated = 0.5 * a * t**2

# 3. Simple harmonic motion: displacement = A * sin(omega * t)
A = 20   # amplitude in metres
omega = 1.0  # angular frequency rad/s
displacement_shm = A * np.sin(omega * t)

fig, axes = plt.subplots(3, 1, figsize=(10, 12))
fig.suptitle("Displacement vs Time", fontsize=16, fontweight="bold")

axes[0].plot(t, displacement_uniform, color="steelblue", linewidth=2)
axes[0].set_title("Uniform Motion  (v = 5 m/s)")
axes[0].set_xlabel("Time (s)")
axes[0].set_ylabel("Displacement (m)")
axes[0].grid(True, linestyle="--", alpha=0.6)

axes[1].plot(t, displacement_accelerated, color="darkorange", linewidth=2)
axes[1].set_title("Uniformly Accelerated Motion  (a = 2 m/s²)")
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("Displacement (m)")
axes[1].grid(True, linestyle="--", alpha=0.6)

axes[2].plot(t, displacement_shm, color="seagreen", linewidth=2)
axes[2].set_title("Simple Harmonic Motion  (A = 20 m, ω = 1 rad/s)")
axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("Displacement (m)")
axes[2].axhline(0, color="black", linewidth=0.8)
axes[2].grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("displacement_vs_time.png", dpi=150, bbox_inches="tight")
print("Graph saved to displacement_vs_time.png")
plt.show()
