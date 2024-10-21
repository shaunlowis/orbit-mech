import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, Ellipse
import matplotlib_rc


# Useful functions can live here.
def calc_r(a, e, theta):
    return (a * (1 - e**2)) / (1 + e * np.cos(theta))


r_earth = 6378

a_sat = 5137
e_sat = 0.3
b_sat = a_sat * np.sqrt(1 - e_sat**2)

# Define our elements here:
earth = Circle((0, 0), r_earth, facecolor="darkseagreen", edgecolor="None")
starting_orbit = Ellipse(
    (-1541.1, 0), 2 * a_sat, 2 * b_sat, facecolor="none", edgecolor="black"
)
fig = plt.figure()

ax = fig.add_subplot(111, aspect="equal")

ax.set_clip_on(False)
ax.set_xlim(-r_earth * 2, r_earth * 2)
ax.set_ylim(-r_earth * 2, r_earth * 2)
ax.add_patch(earth)
ax.plot([], [], c="darkseagreen", label="Earth")
ax.add_patch(starting_orbit)
ax.plot([], [], c="black", label="Launch orbit")

fig.legend()

ax.set_title("ECI frame, task 1.")

plt.show()
