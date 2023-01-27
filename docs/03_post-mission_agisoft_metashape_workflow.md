This document is a working guide for post-processing UAS field missions for forest ecological applications. These instructions are built off of a guide posted in this [Agisoft forum post](https://www.agisoft.com/forum/index.php?topic=7851.0). Also see Megan Cattau's [UASWorkflows repo](https://github.com/mcattau/UASWorkflows)


1. Open Metashape and save project in a sensible place (File -> save)  
2. Set preferences (MetashapePro -> preferences)  
    - -> GPU-> Check box for GPU if there is one available, check box for Use CPU when performing…)  
3. Import photos (Workflow menu in top toolbar -> add photos (or folder--adding the entire folder is often easiest))   
    - Select single (e.g., Phantom4Pro camera) or multi-camera system (e.g., Kernel camera (Micasense))
    - - When uploading a folder of images for a multi-camera system, will need to select “Multi-camera system: arrange images based on meta data.” It is okay to have subfolders included in the folder (i.e. adding a folder with subfolders of "Camera1" and "Camera2" will add all photos from both subfolders).
    - Import all photos, including reflectance cal target photos (have to repeat this if images are in separate folders)  
    - Note: Cal photos need to go in a separate folder for calibration images in the Workspace pane. They are often automatically detected at import (if noted in metadata), automatically detected at the next step, or manually moved later. 
4. Clean up photos 
    - Manually remove outlier photos (e.g.,  taken during take-off) in Model workspace
    - Check camera calibration (from EXIF files) (tools-> Camera calibration) exiftool  
5. Convert GPS coordinates of your geotagged images to match the coordinate system of your ground control points (GCPs) which will be imported later. Use the "convert" tab under the "Reference" panel and select the coordinate system from the "coordinate System" under "Convert Reference" dialog box. Verify coordinate system of imagery by clicking on chunk in Workspace pane and looking in bottom left corner.
    - Phantom 4 imagery is in WGS84 (EPSG::4326) by default
    - Phantom 4 vertical height is notoriously imprecise. Use relative rather than absolute camera height. Follow instructions in [this link](https://agisoft.freshdesk.com/support/solutions/articles/31000152491-working-with-dji-photos-altitude-problem-) to use DJI relative height and then add take-off height.
    - See [this link](http://www.agisoft.com/forum/index.php?topic=4986.msg38769#msg38769) for trouble-shooting vertical height with a Phantom 4.  
6. Estimate image quality  
    - In Photos workspace, change view to detailed > select all photos > right-click > Estimate Image Quality... 
    - Disable all images that have an image quality below 0.7  
7. If reflectance panel (e.g. with Micasense camera) -> Run reflectance calibration  
    - Tools-> Calibrate reflectance-> Locate panels  
    - Input calibration data for panel as a CSV, or manually  
    - Check on “Use reflectance panels” and “Use sun sensor” (if had a sun sensor & using data) options in the Calibrate Reflectance dialog to perform calibration based on panel data and/or image meta information. Click OK to start the calibration process  
8. Generate masks if necesary (for example, if you don't want to include cars or other moving objects)
9. Align photos (workflow->) same as generating sparse point cloud  
    - High accuracy, generic preselection, reference preselection, key and tie point limits to default (40,000 and 4,000 respectively) Adaptive model fitting – yes Apply masks if using a mask  
    - Can experiment the best key and tie point limits for the project. Some projects use (40,000 and 10,000 respectively) or (40,000 and no value for tie point limit (aka unlimited) respectively)
10. GCPs  
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
11. Assuming that you have a sufficient number (~8 or more)  of high accuracy ground control points, uncheck all images in the reference pane and also uncheck a few GCPs (20 to 30%) in order to use them as check points instead of control points. This will give you a better measure of the 'real accuracy' of your dataset. Note that the layout/distribution of GCPs is very important. If you have been able to correct the EXIF altitude information for all your cameras, then you do not have to uncheck the cameras in the reference pane. They can be used as reference as long as the right camera accuracy settings (leave default 10m) have been chosen.
12. Clean sparse point cloud (Model > GRADUAL SELECTION). Remove all points with high reprojection error (choose a value below 1, suggest using 0.5-0.8 ) and high reconstruction uncertainty (try to find the 'natural threshold' by moving the slider).
13. Adjust bounding box
14. Optimize Cameras (tools ->) to improve alignment accuracy  
    - Check all but bottom left one (Fit k4) when using DJI imagery. Don’t check advanced (Adaptive camera model fitting and est tie point covariance)  
    - Agisoft’s description of through correspondence (AIS): Optimize cameras - you refine the camera calibration parameter values based on the calculated values after the images are aligned.    
15. Build Dense point cloud (workflow ->)    
    - High or Medium quality (higher quality more accurate but increase processing time), aggressive depth filtering, check box for calculate point colors)  
    - If depth maps already exist, you can reuse these maps in the dense point cloud generation by selecting “Reuse depth maps” in the dense point cloud build window.  
16. Build mesh (not needed if you just want a DEM and/or orthophotograph)  
17. Build texture (not needed if you just want a DEM and/or orthophotograph)  
18. Build DEM from dense cloud (workflow ->)   
    - For orthomosaic generation – faster than mesh (but mesh may be required for complex terrain)  
    - Geographic type, check that it’s correct projection  
    - Source data: dense cloud  
    - Interpolation: Extrapolated (interpolation – enabled would leave elevation values only for areas seen by a camera)  
    - Check resolution  
19. Build orthomosaic based on DEM (workflow ->)
    - DEM surface
    - Select if you want blending, otherwise Mosaic (default)
    - Enable hole filling
    - Check pixel size (can check meters button)
20.	If calculating indices -> Calculate required index information
    - Tools-> set raster transformation-> transform tab
21. Classify ground points (takes a long time)
22.	Export results (file->export)
    - Both the pointcloud and the DEM


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
