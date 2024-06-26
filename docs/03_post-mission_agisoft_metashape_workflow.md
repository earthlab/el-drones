This document is a working guide for post-processing UAS field missions for forest ecological applications. These instructions are built off of a guide posted in this [Agisoft forum post](https://www.agisoft.com/forum/index.php?topic=7851.0). Also see Megan Cattau's [UASWorkflows repo](https://github.com/mcattau/UASWorkflows)

0. If you are operating on CU Boulder research computing resources, before the FIRST time you ever use Metashape, run this line of code from the terminal:

   echo "umask 0000" >> ~/.metashape
   
   This will ensure that all of your Metashape files and directories have open permissions (the default settings are a pain)
2. Open Metashape and save project in a sensible place (File -> save)
   - To open metashape on  CURC, open a terminal and type the following code lines:
        - source ~/.metashape
        - metashape
    - When saving your file, keep the file naming structure as the plot or transect directory you are working in and add _METASHAPE to the end. If you are processing for Macrosystems, add either M300_METASHAPE or MINI2_METASHAPE to the end.
4. Set preferences (Tools -> preferences)  
    - -> GPU-> Check box for GPU if there is one available, check box for Use CPU when performing…)  
5. Import photos (Workflow menu in top toolbar -> add photos (or folder--adding the entire folder is often easiest))   
    - Select single (e.g., Phantom4Pro camera) or multi-camera system (e.g., Kernel camera (Micasense))
    - - When uploading a folder of images for a multi-camera system, will need to select “Multi-camera system: arrange images based on meta data.” It is okay to have subfolders included in the folder (i.e. adding a folder with subfolders of "Camera1" and "Camera2" will add all photos from both subfolders).
    - Import all photos, including reflectance cal target photos (if you have them, i.e. for MicaSense camera) (have to repeat this if images are in separate folders)  
    - Note: Cal photos need to go in a separate folder for calibration images in the Workspace pane. They are often automatically detected at import (if noted in metadata), automatically detected at the next step, or manually moved later.
6. Clean up photos 
    - Manually remove outlier photos (e.g.,  taken during take-off) in Model workspace
    - Check camera calibration (from EXIF files) (tools-> Camera calibration) exiftool  
