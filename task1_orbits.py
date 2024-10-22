# Basic polar coordinates plot with orbit segment between two angles
import numpy as np
import matplotlib.pyplot as plt
import matplotlib_rc


def calc_r(a, e, theta):
    return (a * (1 - e**2)) / (1 + e * np.cos(theta))


def calc_transfer_e(ra, rb, theta_a, theta_b):
    return (rb - ra) / (ra * np.cos(theta_a) - rb * np.cos(theta_b))


def calc_a(ra, rb):
    return 0.5 * (ra + rb)


# Orbit parameters
a_sat = 5137
e_sat = 0.3
theta = np.linspace(0, 2 * np.pi, 360)
r_sat = calc_r(a_sat, e_sat, theta)

a_earth = 6378
e_earth = 0
r_earth = calc_r(a_earth, e_earth, theta)

a_parking = 8371
e_parking = 0
r_parking = calc_r(a_parking, e_parking, theta)

# Define angles in degrees and convert to radians
theta_a_deg = 160
theta_b_deg = 180
theta_a = np.deg2rad(theta_a_deg)
theta_b = np.deg2rad(theta_b_deg)

# Calculate r at these specific angles
ra_transfer = calc_r(a_sat, e_sat, theta_a_deg)
rb_transfer = calc_r(a_parking, e_parking, theta_b_deg)

# Slice theta and r between theta_a and theta_b
theta_segment = theta[(theta >= theta_a) & (theta <= theta_b)]
theta_segment = theta
r_segment = calc_r(
    calc_a(ra_transfer, rb_transfer),
    calc_transfer_e(ra_transfer, rb_transfer, theta_a, theta_b),
    theta_segment,
)  # Or use the orbit of interest

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "polar"})

# Full orbits
ax.plot(theta, r_earth, label="Earth, true scale")
ax.plot(theta, r_sat, label="Satellite launch orbit")
ax.plot(theta, r_parking, label="Satellite parking orbit")

# Orbit segment between theta_a and theta_b
# ax.plot(
#     theta_segment,
#     r_segment,
#     label=f"Orbit between {theta_a_deg}° and {theta_b_deg}°",
#     linestyle="--",
#     color="red",
# )

# Scatter points at theta_a and theta_b
ax.scatter(
    theta_a,
    ra_transfer,
    marker="x",
    label="Initial location",
    zorder=10,
    c="black",
    clip_on=False,
)
ax.scatter(
    theta_b,
    rb_transfer,
    marker="x",
    label="Parking location",
    zorder=10,
    c="grey",
    clip_on=False,
)

ax.set_rticks([5000, 7000, 9000])  # Adjust radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

fig.legend()
plt.savefig("plots/initial_parking.pdf")


# Alternative plotting tried here:

# import numpy as np
# import matplotlib.pyplot as plt

# # Create a polar plot
# fig, ax = plt.subplots(subplot_kw={"projection": "polar"})


# def calc_r(a, e, theta):
#     return (a * (1 - e**2)) / (1 + e * np.cos(theta))


# # Define radii for the orbits
# a_sat = 5137
# e_sat = 0.3
# r1 = calc_r(a_sat, e_sat, 160)

# a_earth = 6378
# e_earth = 0
# r2 = calc_r(a_earth, e_earth, 180)
# # r2 = 1.5  # Elliptical (approximation) orbit semi-major axis

# # Define start and end angles for the orbits and arc (in degrees)
# theta_start = 160  # Start angle of arc (in degrees)
# theta_end = 180  # End angle of arc (in degrees)

# # Convert angles to radians for plotting
# theta_start_rad = np.deg2rad(theta_start)
# theta_end_rad = np.deg2rad(theta_end)

# # Define theta range for the full circular orbits (0 to 360 degrees)
# theta = np.deg2rad(np.linspace(0, 360, 500))

# # Plot the circular orbit
# ax.plot(theta, np.full_like(theta, r1), label="Circular Orbit")

# # Plot the elliptical orbit approximation as a second circle (semi-major axis r2)
# ax.plot(theta, np.full_like(theta, r2), label="Elliptical Transfer Orbit")

# # Now create an arc to represent the transfer
# theta_arc = np.deg2rad(
#     np.linspace(theta_start, theta_end, 100)
# )  # arc from start to end angle
# r_arc = np.linspace(r1, r2, 100)  # transition between the orbits

# # Plot the arc (transfer)
# ax.plot(theta_arc, r_arc, color="red", label="Transfer Arc")

# # Add labels and legends
# ax.set_title("Polar Plot: Circular and Elliptical Transfer Orbit", va="bottom")
# ax.legend(loc="upper right")

# # Show the plot
# plt.show()
