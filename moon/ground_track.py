import glob, os, requests, random, pytz

import datetime
# from datetime import datetime
from dateutil.relativedelta import relativedelta

from bs4 import BeautifulSoup
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl
from skyfield.api import load, wgs84

import cartopy.crs as ccrs


ts = load.timescale()
tz = pytz.timezone("UTC")
dt = tz.localize(datetime.utcnow())

t0 = ts.utc(dt)
t1 = ts.utc(dt + relativedelta(minutes=200))
timescales = ts.linspace(t0, t1, 101)

geocentrics = satellite[-1].at(timescales)
subpoints = wgs84.subpoint_of(geocentrics)

proj = ccrs.Robinson()
fig, ax = plt.subplots(
    1, figsize=(20, 22), sharey=True, subplot_kw=dict(projection=proj)
)

coordinates = pd.DataFrame()
coordinates["lons"] = subpoints.longitude.degrees
coordinates["lats"] = subpoints.latitude.degrees

ax.set_global()

ax.stock_img()
ax.coastlines()

ax.scatter(
    coordinates["lons"].values,
    coordinates["lats"].values,
    color="red",
    marker="x",
    transform=ccrs.PlateCarree(),
    s=25,
    linewidth=3,
)

plt.title("Geocentric coordinates during last 200min of TLE", fontsize=18)
plt.tight_layout()
plt.show()