7. Convert GPS coordinates of your geotagged images to match the coordinate system of your ground control points (GCPs) which will be imported later. Use the "convert" tab under the "Reference" panel and select the coordinate system from the "coordinate System" under "Convert Reference" dialog box. Verify coordinate system of imagery by clicking on chunk in Workspace pane and looking in bottom left corner.
    - For all Macrosystems project imagery, convert coordinates to EPSG::5070.
    - Phantom 4 imagery is in WGS84 (EPSG::4326) by default
    - Phantom 4 vertical height is notoriously imprecise. Use relative rather than absolute camera height. Follow instructions in [this link](https://agisoft.freshdesk.com/support/solutions/articles/31000152491-working-with-dji-photos-altitude-problem-) to use DJI relative height and then add take-off height.
    - See [this link](http://www.agisoft.com/forum/index.php?topic=4986.msg38769#msg38769) for trouble-shooting vertical height with a Phantom 4.  
9. Estimate image quality  
    - In Photos workspace, change view to detailed > select all photos > right-click > Estimate Image Quality... 
    - Disable all images that have an image quality below 0.7  
10. If reflectance panel (e.g. with Micasense camera) -> Run reflectance calibration  
    - Tools-> Calibrate reflectance-> Locate panels  
    - Input calibration data for panel as a CSV, or manually  
    - Check on “Use reflectance panels” and “Use sun sensor” (if had a sun sensor & using data) options in the Calibrate Reflectance dialog to perform calibration based on panel data and/or image meta information. Click OK to start the calibration process  
    - Please refer [this page](https://support.micasense.com/hc/en-us/articles/115000765514-Use-of-Calibrated-Reflectance-Panels-For-MicaSense-Data) for more information on calibration panel and [this page](https://agisoft.freshdesk.com/support/solutions/articles/31000148780-micasense-rededge-mx-processing-workflow-including-reflectance-calibration-in-agisoft-metashape-pro#Appendix-C.-Controlling-reflectance-calculation) for calibration process.
    - If you need to find the calibration panel manually, it is here: /pl/active/earthlab/macrosystem/UAS/PanelCalibration/RP06-2104096-OB.csv
11. Generate masks if necesary (for example, if you don't want to include cars or other moving objects. Should not be necessary for Macrosystems & CAREER)
12. Align photos (workflow->) same as generating sparse point cloud  
    - High accuracy, generic preselection, reference preselection, key and tie point limits to default (40,000 and 4,000 respectively)
    - Under advanced, check Adaptive model fitting
    - Apply masks if using a mask  
    - Can experiment the best key and tie point limits for the project. Some projects use (40,000 and 10,000 respectively) or (40,000 and no value for tie point limit (aka unlimited) respectively)
    - Macrosystems uses 40,000 & 4,000 for key and tie point limits
13. GCPs  (if your flight was performed with GCPs)
    - Add Markers (3rd icon from left in Workspace toolbar, 1st icon from left in Reference toolbar)  
    - Specify accuracy for markers
    - Delimiter: Comma so that csv cells would go into correct columns  
    - Items: Markers   
    - Yes to all for creating markers. Click on flag icon in top toolbar to make them appear  
    - Verify and link markers to images
        - Right click on GCP -> filter by markers
        - View-> photos. Double click each photo. If using a non-RGB sensor, such as a MicaSense RedEdge, your photos may appear completely dark. If so, go to: Tools -> Set Brightness -> Estimate (or adjust manually) -> Apply
        - Make sure marker is in correct place. If not move the marker to the correct place. repeat this process for each GCP in 3-6 images (right click -> Place markers - > click correct marker)
        - Do for all GCPs (or 4-5 at least)  
    - Update  
        - Agisoft’s description through correspondence (AIS): Update - after adjusting marker locations on the photos, you recalculate the coordinates and calculate errors given the position of the GCP.  (Reference pane, sixth button in from the left, 'Update Transform')
14. Assuming that you have a sufficient number (~8 or more)  of high accuracy ground control points, uncheck all images in the reference pane and also uncheck a few GCPs (20 to 30%) in order to use them as check points instead of control points. This will give you a better measure of the 'real accuracy' of your dataset. Note that the layout/distribution of GCPs is very important. If you have been able to correct the EXIF altitude information for all your cameras, then you do not have to uncheck the cameras in the reference pane. They can be used as reference as long as the right camera accuracy settings (leave default 10m) have been chosen.
15. Clean sparse point cloud (Model > GRADUAL SELECTION). Remove all points with high reprojection error (choose a value below 1, suggest using 0.5-0.8 ) and high reconstruction uncertainty (try to find the 'natural threshold' by moving the slider).
16. Adjust bounding box
17. Optimize Cameras (tools ->) to improve alignment accuracy  
    - Check all but bottom left one (Fit k4) when using DJI imagery. Don’t check advanced (Adaptive camera model fitting and est tie point covariance)  
    - Agisoft’s description of through correspondence (AIS): Optimize cameras - you refine the camera calibration parameter values based on the calculated values after the images are aligned.    
18. Build Dense point cloud (workflow ->)    
    - High or Medium quality (higher quality more accurate but increase processing time), aggressive depth filtering, check box for calculate point colors)
         - (Ideally High unless major processing bottleneck)
         - Macrosystems uses High
    - If depth maps already exist, you can reuse these maps in the dense point cloud generation by selecting “Reuse depth maps” in the dense point cloud build window.  
19. Build mesh (not needed if you just want a DEM and/or orthophotograph)
    - Not necessary for Macrosystems RGB imagery 
21. Build texture (not needed if you just want a DEM and/or orthophotograph)
    - Not necessary for Macrosystems RGB imagery 
23. Build DEM from dense cloud (workflow ->)   
    - For orthomosaic generation – faster than mesh (but mesh may be required for complex terrain)  
    - Geographic type, check that it’s correct projection  
    - Source data: dense cloud  
    - Interpolation: Extrapolated (interpolation – enabled would leave elevation values only for areas seen by a camera)  
    - Check resolution  
24. Build orthomosaic based on DEM (workflow ->)
    - DEM surface
    - Select if you want blending, otherwise Mosaic (default)
    - Enable hole filling
    - Check pixel size (can check meters button)
25.	If calculating indices -> Calculate required index information
    - Tools-> set raster transformation-> transform tab
    - Not necessary for Macrosystems
27. Create a Digital Terrain Model (DTM)
    - Macrosystems: Only do this with Matrice Imagery
    - First, create a copy of your chunk (Metashape only allows one file of each type per chunk, meaning that the DEMs will overwrite one another if this process is all done in a single chunk)
          - In your workspace, right click on 'Chunk 1' and then 'Duplicate...'
          - De-select everything exept for 'Dense Clouds' and then complete the process
          - You should now have a 'Copy of chunk 1' in your workspace. Right click on it and rename it to 'DTM Chunk'. Make this copied chunk active by either double-clicking on it, or right-clicking on it and selecting 'Set active' from the menu. The name should become bold.
    - Classify ground points
        - With this new chunk active, select 'Tools' from the menu. Under 'Dense Cloud', select 'Classify Ground Points.' [This page provides a good overview of the parameters for this tool and what it is doing.](https://agisoft.freshdesk.com/support/solutions/articles/31000160729-parameters-for-ground-point-classification#:~:text=For%20nearly%20flat%20terrain%20it,the%20terrain%20contains%20steep%20slopes.)
        - Leave the 'Classes' parameters as default
        - Under Parameters you will want: Max angle = 15, Max distance = 1, Cell size = 30 OR 50 (50 if there is a lot of dense vegetation), Erosion radius = 0. While these parameters aren't optimized for each location, they should be good enough for basic canopy height calculations. Click 'OK'
    - Build a Mesh from your new classified ground points
        - Now go to 'Workflow' and 'Build Mesh...'
        - Leave the general defaults. Under 'Advanced' click 'Select' next to where it says 'Point classes: All'
        - De-select the point classes until ONLY 'Ground' is still checked. Click 'OK'
        - Click 'Ok' - the Mesh will process, which may take a moment
        - You should now have a 3D model under 'DTM Chunk'
    - Create a DTM from the new mesh
        - Click 'Workflow' in the menu, and then 'Build DEM...'
        - Change your 'Source data:' to 'Mesh' to use the new mesh you've created
        - Click 'Ok' - the DEM will process, which may take a moment
        - You should now have a DEM under 'DTM Chunk'
        - Right click on the new DEM and rename it to 'DTM'
29. Create a canopy height model from the original DEM and the DTM
    - Macrosystems: Only do this with Matrice Imagery
    - Activate 'Chunk 1' again
    - In the menu, go to "Tools" and then under "DEM" select 'Transform DEM..."
        - Click 'Calculate difference'
        - In the dropdown menu, select your DTM from the list (it should be named 'DTM' under the chunk called 'DTM Chunk')
        - Click 'OK'
        - You will be asked if you want to replace the default DEM - CLICK 'NO'!
        - A second DEM will appear under the first one. Rename it to 'Canopy Height'
31. Load a shapefile to set as the export boundary for the project if you want to clip to a shapefile
    - Unnecessary for Macrosystems
    - File -> Import -> Import Shapes...
    - Your project should have a 'Metadata' folder in its file structure. Open the folder and select the .shp file that starts with 'UsableArea...'
    - It will ask you for the projection - is should default to what your project already is (you converted coordinates in Step 6). Note that to make this work the shapefile .prj file has been DELETED from the directories to prompt this dialogue box. For some reason Metashape doesn't want to read the .prj files correctly.
    - Under Chunk 1 you should now see a 'Shapes' folder with 'Layer' in it (probably '1 polygon')
    - Click on the 'Ortho' tab of your processing space. You should see a white boundary
    - Click this white boundary; it should turn red-ish.
    - Right click and then 'Set boundary type...' -> 'Outer boundary'
    - Click on your ortho to make the boundary white again - it should now have black dashes in it
    - Your exports of all DEM and ortho layers should export as clipped by this boundary; when you export something, you can select/de-select 'Clip to boundary shapes'
33.	Export results to the 'Outputs' folder for your project
    - Make Chunk 1 active
        - Right click on the Dense Cloud and 'Export Dense Cloud...' Export the points with the appropriate name and then '_POINTCLOUD'. The filetype will be .laz (the default)
             - If you are exporting a large point clouds (i.e. CAREER project transects), these will need to be tiled. In the dense cloud export dialogue (after you choose your file name), check the box next to "Split in blocks (m):" and then put in your block size. For CAREER processing, use 100x100m.
             - You can also clip to boundary shapes, just as with any .tif file
        - Right click on the DEM and 'Export DEM...' Export the DEM with the appropriate name and then '_DEM'. If you have a shapefile boundary loaded up (see above), make sure that you have 'Clip to boundary shapes' selected.
        - Right click on the orthomosaic and 'Export Orthomosaic...' Export the orthomosaic with the appropriate name and then '_ORTHO'. If you have a shapefile boundary loaded up (see above), make sure that you have 'Clip to boundary shapes' selected.
        - Right click on the Canopy Height layer and 'Export DEM...' Export the Canopy Height with the appropriate name and then "_CANOPYHEIGHT". If you have a shapefile boundary loaded up (see above), make sure that you have 'Clip to boundary shapes' selected.
    - Make DTM chunk active
        - Right click on the DTM and 'Export DEM...' Export the DTM with the appropriate name and then -DTM. If you have a shapefile boundary loaded up (see above), make sure that you have 'Clip to boundary shapes' selected.
34. Generate the processing report
    - File -> Export -> Generate Report
    - Keep all defaults, but re-name it to the appropriate name and then "_report". Click 'ok'
    - Make sure it exports in the 'Outputs' folder for your project with the right name



#### Notes and other references
At least 8 or so markers
GSD 1/3 of accuracy you need

[Agisoft user manual](https://www.agisoft.com/pdf/photoscan-pro_1_3_en.pdf)

https://www.agisoft.com/forum/index.php?topic=7851.msg37494#msg37494

https://agisoft.freshdesk.com/support/solutions/articles/31000148381-micasense-altum-processing-workflow-including-reflectance-calibration-in-agisoft-metashape-professi

https://www.youtube.com/watch?v=CG11F0RX8WE&list=PL2UsAzNdeUas6e8FUh3Sjpqqcxf2Bzh81

Suggestions for DJI photos added from: https://agisoft.freshdesk.com/support/solutions/articles/31000152491-working-with-dji-photos-altitude-problem-

Misc: if Phantom RTK is used, enable "load camera location accuracy from XMP meta data" option in the Advanced preferences tab prior to the image loading in order to read and apply the measurement accuracy of the camera locations data. 

[Cool resource](https://www.unavco.org/software/geodetic-utilities/geoid-height-calculator/geoid-height)
