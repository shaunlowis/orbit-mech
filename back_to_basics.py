# Basic polar coordinates plot. Will move to cartesian as polar sucks.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib_rc


def calc_r(a, e, theta):
    return (a * (1 - e**2)) / (1 + e * np.cos(theta))


a_sat = 5137
e_sat = 0.3
theta = np.linspace(0, 2 * np.pi, 360)
r_sat = calc_r(a_sat, e_sat, theta)

a_earth = 6378
e_earth = 0

r_earth = calc_r(a_earth, e_earth, theta)

a_sat_first_burn = 6439.23
e_sat_first_burn = e_sat
r_sat_first_burn = calc_r(a_sat_first_burn, e_sat_first_burn, theta)

fig, ax = plt.subplots(subplot_kw={"projection": "polar"})

ax.plot(theta, r_earth, label="Earth, true scale")
ax.plot(theta, r_sat, label="Satellite launch orbit")
ax.scatter(
    160,
    calc_r(a_sat, e_sat, 160),
    marker="x",
    label="Satellite location",
    zorder=10,
    c="black",
    clip_on=False,
)
# ax.plot(theta, r_sat_first_burn, label="Satellite orbit after first burn")

ax.set_rticks([5000, 7000])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

fig.legend()

plt.show()

# useful for plotting Earth - Moon transfer orbit:
# https://stackoverflow.com/questions/25174644/elliptic-orbit-with-polar-method-tracing-phases-axes-and-earth-direction
