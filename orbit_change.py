import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
import numpy as np

np.set_printoptions(legacy="1.25")

# SOURCE: https://github.com/bryanwweber/orbital-mechanics-notes/blob/main/orbital-maneuvers/single-impulse-example.md?plain=1
# Shows how to construct orbits and arcs for transfers so I can plot them. Will modify to my use case.

R_E = 6378  # km
orbit_radius = 1000  # km
mu = 398_600  # km**3/s**2
theta = np.radians(35)
earth = Circle((0, 0), R_E, facecolor="paleturquoise", edgecolor="None")
orbit = Circle((0, 0), R_E + orbit_radius, facecolor="None", edgecolor="black")

e_2 = orbit_radius / (R_E + orbit_radius + R_E * np.cos(theta))
h_2 = np.sqrt((R_E + orbit_radius) * mu * (1 - e_2))
a = h_2**2 / mu / (1 - e_2**2)
b = a * np.sqrt(1 - e_2**2)
transfer = Arc(
    (R_E + orbit_radius - a, 0),
    2 * a,
    2 * b,
    theta2=np.degrees(np.pi - theta),
    edgecolor="red",
    linestyle="--",
)
A = (R_E + orbit_radius, 0)
B = (R_E * np.cos(np.pi - theta), R_E * np.sin(np.pi - theta))

fig, ax = plt.subplots(figsize=(7, 7))
plt.rc("font", size=20)
ax.set_aspect("equal")
ax.set_axis_off()
ax.set_clip_on(False)
ax.set_xlim(-R_E - orbit_radius * 2, R_E + orbit_radius * 2)
ax.set_ylim(-R_E - orbit_radius * 2, R_E + orbit_radius * 2)
ax.add_patch(earth)
ax.add_patch(orbit)
ax.add_patch(transfer)
ax.plot(*A, "ko")
ax.plot(*B, "ko")
ax.annotate(
    "Impulse", xy=A, xytext=(10, 10), textcoords="offset points", ha="left", va="center"
)
ax.annotate(
    "Impact", xy=B, xytext=(10, 10), textcoords="offset points", ha="left", va="top"
)
ax.annotate("Earth", xy=(0, -4000), ha="center", va="center")
ax.plot(
    [0, (R_E + orbit_radius + 500) * np.cos(np.pi - theta)],
    [0, (R_E + orbit_radius + 500) * np.sin(np.pi - theta)],
    color="black",
    lw=1,
)
ax.plot([0, R_E + orbit_radius + 500], [0, 0], color="black", lw=1)
ax.add_patch(Arc((0, 0), 2000, 2000, theta2=np.degrees(np.pi - theta)))
ann = (np.pi - theta) / 2
ax.annotate(
    f"{np.degrees(np.pi - theta):.0F}°", xy=(1250 * np.cos(ann), 1250 * np.sin(ann))
)

plt.show()
