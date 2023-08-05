var layerLoadErrorMessages=[];showMessage('Loading',staticTemplates.loadingModal[mode]);
function runGeeViz(){
try{
	Map2.addSerializedLayer({"result": "0", "values": {"1": {"functionInvocationValue": {"functionName": "Image.select", "arguments": {"bandSelectors": {"constantValue": ["tStart", "tEnd", "tBreak", "changeProb", "red.*", "nir.*", "swir1.*", "swir2.*", "NDVI.*", "NBR.*"]}, "input": {"argumentReference": "_MAPPING_VAR_0_0"}}}}, "0": {"functionInvocationValue": {"functionName": "ImageCollection.mosaic", "arguments": {"collection": {"functionInvocationValue": {"functionName": "Collection.map", "arguments": {"baseAlgorithm": {"functionDefinitionValue": {"argumentNames": ["_MAPPING_VAR_0_0"], "body": "1"}}, "collection": {"functionInvocationValue": {"functionName": "ImageCollection.load", "arguments": {"id": {"constantValue": "projects/lcms-292214/assets/CONUS-LCMS/Base-Learners/CCDC-Collection-1984-2022"}}}}}}}}}}}},{},'Raw CCDC Output',true);
}catch(err){
	layerLoadErrorMessages.push("Error loading: Raw CCDC Output<br>GEE "+err);}
if(layerLoadErrorMessages.length>0){showMessage("Map.addLayer Error List",layerLoadErrorMessages.join("<br>"));}
setTimeout(function(){if(layerLoadErrorMessages.length===0){$('#close-modal-button').click();}}, 2500);
synchronousCenterObject({"type": "Polygon", "coordinates": [[[-180, -90], [180, -90], [180, 90], [-180, 90], [-180, -90]]]})
$('#query-label').click();
queryWindowMode = "sidePane"
}