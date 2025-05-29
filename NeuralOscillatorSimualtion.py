import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Parameters
N = 30
K_initial = 5.0
dt = 0.05
x_window = 10  # Time window shown on the plot

omega = np.random.normal(loc=1.0, scale=0.1, size=N)
theta = np.random.uniform(0, 2 * np.pi, N)

r_values = []
time_values = []

# Create figure and gridspec layout
fig = plt.figure(figsize=(12, 7))
gs = fig.add_gridspec(3, 2, height_ratios=[10, 0.5, 0.5])

# Subplots
ax_phase = fig.add_subplot(gs[0, 0])
ax_order = fig.add_subplot(gs[0, 1])
ax_slider = fig.add_subplot(gs[1, :])

# Phase plot
ax_phase.set_xlim(-1.2, 1.2)
ax_phase.set_ylim(-1.2, 1.2)
ax_phase.set_aspect('equal')
ax_phase.set_title('Neural Oscillators on Unit Circle')
points, = ax_phase.plot([], [], 'bo', ms=8)

# Order plot
ax_order.set_ylim(0, 1.05)
ax_order.set_xlabel('Time (s)')
ax_order.set_ylabel('r(t)')
ax_order.set_title('Order Parameter (Synchronization)')
order_line, = ax_order.plot([], [], 'r-', lw=2)

# Slider
slider_K = Slider(ax_slider, 'Coupling K', 0.0, 10.0, valinit=K_initial, valstep=0.1)

# Update function
def update(frame):
    global theta

    K = slider_K.val

    dtheta = omega + (K / N) * np.sum(np.sin(theta[:, None] - theta), axis=1)
    theta += dtheta * dt

    x = np.cos(theta)
    y = np.sin(theta)
    points.set_data(x, y)

    r = np.abs(np.mean(np.exp(1j * theta)))
    time = frame * dt

    r_values.append(r)
    time_values.append(time)

    # Show only the recent `x_window` seconds
    min_time = max(0, time - x_window)
    visible_indices = [i for i, t in enumerate(time_values) if t >= min_time]

    visible_times = [time_values[i] for i in visible_indices]
    visible_rs = [r_values[i] for i in visible_indices]

    order_line.set_data(visible_times, visible_rs)
    ax_order.set_xlim(min_time, time)

    return points, order_line

# Animation
ani = FuncAnimation(fig, update, interval=50, blit=False)

plt.tight_layout()
plt.show()
