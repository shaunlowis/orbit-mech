import pytest

# Constants
EARTH_RADIUS = 6371e3  # meters (average radius of Earth)


# Function to check if orbit intersects with the Earth
def check_orbit_collision(orbit_periapsis, orbit_apoapsis, earth_radius=EARTH_RADIUS):
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
