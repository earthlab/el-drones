This document is a working guide for post-processing UAS field missions using the Phantom 4 Pro for forest ecological applications. Major source of information is Megan Cattau's [UASWorkflows repo](https://github.com/mcattau/UASWorkflows) 


1. Open Metashape and save project in a sensible place (File -> save)  
2. Set preferences (MetashapePro -> preferences)  
    - -> GPU-> Check box for GPU if there is one available, check box for Use CPU when performing…)  
3. Add photos (Workflow menu in top toolbar -> add photos (or folder))   
    - Select single (e.g., Phantom4Pro camera) or multi-camera system (e.g., Kernel cam).  
    - Import all photos, including reflectance cal target photos (have to repeat this if images are in separate folders)  
    - Note: Cal photos need to go in a separate folder for calibration images in the Workspace pane. They may be automatically detected at import (if noted in metadata), automatically detected at the next step, or manually moved later.  
4. Clean photos up / check them  
    - Remove outlier photos (e.g., one taken during take-off) manually in Model workspace
    - Check camera calibration (from EXIF files) (tools-> Camera calibration) exiftool  
5. Estimate image quality  
    - In Photos workspace, change view to detailed > select all photos > right-click > Estimate Image Quality...  
    - Takes a while  
    - Disable all images that have an image quality below 0.7-0.85  
6. If reflectance panel -> Run reflectance calibration  
    - Tools-> Calibrate reflectance-> Locate panels  
    - Input calibration data for panel as a CSV, or manually  
    - Check on “Use reflectance panels” and “Use sun sensor” options in the Calibrate Reflectance dialog to perform calibration based on panel data and/or image meta information. Click OK to start the calibration process  

7. Align photos (workflow->) same as generating sparse point cloud  
    - High accuracy, generic preselection, reference preselection, key and tie point limits to default (40,000 and 4,000 respectively) Adaptive model fitting – yes Apply masks if using a mask  

8. GCPs  
    - Add Markers (3rd icon from left in Workspace toolbar, 1st icon from left in Reference toolbar)  
    - Convert GPS coordinates of your geotagged images to match the coordinate system of your ground control points (GCPs). Select datum coordinate systems for Cameras and Markers (spatialreference.org if need new datum to import into project).  
        - Check that coordinate system is correct (Phantom 4 Pro is WGS 84 (EPSG::4326)), columns in correct order  
        - Make sure there’s a checkmark in the box next to “Accuracy” and specify the correct accuracy (m) for long/lat/elev  
        - Delimiter: Comma so that csv cells would go into correct columns  
        - Items: Markers   
        - Yes to all for creating markers. Click on flag icon in top toolbar to make them appear  
        - Note: altitude information stored in the EXIF data of imagery acquired by DJI drones is the relative altitude from the point of take off and not the absolute/real world altitude. Here are 3 ways to fix this issue: http://www.agisoft.com/forum/index.php?topic=4986.msg38769#msg38769  
    - Verify and link markers to images
        - Right click on GCP -> filter by markers
        - View-> photos. Double click each photo
        - Make sure marker is in correct place. Mark each GCP in 3-6 images (right click -> Place markers - > click correct marker)
        - Do for all GCPs (or 4-5 at least)  
    - Click update button in reference pane  
        - Agisoft’s description through correspondence (AIS): Update - after adjusting marker locations on the photos, you recalculate the coordinates and calculate errors given the position of the GCP.  
    - Right click on GCP -> filter by markers (gives you rest of photos with GCP in them)  
    - Uncheck all images and 20-30% of GCPs so you can use them as checkpoints to confirm measurements (if you correct EXIF altitude, then don’t have to uncheck cameras)   
    - Update  
9. Optimize Cameras (tools ->) to improve alignment accuracy  
    - Check all but bottom left one (Fit k4) and bottom right 2 (Fit p3 and p4). Don’t check advanced (Adaptive camera model fitting and est tie point covariance)  
    - Agisoft’s description of through correspondence (AIS): Optimize cameras - you refine the camera calibration parameter values based on the calculated values after the images are aligned.   
10. Build Dense point cloud (workflow ->)  
    - Model > Transform region > Resize region?  
    - High or Medium quality (higher quality more accurate but increase processing time), aggressive depth filtering, check box for calculate point colors)  
    - If depth maps already exist, you can reuse these maps in the dense point cloud generation by selecting “Reuse depth maps” in the dense point cloud build window.  

(Optional: Build Mesh from dense cloud and Texture)

11. Build DEM (workflow ->)  
    - For orthomosaic generation – faster than mesh (but mesh may be required for complex terrain)  
    - Geographic type, check that it’s correct projection  
    - Source data: dense cloud  
    - Interpolation: Extrapolated (interpolation – enabled would leave elevation values only for areas seen by a camera)  
    - Check resolution  
12. Build orthomosaic (workflow ->)
    - DEM surface
    - Select if you want blending, otherwise Mosaic (default)
    - Enable hole filling
    - Check pixel size (can check meters button)
13.	If calculating indices -> Calculate required index information
    - Tools-> set raster transformation-> transform tab

14.	Export results (file->export)
    - Both the pointcloud and the DEM


#### Notes and other references
At least 8 or so markers
GSD 1/3 of accuracy you need

[Agisoft user manual](https://www.agisoft.com/pdf/photoscan-pro_1_3_en.pdf)

https://www.agisoft.com/forum/index.php?topic=7851.msg37494#msg37494

https://agisoft.freshdesk.com/support/solutions/articles/31000148381-micasense-altum-processing-workflow-including-reflectance-calibration-in-agisoft-metashape-professi

https://www.youtube.com/watch?v=CG11F0RX8WE&list=PL2UsAzNdeUas6e8FUh3Sjpqqcxf2Bzh81


