# GIS Portfolio — Joseph Pradil

Australian and New Zealand focused spatial analysis projects built with Python and Tableau.

## About Me
Spatial analyst with utility-infrastructure experience and advanced Python-based geospatial analytics. I work in utility network and asset GIS, and build decision-support analyses for hazard, exposure, and infrastructure-resilience problems. Currently based in the US, open to opportunities in Australia 🇦🇺 and New Zealand 🇳🇿.

## Tech Stack
- **Python:** geopandas, rasterio, shapely, folium, osmnx, networkx, numpy, pandas
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

**Decision this supports:** Prioritising fire-mitigation resources and emergency planning, directing effort to where fire danger and population overlap rather than just where fires are frequent.

**Why I built this:** I work in utility infrastructure in Los Angeles, a region that lives with wildfire every year. That experience taught me that a fire's true cost isn't measured by how often an area burns; it's measured by what's at stake when it does. I built this model to reflect that, using Australian data since I'm targeting GIS roles in Australia and NSW faces near-identical fire challenges to California.

**Method:**
1. Loaded 126 years of NSW fire history (37,588 recorded fires, 1900-2026)
2. Overlaid a 10km grid across the state and counted fire occurrences per cell (frequency)
3. Overlaid population data (Kontur, 517k hexagons) to measure exposure
4. Combined the two into a consequence score (fire risk x population) to find zones where danger and people overlap

**Key findings:**
- 2.6 million people live in Extreme fire-risk zones in NSW
- The highest-risk zones are also the most populated. Fire danger concentrates exactly where people have built, not in empty bush
- The consequence model surfaces zones a frequency-only model would miss: one area with only moderate fire history but 380,000 residents ranks among the top consequence hotspots

**Recommendation:** The model flags the Sydney metropolitan bushland-urban interface, the northern (Hornsby–Ku-ring-gai), southern (Sutherland), and south-western suburbs where dense population abuts fire-prone bush, plus Greater Newcastle, as the highest-consequence priorities for fuel-reduction, evacuation-route planning, and asset-hardening investment. Notably, it elevates a moderate-frequency southern-Sydney zone holding ~380,000 residents into the top tier: a hotspot a frequency-only map would overlook, but one where the scale of exposed population makes mitigation critical.

**Data:** NSW NPWS Fire History; Kontur Population Australia 2023 (both open data)

