# GIS Portfolio — Joseph Pradil

Australian and New Zealand focused spatial analysis projects built with Python, ArcGIS, Tableau, and PostGIS.

## About Me
GIS Analyst with experience in ArcGIS Pro, Python (arcpy/geopandas), SQL/PostGIS, and ArcGIS Online. 
Currently based in the US, open to opportunities in Australia 🇦🇺 and New Zealand 🇳🇿.

## Tech Stack
- **Python:** geopandas, rasterio, shapely, folium, numpy, pandas
- **GIS:** ArcGIS Pro, ArcGIS Online, Experience Builder, StoryMaps
- **Database:** PostGIS, SQL
- **Visualization:** Tableau, folium, matplotlib, ArcGIS Dashboards

## Projects

### Week 1 — Australian GIS Fundamentals
Core spatial operations applied to Australian cities and regions:
- Spatial data creation and visualization of Australian survey sites
- 500km buffer analysis around major Australian cities
- Population dissolve analysis by Australian state

### Week 2 — Interactive Web Mapping
- Built interactive folium map of Australian cities with population data
- Color coded markers by population size with custom legend
- Live Map: https://joseph-pradil.github.io/gis-portfolio/australia_map.html

### Project 1 — NSW Bushfire Consequence Model

A bushfire risk model for New South Wales that goes beyond "where do fires happen" to ask the question that actually matters: **where do fires threaten people?**

**Decision this supports:** Prioritising fire-mitigation resources and emergency planning — directing effort to where fire danger and population overlap, not just where fires are frequent.

**Why I built this:** I work in utility infrastructure in Los Angeles, a region that lives with wildfire every year. That experience taught me that a fire's true cost isn't measured by how often an area burns — it's measured by what's at stake when it does. I built this model to reflect that, using Australian data since I'm targeting GIS roles in Australia and NSW faces near-identical fire challenges to California.

**Method:**
1. Loaded 126 years of NSW fire history (37,588 recorded fires, 1900-2026)
2. Overlaid a 10km grid across the state and counted fire occurrences per cell (frequency)
3. Overlaid population data (Kontur, 517k hexagons) to measure exposure
4. Combined the two into a consequence score (fire risk x population) to find zones where danger and people overlap

**Key findings:**
- 2.6 million people live in Extreme fire-risk zones in NSW
- The highest-risk zones are also the most populated — fire danger concentrates exactly where people have built, not in empty bush
- The consequence model surfaces zones a frequency-only model would miss: one area with only moderate fire history but 380,000 residents ranks among the top consequence hotspots

**Data:** NSW NPWS Fire History; Kontur Population Australia 2023 (both open data)

