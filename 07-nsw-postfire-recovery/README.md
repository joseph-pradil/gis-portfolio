# Post-Fire Vegetation Recovery Monitoring: Gospers Mountain Fire, NSW

A repeatable, zero-cost satellite workflow that tells asset owners and land managers **where and when to spend post-fire budget**, built on Sentinel-2 and Google Earth Engine.

## The decision this supports

After a megafire strips hundreds of thousands of hectares, utilities, insurers, councils and rehabilitation contractors face the same problem: finite crews and finite dollars against a burn scar too large to treat uniformly. Blanket-treating the whole area wastes money on land that is recovering on its own. Ignoring it lets fuel load and vegetation re-accumulate under powerlines and rebuild ignition risk.

The question is not "did the bush recover." It is:

- **Which areas are regrowing fast enough** to re-threaten powerline clearances or rebuild fuel load, and therefore need re-prioritised inspection and vegetation-management cycles?
- **Which areas are recovering slowly or not at all**, flagging erosion, landslide exposure on bare slopes, or a need for active revegetation spend?

This workflow answers both, spatially and over time, from free imagery, so spend can be targeted instead of spread thin.

## Who uses this and for what

- **Network utilities** (Essential Energy, Endeavour Energy in NSW; Vector, Powerco in NZ): re-sequence line-clearance and vegetation-management inspections toward fast-regrowth zones near assets. This is the same class of analysis behind utility vegetation and ignition-risk programs, which is my day-to-day domain.
- **Insurers and reinsurers**: re-rate wildfire risk as fuel load re-accumulates. Recovery rate is a leading indicator of when a burned area stops being low risk.
- **Councils and land managers** (clients of Tonkin + Taylor, GHD and similar): direct rehabilitation budget to stalled-recovery areas and monitor revegetation against targets.

## Study area and event

Gospers Mountain fire, Wollemi National Park, NSW. Ignited around 26 October 2019, contained early January 2020, roughly 512,000 hectares burnt. The largest forest fire from a single ignition point in Australian history and a defining Black Summer event. It sits directly north of the region in my NSW Bushfire Consequence project.

## Findings, as decision inputs

NDVI (a standard greenness index) tracked across the high-severity burn zone, quarterly:

| Moment | NDVI | Read |
| --- | --- | --- |
| Pre-fire (Jul 2019) | 0.78 | Healthy baseline |
| Trough (Jan 2020) | 0.29 | 63% loss of green cover at peak impact |
| First rebound (Apr 2020) | 0.54 | Rapid regrowth, one quarter after containment |
| Recovered (Apr 2022) | 0.82 | Back to pre-fire levels |

Decision-relevant takeaways:

- High-severity zone: roughly 1218 km2, 27.9% of the study area**. This footprint carries the return-of-risk.
- Recovery to pre-fire green cover took about **2.25 years (9 quarters)**. For a utility, that is the window in which clearance risk under lines rebuilds. Inspection cycles in this zone should tighten well before the two-year mark, not after.
- The fast Apr 2020 rebound, 0.29 to 0.54 in a single quarter, signals early vigorous regrowth typical of eucalypt fire response. Fuel load and clearance risk return faster than a naive "recovery takes years" assumption implies. That is the operational headline.

## Operationalising it

This is a template, not a one-off. Point it at any fire perimeter and it returns the same severity map and recovery curve. Run quarterly, it becomes a monitoring layer: a utility or council can watch recovery per management zone and trigger action when a zone crosses a chosen NDVI threshold. Swapping the bounding box for an official fire-extent polygon tightens the numbers for reporting.

## Data

- Sentinel-2 Surface Reflectance (COPERNICUS/S2_SR_HARMONIZED), 10 to 20 m.
- Cloud Score+ (GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED) for cloud masking.
- Optional: official fire-extent polygon from the NSW RFS or DPE fire-history layer to replace the bounding-box AOI with the true burn perimeter.

All data is accessed in the cloud through Earth Engine. Nothing is downloaded.

## Method

1. Build cloud-masked pre-fire and post-fire Sentinel-2 median composites.
2. Compute the Normalised Burn Ratio (NBR) for each and derive dNBR as the difference.
3. Classify dNBR into USGS burn-severity classes and isolate the high-severity zone (dNBR >= 0.44).
4. Build quarterly NDVI composites from mid-2019 to early 2023, masked to the high-severity zone.
5. Reduce each to a mean and chart the recovery trajectory.

## Outputs

- `outputs/ndvi_recovery_curve.png`: the recovery trajectory chart.
- `outputs/burn_severity_map.html`: an interactive dNBR and severity map, hostable as a live demo.

## Tools

Google Earth Engine (Python API), geemap, pandas, matplotlib. A Code Editor JavaScript version is included for quick visual inspection.

## How to run

```bash
pip install -r requirements.txt
python3 -c "import ee; ee.Authenticate()"   # first run only
python3 postfire_recovery.py
```

Set your GEE project id in `postfire_recovery.py` before running.

## Interview talking points

- Lead with the decision, not the index. This workflow exists to target post-fire spend, and the recovery curve is the trigger signal.
- The utility connection: recovery rate equals return of vegetation-contact and fuel-load risk, which is the core of utility vegetation management and my SoCalGas domain.
- Why free and repeatable matters commercially: no licence, cloud-processed, rerunnable on any perimeter, so it scales across a whole network's fire exposure at near-zero marginal cost.
- Honest limits: NDVI is a proxy for greenness, not fuel structure. A bounding-box AOI slightly overcounts. Pairing this with LiDAR canopy height would turn "green is back" into "clearance is breached," which is the natural next build.
