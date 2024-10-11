import pytest
import numpy as np

# Constants
EARTH_RADIUS = 6371e3  # meters (average radius of Earth)


# Function to check if orbit intersects with the Earth
def check_orbit_collision(
    orbit_periapsis: int, orbit_apoapsis: int, earth_radius=EARTH_RADIUS
) -> bool:
    """
    Check if the satellite's orbit intersects with Earth.

    Parameters:
    - orbit_periapsis: Closest distance from Earth's center to satellite in meters.
    - orbit_apoapsis: Farthest distance from Earth's center to satellite in meters.
    - earth_radius: Earth's radius (default = 6371 km).

    Returns:
    - True if orbit intersects with Earth, False otherwise.
    """
    # If the periapsis (closest point) is less than the Earth's radius, there's a collision.
    if orbit_periapsis < earth_radius:
        return True
    return False


def check_vector_coincidence(vector_a: np.ndarray, vector_b: np.ndarray) -> bool:
    """
    This works because A⋅B = |A|*|B|*cos(t),
    where t is the angle between the two vectors, so (A⋅B)² = |A|² * |B|² * cos²(t).
    If the vectors are multiples of each other, then t is 0 or 180 degrees, and cos²(t) == 1.
    """
    return np.dot(vector_a, vector_b) * np.dot(vector_a, vector_b) == np.dot(
        vector_a, vector_a
    ) * np.dot(vector_b, vector_b)


def check_tangential_burn(orbital_elements_i: dict, orbital_elements_f: dict) -> bool:
    """
    check_tangential_burn
    tangential burns satisfy the following conditions:
        - do not change velocity orientation, just magnitude.
        - do not change the flight path angle

    Parameters
    ----------
    orbital_elements_i : dict
        Keplerian elements before burn
    orbital_elements_f : dict
        Keplerian elements after burn

    Returns
    -------
    bool
        _description_
    """
    # TODO: finish adding this test. Might be better to input velocities?
    vis_viva = np.sqrt()
    pass


def check_hohmann_conditions(v1: np.ndarray, v2: np.ndarray, v3: np.ndarray) -> bool:
    """
    check_hohmann_conditions
    Hohmann transfers satisfy the following conditions:
        - Manoeuvres occur at the apses.
        - Velocity at periapsis on the transfer arc is faster than the initial velocity of the starting orbit.
        - Velocity of the transfer arc is slower than the velocity of the target orbit
        - These should all be in-plane manoeuvres.

    Parameters
    ----------
    v1 : np.ndarray
        initial velocity of the starting orbit
    v2 : np.ndarray
        velocity of the transfer arc
    v3 : np.ndarray
        velocity of the target orbit.

    Returns
    -------
    bool
        _description_
    """
    return (v1 < v2 < v3) is True


# Pytest test cases
@pytest.mark.parametrize(
    "periapsis, apoapsis, expected",
    [
        (7000e3, 42000e3, False),  # Safe orbit (above Earth)
        (6000e3, 42000e3, True),  # Periapsis below Earth's surface (collision)
        (6371e3, 8000e3, False),  # Orbit skimming Earth's surface (no collision)
    ],
)
def test_check_orbit_collision(periapsis, apoapsis, expected):
    assert check_orbit_collision(periapsis, apoapsis) == expected
