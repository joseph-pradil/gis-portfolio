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

### Project 1 — NSW Bushfire Risk Model
A frequency-based bushfire risk model for New South Wales using 126 years of government fire history data.

**Method:** Overlaid a 10km grid across NSW, counted historical fire occurrences per cell using a spatial join, and classified each zone into Low/Medium/High/Extreme risk based on fire frequency.

**Data:** NSW NPWS Fire History (37,588 fires, 1900-2026)

**Key findings:** 244 extreme-risk zones identified, concentrated along the east coast ranges and Sydney basin. Total area burned across the record: 34.4 million hectares.

- [Live Risk Map](https://transcendent-sable-e6a8a6.netlify.app/nsw_bushfire_risk.html)
- [View Code](https://github.com/joseph-pradil/gis-portfolio/blob/main/project1_nsw_bushfire_risk.ipynb)

**Limitations / next steps:** Model is frequency-based (backward-looking). Future versions would incorporate vegetation type, slope, rainfall, and proximity to settlements for a forward-looking risk assessment.

## Connect
- LinkedIn: https://www.linkedin.com/in/joseph-pradil-bolleddu-45277921a/
- Email: josephpradil@gmail.com