- [Live Consequence Map](https://transcendent-sable-e6a8a6.netlify.app/nsw_bushfire_consequence.html)
- [View Code](https://github.com/joseph-pradil/gis-portfolio/blob/main/project1_nsw_bushfire_risk.ipynb)

**Limitations / next steps:** The frequency component is backward-looking. A production model would add vegetation/fuel type, slope, fire weather, and proximity-to-asset data. Population is residential only — it doesn't capture critical infrastructure or daytime/transient populations.

### Project 2 — Melbourne Urban Heat Island Analysis

A satellite-based heat map of inner Melbourne that asks not just **where is it hottest**, but **why** — by testing how surface temperature tracks vegetation cover, council by council.

**Decision this supports:** Targeting urban-cooling investment — tree canopy and reflective surfaces — to the councils that run hottest and have the least vegetation.

**Why I built this:** Coming from utility infrastructure in heat- and fire-prone California, I'm interested in how cities manage extreme heat — a growing issue for Australian urban planning. Surface temperature from satellite imagery is a direct, repeatable way to find a city's heat-vulnerable areas and make the case for where cooling investment (tree canopy, reflective surfaces) should go.

**Method:**
1. Pulled a clear summer Landsat 9 scene over Melbourne (3 Feb 2024) from USGS EarthExplorer
2. Converted the thermal band to land surface temperature in °C and clipped it to the 13 inner/middle-Melbourne councils
3. Calculated NDVI (vegetation index) from the red and near-infrared bands
4. Measured the correlation between vegetation and temperature across land surfaces (water masked out)
5. Computed mean surface temperature per council and ranked them — zonal statistics implemented directly from the raster

**Key findings:**
- Inner Melbourne's councils differ by ~3.5 °C in mean surface temperature on a single summer afternoon (34.1 °C to 37.6 °C)
- The hottest councils cluster in the more industrial northwest (Moonee Valley, Maribyrnong, Moreland); the coolest are the leafy southeast suburbs (Boroondara, Bayside, Stonnington)
- Surface temperature shows a moderate negative correlation with vegetation (r = −0.47) — greener areas are measurably cooler, confirming vegetation as one major driver of urban heat

**Data:** Landsat 9 Collection 2 Level-2 (USGS); ABS 2021 Local Government Area boundaries (both open data)

- [View Project & Maps](https://github.com/joseph-pradil/gis-portfolio/tree/main/02-melbourne-urban-heat)
- [View Code](https://nbviewer.org/github/joseph-pradil/gis-portfolio/blob/main/02-melbourne-urban-heat/notebooks/01_explore_temperature.ipynb)

**Limitations / next steps:** A single-date snapshot, not a multi-year climatology. Surface temperature is not air temperature — it runs hotter. A production version would average several summer scenes and overlay socioeconomic data to map heat *vulnerability*, not just heat.

### Project 3 — Greater Brisbane Flood Exposure Dashboard

An interactive dashboard quantifying how many people and homes sit in Brisbane's flood-risk zones — and which suburbs are most exposed.

**Decision this supports:** Prioritising flood-resilience investment and emergency planning — identifying which suburbs have the most people and dwellings exposed to high- and medium-likelihood flooding.

**Why I built this:** After the 2011 and 2022 floods, flood exposure is one of the most pressing planning questions in South-East Queensland. A hazard map alone shows where water goes, not who and what is in the way. This project joins flood-likelihood mapping to census population and dwelling counts to answer the question that drives investment: which suburbs have the most people and homes exposed, and at what likelihood.

**Method:**
1. Took Brisbane City Council's flood-likelihood layer (231,445 polygons) and dissolved it into four likelihood zones (High / Medium / Low / Very Low)
2. Joined ABS 2021 Census population (G01) and dwelling (G37) counts at suburb (SA2) level, filtered to Greater Brisbane (243 suburbs)
3. Estimated exposure by areal interpolation — apportioning each suburb's people and dwellings to flood zones by area
4. Built an interactive Tableau dashboard: exposure map, ranked suburb bar chart, and headline KPIs

**Key findings:**
- ~302,000 people and ~116,000 dwellings across Greater Brisbane sit within mapped flood-risk zones
- ~118,000 people are in high-likelihood zones specifically, concentrated in riverside and bayside suburbs
- The most-exposed suburbs — Newstead–Bowen Hills, Wynnum West–Hemmant, Nudgee–Banyo, West End, Boondall — are all recognisable Brisbane River corridor and bayside areas that flooded in 2011 and/or 2022

**Data:** Brisbane City Council Flood Awareness (Flood Risk Overall); ABS 2021 Census G01 & G37, SA2 level (both open data)

- [Live Interactive Dashboard (Tableau Public)](https://public.tableau.com/app/profile/joseph.bolleddu/viz/GreaterBrisbaneFloodExposure/Dashboard1)
- [View Project & Code](https://github.com/joseph-pradil/gis-portfolio/tree/main/03-queensland-flood)

**Limitations / next steps:** Exposure is estimated by areal interpolation, which assumes population is spread evenly within each suburb — so figures are estimates, not building-level counts. The flood layer gives likelihood, not depth, so it identifies who is exposed, not how severe the impact would be. A production version would use building-footprint data and overlay socioeconomic indicators to map flood *vulnerability*, not just exposure.

## Connect
- LinkedIn: https://www.linkedin.com/in/joseph-pradil-bolleddu-45277921a/
- Email: josephpradil@gmail.com
