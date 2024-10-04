"""
TASK:
Determine a sequence of impulsive manoeuvres to get from the initial launch vehicle state
(a = 5137 km, e = 0.3, i = 39◦, Ω = 90, ω = 270◦, θ0 = 160◦) to a circular parking orbit of
your design outside of requiring an inclination of i = 28.58◦.

SOLUTION:
We will use astropy for importing astronomical units and poliastro for orbit visualisations.

An inclination change is needed and for this, we should define a spacecraft.
We can look to the poliastro applying thrust example: https://docs.poliastro.space/en/stable/examples/Natural%20and%20artificial%20perturbations.html#Applying-thrust

"""

# matplotlib settings to make nice report plots
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

# Let's get a ballpark of times for our mission, looking at christmas and new years for fun

from astropy import units as u

from poliastro.bodies import Earth, Mars
from poliastro.plotting.porkchop import PorkchopPlotter
from poliastro.util import time_range

# launch_span = time_range("2024-12-01", end="2024-12-31")
# arrival_span = time_range("2024-12-01", end="2024-12-31")

launch_span = time_range("2005-04-30", end="2005-10-07")
arrival_span = time_range("2005-11-16", end="2006-12-21")

porkchop_plot = PorkchopPlotter(Earth, Mars, launch_span, arrival_span)
dv_dpt, dv_arr, c3dpt, c3arr, tof = porkchop_plot.porkchop()
