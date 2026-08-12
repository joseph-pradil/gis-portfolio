"""
Post-Fire Vegetation Recovery - Gospers Mountain Fire, NSW (2019-2020)
Sentinel-2 dNBR burn severity + multi-year NDVI recovery trajectory.
Author: Joseph Pradil
"""

import ee
import geemap
import pandas as pd
import matplotlib.pyplot as plt

# ee.Authenticate()   # first run only, opens a browser
ee.Initialize(project="edenhazard")

# --- 1. Area of interest (Gospers Mountain scar, Wollemi NP, NSW) ---
aoi = ee.Geometry.Rectangle([150.2, -33.2, 150.9, -32.6])

# --- 2. Key dates ---
PRE_START,  PRE_END  = "2019-09-01", "2019-10-20"
POST_START, POST_END = "2020-02-01", "2020-03-31"

# --- 3. Cloud masking with Cloud Score+ ---
S2     = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
CSPLUS = ee.ImageCollection("GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED")
CS_BAND = "cs"
CLEAR_THRESH = 0.6

def mask_s2(img):
    return img.updateMask(img.select(CS_BAND).gte(CLEAR_THRESH))

def prep(start, end):
    return (S2.filterBounds(aoi)
              .filterDate(start, end)
              .linkCollection(CSPLUS, [CS_BAND])
              .map(mask_s2))

# --- 4. NBR + dNBR (burn severity) ---
def add_nbr(img):
    return img.addBands(img.normalizedDifference(["B8", "B12"]).rename("NBR"))

pre  = prep(PRE_START,  PRE_END ).map(add_nbr).median().clip(aoi)
post = prep(POST_START, POST_END).map(add_nbr).median().clip(aoi)
dnbr = pre.select("NBR").subtract(post.select("NBR")).rename("dNBR")

severity = (dnbr
    .where(dnbr.lt(0.10), 0)
    .where(dnbr.gte(0.10).And(dnbr.lt(0.27)), 1)
    .where(dnbr.gte(0.27).And(dnbr.lt(0.44)), 2)
    .where(dnbr.gte(0.44).And(dnbr.lt(0.66)), 3)
    .where(dnbr.gte(0.66), 4)
    .rename("severity"))

high_sev = dnbr.gte(0.44)

# --- 5. NDVI recovery trajectory (quarterly composites) ---
def quarterly_ndvi(year, month):
    start = ee.Date.fromYMD(year, month, 1)
    end   = start.advance(3, "month")
    ndvi  = (prep(start, end)
             .map(lambda i: i.normalizedDifference(["B8", "B4"]).rename("NDVI"))
             .median())
    stats = ndvi.updateMask(high_sev).reduceRegion(
        reducer=ee.Reducer.mean(), geometry=aoi, scale=100, maxPixels=1e9)
    return ee.Feature(None, {"date": start.format("YYYY-MM"),
                             "NDVI": stats.get("NDVI")})

quarters = [(y, m) for y in range(2019, 2024) for m in (1, 4, 7, 10)]
quarters = [(y, m) for (y, m) in quarters
            if not (y == 2019 and m < 7) and not (y == 2023 and m > 1)]

traj = ee.FeatureCollection([quarterly_ndvi(y, m) for (y, m) in quarters])

# --- 6. Pull to pandas + plot recovery curve ---
rows = traj.getInfo()["features"]
df = pd.DataFrame([f["properties"] for f in rows]).dropna()
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["date"], df["NDVI"], marker="o", linewidth=2)
ax.axvspan(pd.Timestamp("2019-10-26"), pd.Timestamp("2020-01-10"),
           color="red", alpha=0.12, label="Fire active")
ax.set_title("NDVI recovery in high-severity burn zone\nGospers Mountain fire, NSW")
ax.set_ylabel("Mean NDVI (high-severity zone)")
ax.set_xlabel("Date")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("outputs/ndvi_recovery_curve.png", dpi=150)
print("Saved outputs/ndvi_recovery_curve.png")
print(df.to_string(index=False))

# --- 7. Interactive map export ---
m = geemap.Map()
m.centerObject(aoi, 10)
m.addLayer(dnbr, {"min": -0.1, "max": 1.0,
                  "palette": ["0000ff", "ffffff", "ffff00", "ff8c00", "ff0000"]}, "dNBR")
m.addLayer(severity, {"min": 0, "max": 4,
                      "palette": ["1a9850", "d9ef8b", "fee08b", "fc8d59", "d73027"]}, "Burn severity")
m.addLayer(dnbr.updateMask(high_sev), {"palette": ["d73027"]}, "High-severity zone")
m.to_html("outputs/burn_severity_map.html")
print("Saved outputs/burn_severity_map.html")