- [Live Consequence Map](https://transcendent-sable-e6a8a6.netlify.app/nsw_bushfire_consequence.html)
- [View Code](https://github.com/joseph-pradil/gis-portfolio/blob/main/01-nsw-bushfire/project1_nsw_bushfire_risk.ipynb)

**Limitations / next steps:** The frequency component is backward-looking. A production model would add vegetation/fuel type, slope, fire weather, and proximity-to-asset data. Population is residential only, so it doesn't capture critical infrastructure or daytime/transient populations.

### Project 2 — Melbourne Urban Heat Island Analysis

A satellite-based heat map of inner Melbourne that asks not just **where is it hottest**, but **why**, by testing how surface temperature tracks vegetation cover, council by council.

**Decision this supports:** Targeting urban-cooling investment (tree canopy and reflective surfaces) to the councils that run hottest and have the least vegetation.

**Why I built this:** Coming from utility infrastructure in heat- and fire-prone California, I'm interested in how cities manage extreme heat, a growing issue for Australian urban planning. Surface temperature from satellite imagery is a direct, repeatable way to find a city's heat-vulnerable areas and make the case for where cooling investment (tree canopy, reflective surfaces) should go.

**Method:**
1. Pulled a clear summer Landsat 9 scene over Melbourne (3 Feb 2024) from USGS EarthExplorer
2. Converted the thermal band to land surface temperature in °C and clipped it to the 13 inner/middle-Melbourne councils
3. Calculated NDVI (vegetation index) from the red and near-infrared bands
4. Measured the correlation between vegetation and temperature across land surfaces (water masked out)
5. Computed mean surface temperature per council and ranked them, with zonal statistics implemented directly from the raster

**Key findings:**
- Inner Melbourne's councils differ by ~3.5 °C in mean surface temperature on a single summer afternoon (34.1 °C to 37.6 °C)
- The hottest councils cluster in the more industrial northwest (Moonee Valley, Maribyrnong, Moreland); the coolest are the leafy southeast suburbs (Boroondara, Bayside, Stonnington)
- Surface temperature shows a moderate negative correlation with vegetation (r = −0.47): greener areas are measurably cooler, confirming vegetation as one major driver of urban heat

**Recommendation:** Cooling investment (street-tree canopy, reflective and permeable surfaces, green space) should be directed first at the northwest councils (Moonee Valley, Maribyrnong, Moreland), which run hottest precisely because they are the least vegetated. The vegetation–temperature relationship gives councils a measurable, repeatable target: raising canopy cover in these areas is the most direct lever on surface heat.

**Data:** Landsat 9 Collection 2 Level-2 (USGS); ABS 2021 Local Government Area boundaries (both open data)

- [View Project & Maps](https://github.com/joseph-pradil/gis-portfolio/tree/main/02-melbourne-urban-heat)
- [View Code](https://nbviewer.org/github/joseph-pradil/gis-portfolio/blob/main/02-melbourne-urban-heat/notebooks/01_explore_temperature.ipynb)

**Limitations / next steps:** A single-date snapshot, not a multi-year climatology. Surface temperature is not air temperature; it runs hotter. A production version would average several summer scenes and overlay socioeconomic data to map heat *vulnerability*, not just heat.

### Project 3 — Greater Brisbane Flood Exposure Dashboard

An interactive dashboard quantifying how many people and homes sit in Brisbane's flood-risk zones, and which suburbs are most exposed.

**Decision this supports:** Prioritising flood-resilience investment and emergency planning, identifying which suburbs have the most people and dwellings exposed to high- and medium-likelihood flooding.

**Why I built this:** After the 2011 and 2022 floods, flood exposure is one of the most pressing planning questions in South-East Queensland. A hazard map alone shows where water goes, not who and what is in the way. This project joins flood-likelihood mapping to census population and dwelling counts to answer the question that drives investment: which suburbs have the most people and homes exposed, and at what likelihood.

**Method:**
1. Took Brisbane City Council's flood-likelihood layer (231,445 polygons) and dissolved it into four likelihood zones (High / Medium / Low / Very Low)
2. Joined ABS 2021 Census population (G01) and dwelling (G37) counts at suburb (SA2) level, filtered to Greater Brisbane (243 suburbs)
3. Estimated exposure by areal interpolation, apportioning each suburb's people and dwellings to flood zones by area
4. Built an interactive Tableau dashboard: exposure map, ranked suburb bar chart, and headline KPIs

**Key findings:**
- ~302,000 people and ~116,000 dwellings across Greater Brisbane sit within mapped flood-risk zones
- ~118,000 people are in high-likelihood zones specifically, concentrated in riverside and bayside suburbs
- The most-exposed suburbs (Newstead–Bowen Hills, Wynnum West–Hemmant, Nudgee–Banyo, West End, Boondall) are all recognisable Brisbane River corridor and bayside areas that flooded in 2011 and/or 2022

**Recommendation:** Flood-resilience spending (property-level mitigation, drainage upgrades, evacuation planning, and revised building controls) should be prioritised in the high-likelihood riverside and bayside suburbs the dashboard ranks at the top (Newstead–Bowen Hills, Wynnum West–Hemmant, Nudgee–Banyo, West End, Boondall). Presenting exposure as a ranked, filterable dashboard lets a council or insurer triage limited budget to the suburbs where the most people and dwellings sit in the most likely flood zones.

**Data:** Brisbane City Council Flood Awareness (Flood Risk Overall); ABS 2021 Census G01 & G37, SA2 level (both open data)

- [Live Interactive Dashboard (Tableau Public)](https://public.tableau.com/app/profile/joseph.bolleddu/viz/GreaterBrisbaneFloodExposure/Dashboard1)
- [View Project & Code](https://github.com/joseph-pradil/gis-portfolio/tree/main/03-queensland-flood)

**Limitations / next steps:** Exposure is estimated by areal interpolation, which assumes population is spread evenly within each suburb, so figures are estimates rather than building-level counts. A production model would use dasymetric mapping, masking unpopulated land with land-use zones or building footprints (e.g. Microsoft's open building footprints) before distributing census counts, to avoid overestimating exposure where a flood zone hits the empty part of a large suburb. The flood layer also gives likelihood, not depth, so it identifies who is exposed, not how severe the impact would be.

### Project 4 — Victorian Flood Road-Access Analysis

A road-network connectivity analysis of the Rochester–Echuca region: when a major flood hits, which towns lose road access and how does the network break apart?

**Decision this supports:** Prioritising road-resilience investment and emergency planning, identifying which communities get isolated in a major flood and where the network's critical weak points are.

**Why I built this:** In October 2022 Rochester was cut off and evacuated when the Campaspe River flooded. A hazard map shows where water goes; for emergency planning the sharper question is which communities get isolated, a road-network connectivity question rather than a hazard-mapping one. So this project models the actual road network and tests what happens to it under flood.

**Method:**
1. Pulled the drivable road network for the Rochester–Echuca corridor from OpenStreetMap (OSMnx): 2,449 intersections, 6,107 road segments, modelled as a graph
2. Overlaid Victoria's 1% AEP (1-in-100-year) flood extent, the statutory floodplain layer used in Victorian planning schemes
3. Identified and removed flooded road segments (31% of the network), then ran shortest-path and connectivity analysis on the damaged graph
4. Determined which towns lose access to the regional centre (Echuca) and how the network fragments

**Key findings:**
- All four surrounding towns (Rochester, Elmore, Lockington, Kyabram) lose road access to Echuca in a 1% flood
- The flood fragments the network into isolated pockets: the major towns end up in separate zones that cannot reach one another
- The modelled isolation reproduces the real access collapse of the 2022 floods, providing independent validation

**Recommendation:** Because every studied town loses its connection to Echuca, road-resilience investment should focus on securing at least one all-weather access route per community (through bridge-raising, road-embankment works, or designated flood-evacuation corridors) rather than spreading effort evenly. The fragmentation result also makes the case for pre-positioning emergency supplies and services within each isolated pocket, since cross-region resupply by road cannot be relied on during a major flood.

**Data:** OpenStreetMap road network (via OSMnx); Victorian Government 1% AEP flood extent (both open data)

- [View Project, Maps & Code](https://github.com/joseph-pradil/gis-portfolio/tree/main/04-victoria-road-access)

**Limitations / next steps:** "Cut off" is defined at the level of the modelled drivable network intersecting the flat 2D flood extent, so it doesn't account for flood depth, timing, or high-clearance vehicles. A more robust pipeline would intersect the road network with a flood-depth raster and remove roads only where water depth exceeds a critical threshold (e.g. >0.3 m, where standard vehicles lose traction), and rank individual roads and bridges by criticality to pinpoint the highest-priority resilience investments.

### Project 5 — Wellington Road-Network Criticality (Seismic Access)

A network-criticality analysis of earthquake-prone Wellington: which individual roads, if damaged, would most degrade the population's access to hospital, and so should be hardened first?

**Decision this supports:** Prioritising seismic road-resilience investment, identifying the specific roads whose failure imposes the greatest access burden, so bridge-strengthening and route-hardening target the highest-impact links first.

**Why I built this:** Earthquakes are New Zealand's defining hazard, and Wellington's constrained geography funnels road access through a few corridors. After a major quake the question isn't just what's damaged, but which damaged road hurts most, a network-criticality question. This project also delivers the "rank roads by criticality" extension flagged as a next step in Project 4, applied to NZ's signature hazard.

**Method:**
1. Pulled Wellington City's drivable road network from OpenStreetMap (OSMnx): 4,445 intersections, 9,850 road segments
2. Assigned 2023 NZ Census population (205,035 people across 88 SA2 areas) to network nodes
3. For each of 1,628 major road links, removed it and measured the population-weighted increase in travel distance to Wellington Hospital (person-km of added detour), a detour-weighted criticality score
4. Ranked roads by total added burden and mapped the result

**Key findings:**
- Wellington's major road network is largely redundant (only ~700 of 1,628 links cause any added travel burden when removed) but criticality is highly concentrated in a few roads
- The northern motorway lifeline (Johnsonville–Porirua / Transmission Gully) is the single most critical route, with no genuine alternative for northern access
- Adelaide Road, the arterial spine to the hospital itself, carries the highest aggregate criticality, making the hospital approach a key vulnerability; single-access hill suburbs (Karori, Newlands) also rank high

**Recommendation:** Seismic-hardening investment should concentrate on the small set of high-criticality roads rather than spread evenly. The clear priorities are the northern motorway lifeline and Adelaide Road (the hospital approach), followed by single-access hill-suburb arterials. Because the network is otherwise redundant, targeted strengthening of these few links delivers far more resilience per dollar than uniform investment.

**Data:** OpenStreetMap road network (via OSMnx); 2023 Census usually-resident population by SA2 (Stats NZ) (both open data)

- [View Project, Maps & Code](https://github.com/joseph-pradil/gis-portfolio/tree/main/05-wellington-seismic-access)

**Limitations / next steps:** Criticality is measured to a single destination (Wellington Hospital); the person-km figures are indicative rather than precise (aggregating across a road's segments slightly over-counts). A fuller analysis would test multiple destinations and model simultaneous failure of all roads crossing the Wellington Fault rupture zone, weighted by each link's actual seismic-failure likelihood.

### Project 6 — Auckland Compound Hazard (Flood + Landslide Overlap)

A multi-hazard overlay for Auckland: where do flood and landslide risk overlap, and how many people live on that double-jeopardy land that single-hazard maps miss?

**Decision this supports:** Prioritising resilience investment and planning scrutiny for communities facing *compound* hazard, land exposed to both flooding and landslides that a flood map alone, or a landslide map alone, would never flag.

**Why I built this:** The 2023 Auckland Anniversary floods and Cyclone Gabrielle struck with both flooding and landslides, the latter triggering ~50,000 slips, NZ's largest landslide event on record. Auckland now maps both hazards (feeding LIM reports and Plan Change 120 consent rules) but assesses them separately. The places where they coincide are exactly the terrain that failed in 2023, yet they fall through the cracks of single-hazard planning. This project overlays the two to surface that blind spot.

**Method:**
1. Took Auckland Council's current 1% AEP flood plains (12,670 polygons, predominantly post-2023 modelling), dissolved into a flood zone
2. Pulled the 2025 region-wide Large-Scale Landslide Susceptibility layer (TR2025/7) via the council's ArcGIS REST API (86,475 polygons), filtered to High + Very High and dissolved
3. Intersected the two to isolate the compound (both-hazard) zone
4. Estimated population in each zone by areal interpolation from 2023 NZ Census SA2 data (~1.72M Auckland population)

**Key findings:**
- ~194,000 Aucklanders live in the flood zone and ~102,000 in the high-landslide zone, but only ~5,600 live in the compound zone where both overlap
- The small overlap is the point: flood-prone (flat) and landslide-prone (steep) land are mostly different terrain, so these ~5,600 people are systematically invisible to single-hazard planning. A flood map doesn't flag them, and neither does a landslide map
- The compound population concentrates in West and North Auckland's hill-and-gully suburbs (Western Heights, Bayview, Massey, Glen Eden, Stillwater, Papakura East), the same terrain hit hardest in 2023

**Recommendation:** The compound zone should be treated as a distinct planning category rather than left to fall between two separately-administered hazard layers. The ~5,600 people in West and North Auckland's overlap suburbs warrant prioritised attention: combined flood-and-slope geotechnical assessment, stricter consent scrutiny, and targeted stormwater and slope-stabilisation works. Overlaying existing official hazard layers is a low-cost way for a council to surface this blind spot from data it already holds.

**Data:** Auckland Council flood plains & Large-Scale Landslide Susceptibility (TR2025/7, via ArcGIS REST API); 2023 Census population by SA2 (Stats NZ) (all open data)

- [View Project, Maps & Code](https://github.com/joseph-pradil/gis-portfolio/tree/main/06-auckland-flood)

**Limitations / next steps:** Population is estimated by areal interpolation (people assumed evenly spread within each SA2), so the compound figure is an estimate rather than a building-level count. The analysis uses large-scale landslide susceptibility; the shallow-landslide layer (which dominated the 2023 slips) is a separate official dataset a refined version would also overlay. Susceptibility indicates where landslides are more likely, not that they will occur. A natural extension would add coastal inundation for a three-hazard analysis and overlay socioeconomic data to map compound *vulnerability*.

### Project 7 — Post-Fire Vegetation Recovery Monitoring (NSW)

A satellite-based recovery tracker for the Gospers Mountain megafire: where did the fire burn worst, and how fast do vegetation, fuel load and ignition risk grow back?

**Decision this supports:** Targeting post-fire budget, telling utilities, insurers and councils which burnt areas are regrowing fast enough to rebuild vegetation-contact and fuel-load risk (and so need re-prioritised inspection) versus which are recovering slowly (flagging erosion, slope exposure, or active revegetation spend).

**Why I built this:** I work in utility infrastructure in a fire-prone US region, where post-fire vegetation regrowth under powerlines is a live ignition-risk and vegetation-management problem. After a megafire an asset owner cannot treat the whole burn scar at once; the operational question is where and when regrowth re-establishes risk. This project answers that from free satellite imagery, using the largest single-ignition fire in Australian history. It also adds cloud-scale remote sensing (Google Earth Engine) to my open-source Python work.

**Method:**
1. Built cloud-masked pre-fire and post-fire Sentinel-2 median composites (Cloud Score+ masking)
2. Computed the Normalised Burn Ratio (NBR) for each and derived dNBR (burn severity) as the difference
3. Classified dNBR into USGS burn-severity classes and isolated the high-severity zone (dNBR >= 0.44)
4. Tracked NDVI quarterly across the high-severity zone from mid-2019 to early 2023 to trace the recovery trajectory

**Key findings:**
- The high-severity burn core covers ~1,218 km2, 27.9% of the study area: the footprint that carries the return-of-risk
- Green cover in that zone crashed 63% at peak impact (NDVI 0.78 pre-fire to 0.29 in Jan 2020), then returned to pre-fire levels by Apr 2022, about 2.25 years
- Regrowth rebounds fast (NDVI 0.29 to 0.54 in a single quarter): eucalypt recovery is vigorous, so fuel load and clearance risk return faster than a naive "recovery takes years" assumption implies

**Recommendation:** Because clearance and fuel-load risk rebuild inside roughly two years, vegetation-management and line-clearance inspection cycles in high-severity zones should tighten well before the two-year mark, not after. The workflow runs on free imagery and reruns on any fire perimeter, so it scales across a whole network's fire exposure as a repeatable quarterly monitoring layer rather than a one-off study, letting an asset owner trigger action when a management zone crosses a chosen recovery threshold.

**Data:** Sentinel-2 Surface Reflectance and Cloud Score+ (both open, via Google Earth Engine)

- [View Project, Map & Code](https://github.com/joseph-pradil/gis-portfolio/tree/main/07-nsw-postfire-recovery)

**Limitations / next steps:** NDVI is a proxy for greenness, not fuel structure or canopy height, so "green is back" is not yet "clearance is breached." A bounding-box study area slightly over-counts; swapping in the official NSW RFS fire-extent polygon would tighten the figures. The natural next build pairs this with LiDAR-derived canopy height to convert recovery into actual powerline-clearance breaches, and adds a recovery-rate threshold per management zone to trigger inspections automatically.

## Connect
- LinkedIn: https://www.linkedin.com/in/joseph-pradil-bolleddu-45277921a/
- Email: josephpradil@gmail.com
