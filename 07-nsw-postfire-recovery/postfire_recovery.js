// =====================================================================
// Post-Fire Vegetation Recovery - Gospers Mountain Fire, NSW (2019-2020)
// Paste into the GEE Code Editor: https://code.earthengine.google.com
// Quick visual companion to the Python pipeline (the canonical artifact).
// =====================================================================

var aoi = ee.Geometry.Rectangle([150.2, -33.2, 150.9, -32.6]);
Map.centerObject(aoi, 10);

var PRE_START  = '2019-09-01', PRE_END  = '2019-10-20';
var POST_START = '2020-02-01', POST_END = '2020-03-31';

var S2     = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED');
var CSPLUS = ee.ImageCollection('GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED');
var CS_BAND = 'cs', CLEAR = 0.6;

function maskS2(img){ return img.updateMask(img.select(CS_BAND).gte(CLEAR)); }
function prep(s, e){
  return S2.filterBounds(aoi).filterDate(s, e)
           .linkCollection(CSPLUS, [CS_BAND]).map(maskS2);
}
function addNBR(img){
  return img.addBands(img.normalizedDifference(['B8','B12']).rename('NBR'));
}

var pre  = prep(PRE_START,  PRE_END ).map(addNBR).median().clip(aoi);
var post = prep(POST_START, POST_END).map(addNBR).median().clip(aoi);
var dnbr = pre.select('NBR').subtract(post.select('NBR')).rename('dNBR');

Map.addLayer(dnbr,
  {min:-0.1, max:1.0, palette:['0000ff','ffffff','ffff00','ff8c00','ff0000']},
  'dNBR (burn severity)');

var highSev = dnbr.gte(0.44);
var series = prep('2019-07-01','2023-02-01').map(function(img){
  var ndvi = img.normalizedDifference(['B8','B4']).rename('NDVI');
  return ndvi.updateMask(highSev).set('system:time_start', img.get('system:time_start'));
});

var chart = ui.Chart.image.series(series, aoi, ee.Reducer.mean(), 100)
  .setOptions({
    title: 'NDVI recovery in high-severity burn zone - Gospers Mountain',
    vAxis: {title: 'Mean NDVI'},
    hAxis: {title: 'Date'},
    lineWidth: 2, pointSize: 3
  });
print(chart);
