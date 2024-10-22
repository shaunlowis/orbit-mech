import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, Ellipse
import matplotlib_rc


# Useful functions can live here.
def calc_r(a, e, theta):
    return (a * (1 - e**2)) / (1 + e * np.cos(theta))


def calc_ellipse_focus(a, e):
    rp = a * (1 + e)
    return a - rp


def calc_xy_parametric(a, e, theta):
    r = calc_r(a, e, theta)
    return ((r * np.cos(theta)), (r * np.sin(theta)))


r_earth = 6378

a_init = 5137
e_init = 0.3
b_init = a_init * np.sqrt(1 - e_init**2)
theta_init = 180

# Initial polar coordinates:


# First burn target orbit:
a_burn = 6439.23
e_burn = 0.3
b_burn = a_burn * np.sqrt(1 - e_burn**2)


# Define our elements here:
earth = Circle((0, 0), r_earth, facecolor="darkseagreen", edgecolor="None")
starting_orbit = Ellipse(
    (calc_ellipse_focus(a_init, e_init), 0),
    2 * a_init,
    2 * b_init,
    facecolor="none",
    edgecolor="black",
)
# initial_position = Arc(
#     (calc_ellipse_focus(a_init, e_init), 0),
#     2 * a_init,
#     2 * b_init,
#     facecolor="none",
#     edgecolor="orange",
#     theta1=theta_init,
#     theta2=theta_init + 2,
#     linestyle="dotted",
#     linewidth=2,
# )

target_orbit = Ellipse(
    (calc_ellipse_focus(a_burn, e_burn), 0),
    2 * a_burn,
    2 * b_burn,
    facecolor="none",
    edgecolor="red",
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
ax.add_patch(target_orbit)
ax.plot([], [], c="red", label="Target orbit")
# ax.add_patch(initial_position)
initial_coordinates = calc_xy_parametric(a_init, e_init, theta_init)

ax.scatter(
    initial_coordinates[0],
    initial_coordinates[1],
    marker="x",
    c="orange",
    label="Inital position",
)

fig.legend()

ax.set_title("ECI frame, task 1.")

plt.show()
