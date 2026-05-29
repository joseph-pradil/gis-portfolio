# GIS Portfolio — Joseph Pradil

Australian and New Zealand focused spatial analysis projects built with Python, ArcGIS, and PostGIS.

## About Me
GIS Analyst with experience in ArcGIS Pro, Python (arcpy/geopandas), SQL/PostGIS, and ArcGIS Online. 
Currently based in the US, open to opportunities in Australia 🇦🇺 and New Zealand 🇳🇿.

## Tech Stack
- **Python:** geopandas, rasterio, shapely, folium, numpy, pandas
- **GIS:** ArcGIS Pro, ArcGIS Online, Experience Builder, StoryMaps
- **Database:** PostGIS, SQL
- **Visualization:** folium, matplotlib, ArcGIS Dashboards

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

## Connect
- LinkedIn: https://www.linkedin.com/in/joseph-pradil-bolleddu-45277921a/
- Email: josephpradil@gmail.com
