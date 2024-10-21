import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams["figure.dpi"] = 250
mpl.rc("axes", labelsize=10, titlesize=16, linewidth=0.2)
mpl.rc("legend", fontsize=10)
mpl.rc("xtick", labelsize=12)
mpl.rc("xtick.major", size=2, width=0.5)
mpl.rc("xtick.minor", size=1, width=0.25, visible=True)
mpl.rc("ytick", labelsize=12)
mpl.rc("ytick.major", size=2, width=0.5)
mpl.rc("ytick.minor", size=1, width=0.25, visible=True)

# Font
plt.rc("font", family="serif")
plt.rc("text", usetex=True)
plt.rc("font", **{"serif": ["Times New Roman"]})

cos = np.cos
pi = np.pi


def calc_r(a, e, theta):
    return (a * (1 - e**2)) / (1 + e * cos(theta))


a_sat = 5137
e_sat = 0.3
theta = np.linspace(0, 2 * pi, 360)
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
