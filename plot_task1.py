"""
TASK:
Determine a sequence of impulsive manoeuvres to get from the initial launch vehicle state
(a = 5137 km, e = 0.3, i = 39◦, Ω = 90, ω = 270◦, θ0 = 160◦) to a circular parking orbit of
your design outside of requiring an inclination of i = 28.58◦.

SOLUTION:
We will use rebound, an n-body integrator to visualise our orbit.
https://rebound.readthedocs.io/en/latest/

Note: all angles are in radians.

TODO: Update these plots to show the maneuvers calculated for task1.
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

import numpy as np
import rebound

global m_per_AU
m_per_AU = 149597870700


def earth_moon_sat_init(sim_obj: rebound.Simulation):
    # We can retrieve Earth and Moon parameters from NASA Horizons
    sim_obj.add("Earth")

    # Now add the Moon, specify this NAIF ID, otherwise it matches Earth
    # https://ssd.jpl.nasa.gov/horizons/app.html#/
    # https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/MATLAB/req/naif_ids.html#Planets%20and%20Satellites
    # https://rebound.readthedocs.io/en/latest/ipython_examples/Horizons/#adding-particles-using-nasa-jpl-horizons-system
    sim_obj.add(
        "301",
        primary=sim_obj.particles[0],  # specify the Earth is the primary
    )

    # Now our spacecraft: (a = 5137 km, e = 0.3, i = 39◦, Ω = 90, ω = 270◦, θ0 = 160◦)
    # We omit the mass argument for our satellite. Docs: https://rebound.readthedocs.io/en/latest/orbitalelements/
    # specify the Earth is the primary
    sim_obj.add(
        primary=sim_obj.particles[0],  # specify the Earth is the primary
        # a=(5137 * 10**3) / m_per_AU,  # semi-major axis [au]
        a=5137 * 10**3,  # semi-major axis [m]
        e=0.3,  # eccentricity
        inc=np.radians(39),  # inclination [rad]
        Omega=np.radians(90),  # longitude of ascending node [rad]
        omega=np.radians(270),  # argument of pericenter [rad]
        f=np.radians(160),  # true anomaly [rad]
    )


def earth_sat_init(sim_obj: rebound.Simulation):
    """
    earth_sat_init Refer to earth_moon_sat_init for more information.

    Parameters
    ----------
    sim_obj : rebound.Simulation
        The simulation object, a new one should be created unless specified otherwise.
    """
    sim_obj.add("Earth")
    sim_obj.add(
        primary=sim_obj.particles[0],  # specify the Earth is the primary
        # a=(5137 * 10**3) / m_per_AU,  # semi-major axis [au]
        a=5137 * 10**3,  # semi-major axis [m]
        e=0.3,  # eccentricity
        inc=np.radians(39),  # inclination [rad]
        Omega=np.radians(90),  # longitude of ascending node [rad]
        omega=np.radians(270),  # argument of pericenter [rad]
        f=np.radians(160),  # true anomaly [rad]
    )


def earth_sat_inc_burn(sim_obj: rebound.Simulation):
    sim_obj.add("Earth")
    # Initial satellite orbit
    sim_obj.add(
        primary=sim_obj.particles[0],  # specify the Earth is the primary
        # a=(5137 * 10**3) / m_per_AU,  # semi-major axis [au]
        a=5137 * 10**3,  # semi-major axis [m]
        e=0.3,  # eccentricity
        inc=np.radians(39),  # inclination [rad]
        Omega=np.radians(90),  # longitude of ascending node [rad]
        omega=np.radians(270),  # argument of pericenter [rad]
        f=np.radians(160),  # true anomaly [rad]
    )

    # Orbit with the desired inclination
    sim_obj.add(
        primary=sim_obj.particles[0],  # specify the Earth is the primary
        # a=(5137 * 10**3) / m_per_AU,  # semi-major axis [au]
        a=5137 * 10**3,  # semi-major axis [m]
        e=0.3,  # eccentricity
        inc=np.radians(28.58),  # inclination [rad]
        Omega=np.radians(90),  # longitude of ascending node [rad]
        omega=np.radians(270),  # argument of pericenter [rad]
        f=np.radians(160),  # true anomaly [rad]
    )


def earth_sat_inc_circ_burn(sim_obj: rebound.Simulation):
    sim_obj.add("Earth")

    # Initial satellite orbit
    sim_obj.add(
        primary=sim_obj.particles[0],  # specify the Earth is the primary
        # a=(5137 * 10**3) / m_per_AU,  # semi-major axis [au]
        a=5137 * 10**3,  # semi-major axis [m]
        e=0.3,  # eccentricity
        inc=np.radians(39),  # inclination [rad]
        Omega=np.radians(90),  # longitude of ascending node [rad]
        omega=np.radians(270),  # argument of pericenter [rad]
        f=np.radians(160),  # true anomaly [rad]
    )

    # Orbit with the desired inclination
    sim_obj.add(
        primary=sim_obj.particles[0],  # specify the Earth is the primary
        # a=(5137 * 10**3) / m_per_AU,  # semi-major axis [au]
        a=5137 * 10**3,  # semi-major axis [m]
        e=0.3,  # eccentricity
        inc=np.radians(28.58),  # inclination [rad]
        Omega=np.radians(90),  # longitude of ascending node [rad]
        omega=np.radians(270),  # argument of pericenter [rad]
        f=np.radians(160),  # true anomaly [rad]
    )

    # Circular parking orbit with the desired inclination
    sim_obj.add(
        primary=sim_obj.particles[0],  # specify the Earth is the primary
        # a=(5137 * 10**3) / m_per_AU,  # semi-major axis [au]
        a=5137 * 10**3,  # semi-major axis [m]
        e=0,  # eccentricity
        inc=np.radians(28.58),  # inclination [rad]
        Omega=np.radians(90),  # longitude of ascending node [rad]
        omega=np.radians(270),  # argument of pericenter [rad]
        f=np.radians(160),  # true anomaly [rad]
    )


def plot_rebound_sim(sim_obj: rebound.Simulation, title: str = "", savename: str = ""):
    op = rebound.OrbitPlotSet(
        sim_obj,
        slices=0.7,
        figsize=(10, 10),
        unitlabel="[m]",
        color=True,
        show_primary=True,
    )
    op.fig.suptitle(title)
    op.fig.savefig(savename)


def init_sim_obj() -> rebound.Simulation:
    """
    We set G to SI units, see here: https://rebound.readthedocs.io/en/latest/units/#__tabbed_3_2

    From the docs:
    ''From now on, all quantities that have unit of length need to be specified in meters.
    All quantities that have units of time need to be specified in seconds.
    All quantities that have units of mass need to be specified in kg.
    All quantities that have units of velocity need to be specified in meters per second.
    And so on.''"""
    sim = rebound.Simulation()
    sim.G = 6.6743e-11  # m^3 / kg s^2
    sim.units = ("m", "s", "kg")

    return sim


def main():
    sim = init_sim_obj()
    earth_moon_sat_init(sim)
    plot_rebound_sim(
        sim,
        title="Earth-Moon-satellite system\n before any impulsive maneuvers.\n[barycentric coordinates]",
        savename="plots/task1/initial_earth_moon_sat_orbit.png",
    )

    sim = init_sim_obj()
    earth_sat_init(sim)
    plot_rebound_sim(
        sim,
        title="Earth-satellite system\n before any impulsive maneuvers.\n[barycentric coordinates]",
        savename="plots/task1/initial_earth_sat_orbit.png",
    )

    sim = init_sim_obj()
    earth_sat_inc_burn(sim)
    plot_rebound_sim(
        sim,
        title="Earth-satellite system\n after inclination change burn.\n[barycentric coordinates]",
        savename="plots/task1/earth_sat_inc_burn.png",
    )

    sim = init_sim_obj()
    earth_sat_inc_circ_burn(sim)
    plot_rebound_sim(
        sim,
        title="Earth-satellite system\n in circular parking orbit.\n[barycentric coordinates]",
        savename="plots/task1/earth_sat_parking.png",
    )


if __name__ == main():
    main()
