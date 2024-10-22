import kepler
import numpy as np

import matplotlib.pyplot as plt
import matplotlib_rc


def state_machine(e: dict, mean_anomalies: np.ndarray) -> None:
    """
    __init__ Solve Kepler's equation for the given mean anomaly
    range and update the inputted Keplerian elements.

    Parameters
    ----------
    oe_t0 : dict
        Classical orbital elements. Below elements:
        a = 8371[km], e = 0, i = 28.58◦, Ω = 90◦, ω = 0◦ , θ = 180◦
        Represented as:
        oe_t0 = {
                "a": 8371,
                "e": 0,
                "i": 28.58,
                "Omega": 90,
                "omega": 0,
                "true_anom": 180
                }

    mean_anomalies : list
        The range of mean anomalies to use as inputs to the solver.
    """
    eccentricity = e

    true_anomalies = []

    for mean_anomaly in mean_anomalies:
        true_anomalies.append(kepler.solve(mean_anomaly, eccentricity))

    return np.array(true_anomalies)


def calc_TOF(a, gravitational_parameter: float):
    # This is for a Hohmann transfer.
    return np.pi * np.sqrt((a**3) / gravitational_parameter)


def calc_mean_anomaly(
    t_0: float, tof: float, a, gravitational_parameter, finer_grain=False
):
    # NOTE: t_0 is time since periapsis.
    # Construct 11 steps for the inputted times.
    if finer_grain:
        time_array = np.linspace(t_0, t_0 + tof, 10000)
    else:
        time_array = np.arange(t_0, t_0 + tof, 11)

    # n is constant
    n = np.sqrt(gravitational_parameter / (a**3))

    # Return n-1 steps of Mean anomaly
    mean_anomalies = []

    for i, _ in enumerate(time_array):
        if i < len(time_array) - 1:
            # M = n(t-tp)
            mean_anomalies.append(n * (time_array[i + 1] - t_0) % (2 * np.pi))

    return np.array(mean_anomalies), time_array / 86400


def plot_anom_vs_time(time, anomaly):
    fig, ax = plt.subplots()
    ax.plot(time, anomaly)

    plt.show()


def calc_e(ra, rp):
    if ra != rp:
        return (ra - rp) / (ra + rp)
    else:
        return 0


def calc_orbital_period(a, gravitational_parameter):
    return 2 * np.pi * np.sqrt((a**3) / gravitational_parameter)


def plot_anomalies(x, mean, true, title, savepath):
    fig, ax = plt.subplots()
    ax.plot(x[0:-1], mean, label="$M$")
    ax.plot(x[0:-1], true, label="$E$")

    ax.legend()

    ax.set_xlabel("Time [days]")
    ax.set_ylabel("Anomaly, [rad]")
    ax.set_title(title)

    plt.savefig(savepath)


def earth_moon_transfer(mu_earth):
    a_transfer_arc = 163285.5

    tof_transfer_arc = calc_TOF(a_transfer_arc, mu_earth)
    print(f"Time of flight: {tof_transfer_arc}")
    mean_anomalies, times = calc_mean_anomaly(
        0, tof_transfer_arc, a_transfer_arc, mu_earth
    )

    true_anomalies = state_machine(
        e=calc_e(ra=318200, rp=8371), mean_anomalies=mean_anomalies
    )

    plot_anomalies(
        times,
        mean_anomalies,
        true_anomalies,
        "Earth to Moon transfer",
        "plots/earth_moon_transfer.pdf",
    )


def moon_lowering_transfer(mu_moon):
    a_transfer_arc = 61424

    # Moon SOI -> Moon final orbit transfer:
    tof_transfer_arc = calc_TOF(a_transfer_arc, mu_moon)
    print(f"Time of flight: {tof_transfer_arc}")
    mean_anomalies, times = calc_mean_anomaly(
        0, tof_transfer_arc, a_transfer_arc, mu_moon
    )

    true_anomalies = state_machine(
        e=calc_e(ra=66200, rp=4905), mean_anomalies=mean_anomalies
    )

    plot_anomalies(
        times,
        mean_anomalies,
        true_anomalies,
        "Moon SOI to final orbit transfer",
        "plots/moon_lowering_transfer.pdf",
    )


def lunar_orbit(mu_moon):
    a_lunar_orbit = 56648

    # 5 orbital periods:
    tof_orbit = 5 * calc_orbital_period(a_lunar_orbit, mu_moon)
    print(f"Time of 5 orbital periods: {tof_orbit}")
    mean_anomalies, times = calc_mean_anomaly(
        0, tof_orbit, a_lunar_orbit, mu_moon, finer_grain=True
    )

    true_anomalies = state_machine(e=0, mean_anomalies=mean_anomalies)

    plot_anomalies(
        times,
        mean_anomalies,
        true_anomalies,
        "Lunar orbit for 5 periods.",
        "plots/moon_orbit.pdf",
    )


def main():
    mu_earth = 398600
    mu_moon = 4905

    # Maneuvers from launch to parking orbit are instantaneous
    earth_moon_transfer(mu_earth)

    # Inclination change set to instantaneous
    moon_lowering_transfer(mu_moon)

    # Spacecraft now around moon.
    lunar_orbit(mu_moon)


if __name__ == main():
    main()
